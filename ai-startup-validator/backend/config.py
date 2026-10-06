import os

from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# ----------------------------------------
# Application
# ----------------------------------------

APP_NAME = "AI Startup Validator API"
APP_VERSION = "1.0.0"
APP_DESCRIPTION = "Backend API for AI Startup Validator"

# ----------------------------------------
# Gemini Configuration
# ----------------------------------------

GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")

# Primary model
GEMINI_MODEL = os.getenv("GEMINI_MODEL")

# Optional fallback model
GEMINI_FALLBACK_MODEL = os.getenv("GEMINI_FALLBACK_MODEL")
