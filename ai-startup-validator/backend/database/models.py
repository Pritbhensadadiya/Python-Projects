from .database import get_connection


def create_tables():
    """
    Create all database tables if they don't already exist.
    """

    connection = get_connection()
    cursor = connection.cursor()

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS startup_analyses (
        id INTEGER PRIMARY KEY AUTOINCREMENT,

        startup_name TEXT NOT NULL,
        description TEXT NOT NULL,
        industry TEXT NOT NULL,
        target_audience TEXT NOT NULL,
        country TEXT NOT NULL,
        business_stage TEXT NOT NULL,
        budget REAL,

        analysis_json TEXT NOT NULL,

        created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
    )
    """)

    connection.commit()
    connection.close()


import json


def save_analysis(
    startup_name,
    description,
    industry,
    target_audience,
    country,
    business_stage,
    budget,
    analysis,
):
    """
    Save a startup analysis to the database.
    """

    connection = get_connection()
    cursor = connection.cursor()

    cursor.execute(
        """
        INSERT INTO startup_analyses
        (
            startup_name,
            description,
            industry,
            target_audience,
            country,
            business_stage,
            budget,
            analysis_json
        )
        VALUES (?, ?, ?, ?, ?, ?, ?, ?)
        """,
        (
            startup_name,
            description,
            industry,
            target_audience,
            country,
            business_stage,
            budget,
            json.dumps(analysis),
        ),
    )

    connection.commit()
    connection.close()