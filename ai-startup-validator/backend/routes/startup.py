from fastapi import APIRouter

from backend.schemas import StartupIdea
from backend.services.startup_service import validate_startup_idea
from backend.database.models import save_analysis

router = APIRouter()


@router.post("/validate")
def validate_startup(startup: StartupIdea):
    """
    Validate a startup idea using the AI service.
    """

    analysis = validate_startup_idea(startup)

    # Save analysis to SQLite
    save_analysis(
        startup_name=startup.startup_name,
        description=startup.startup_description,
        industry=startup.industry,
        target_audience=startup.target_audience,
        country=startup.country,
        business_stage=startup.business_stage,
        budget=startup.budget,
        analysis=analysis,
    )

    return analysis
