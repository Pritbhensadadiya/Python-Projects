from fastapi import FastAPI  # noqa: I001
from backend.config import (APP_NAME,APP_VERSION,APP_DESCRIPTION,)
from backend.routes.startup import router as startup_router
from fastapi.middleware.cors import CORSMiddleware
from backend.config import (
    GEMINI_API_KEY,
    GEMINI_MODEL,
    GEMINI_FALLBACK_MODEL,
)
from backend.database.models import create_tables

def print_ai_status():
    print("\n" + "=" * 60)
    print("🚀 AI Startup Validator")
    print("-" * 60)

    print(f"API Key        : {'Loaded ✅' if GEMINI_API_KEY else 'Missing ❌'}")
    print(f"Primary Model  : {GEMINI_MODEL}")
    print(f"Fallback Model : {GEMINI_FALLBACK_MODEL or 'None'}")

    print("\nAI Client Ready ✅")
    print("=" * 60 + "\n")


app = FastAPI(
    title=APP_NAME,
    version=APP_VERSION,
    description=APP_DESCRIPTION,
)
create_tables()
print_ai_status()

app.include_router(startup_router, prefix="/api", tags=["Startup Validation"])

app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://127.0.0.1:5500",
        "http://localhost:5500",
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def home():
    return {
        "message": f"Welcome to {APP_NAME}!",
        "status": "Backend is running successfully.",
    }


@app.get("/health")
def health_check():
    return {"status": "healthy", "service": APP_NAME, "version": APP_VERSION}


