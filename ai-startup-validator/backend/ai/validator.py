from copy import deepcopy

from backend.ai.schema import STARTUP_ANALYSIS_SCHEMA


def validate_analysis_response(response: dict) -> dict:
    """
    Validate the AI response against the expected schema.

    Missing fields are filled with default values.
    Extra fields are ignored.
    Invalid data types are replaced with defaults.
    """

    validated = deepcopy(STARTUP_ANALYSIS_SCHEMA)

    for key, default_value in STARTUP_ANALYSIS_SCHEMA.items():
        if key not in response:
            continue

        value = response[key]

        if isinstance(value, type(default_value)):
            validated[key] = value

    return validated
