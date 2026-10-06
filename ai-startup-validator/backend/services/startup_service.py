from backend.ai.llm_client import generate_startup_analysis
from backend.ai.prompts import build_startup_prompt
from backend.schemas import StartupIdea


def validate_startup_idea(startup: StartupIdea):
    """
    Validate a startup idea using Gemini AI.
    """

    prompt = build_startup_prompt(startup)

    analysis = generate_startup_analysis(prompt)

    return analysis
