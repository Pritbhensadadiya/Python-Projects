import json
from pathlib import Path

# Path to the JSON storage file
STORAGE_FILE = Path(__file__).resolve().parent.parent / "storage" / "analyses.json"


def load_history():
    """
    Load all saved startup analyses.
    """

    if not STORAGE_FILE.exists():
        return []

    try:
        with open(STORAGE_FILE, "r", encoding="utf-8") as file:
            return json.load(file)

    except (json.JSONDecodeError, FileNotFoundError):
        return []


def save_history(history):
    """
    Save the complete analysis history.
    """

    with open(STORAGE_FILE, "w", encoding="utf-8") as file:
        json.dump(history, file, indent=4)


def add_analysis(analysis):
    """
    Add a new startup analysis to history.
    """

    history = load_history()

    history.insert(0, analysis)

    save_history(history)

    return analysis
