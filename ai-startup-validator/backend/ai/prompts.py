from backend.ai.prompt_template import STARTUP_PROMPT_TEMPLATE


def build_startup_prompt(startup):
    return f"""
{STARTUP_PROMPT_TEMPLATE}

========================
STARTUP DETAILS
========================

Startup Name:
{startup.startup_name}

Description:
{startup.startup_description}

Industry:
{startup.industry}

Target Audience:
{startup.target_audience}

Country:
{startup.country}

Business Stage:
{startup.business_stage}

Budget:
{startup.budget}
"""
