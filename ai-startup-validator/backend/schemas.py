from pydantic import BaseModel  # noqa: I001
from typing import Optional


class StartupIdea(BaseModel):
    startup_name: str
    startup_description: str
    industry: str
    target_audience: str
    country: str
    business_stage: str
    budget: Optional[float] = None  # noqa: UP045
