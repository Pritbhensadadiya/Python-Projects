import json
import time
from typing import Any, Dict

from google import genai
from google.genai.errors import ClientError, ServerError

from backend.config import (
    GEMINI_API_KEY,
    GEMINI_MODEL,
    GEMINI_FALLBACK_MODEL,
)
from backend.ai.validator import validate_analysis_response

if not GEMINI_API_KEY:
    raise ValueError("GEMINI_API_KEY is missing. Please check your .env file.")

client = genai.Client(api_key=GEMINI_API_KEY)


def _call_model(model_name: str, prompt: str) -> Dict[str, Any]:
    """
    Send a prompt to the specified Gemini model and return the parsed JSON response.
    """

    print(f"Calling Gemini model: {model_name}")

    response = client.models.generate_content(
        model=model_name,
        contents=prompt,
    )

    if not response.text:
        raise ValueError("Gemini returned an empty response.")

    try:
        parsed_response = json.loads(response.text)

        validated_response = validate_analysis_response(parsed_response)

        return validated_response
    except json.JSONDecodeError as e:
        raise ValueError("Gemini returned an invalid JSON response.") from e


def generate_startup_analysis(prompt: str) -> Dict[str, Any]:
    """
    Generate a startup analysis using the configured Gemini model.

    Behaviour:
    - Retries temporary server errors.
    - Falls back to the secondary model if the primary model is unavailable.
    """

    retries = 3
    retry_delay = 3

    for attempt in range(1, retries + 1):
        try:
            print("=" * 60)
            print(f"Primary Model : {GEMINI_MODEL}")
            print(f"Fallback Model: {GEMINI_FALLBACK_MODEL or 'None'}")
            print("=" * 60)

            return _call_model(GEMINI_MODEL, prompt)

        except ServerError:
            print(
                f"Gemini server is busy "
                f"(Attempt {attempt}/{retries}). Retrying in {retry_delay} seconds..."
            )

            if attempt < retries:
                time.sleep(retry_delay)
                continue

            raise Exception(
                "Gemini is temporarily unavailable. Please try again later."
            )

        except ClientError as e:
            print(f"Primary model failed: {e}")

            if GEMINI_FALLBACK_MODEL:
                try:
                    print(f"Switching to fallback model: {GEMINI_FALLBACK_MODEL}")

                    return _call_model(
                        GEMINI_FALLBACK_MODEL,
                        prompt,
                    )

                except Exception as fallback_error:
                    raise Exception(
                        f"Fallback model also failed: {fallback_error}"
                    ) from fallback_error

            raise

        except Exception:
            raise

    raise Exception("Unable to generate startup analysis.")
