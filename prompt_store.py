import streamlit as st

CLASSIFIER_PROMPT = """
Teacher agent prompt
"""

MATH_PROMPT = """
Math agent prompt
"""

READING_PROMPT = """
Reading agent prompt
"""

WRITING_PROMPT = """
Writing agent prompt
"""

def get_prompt_code(prompt_name, user="default"):
    prompt_mapping = {
        "classifier": CLASSIFIER_PROMPT,
        "math": MATH_PROMPT,
        "reading": READING_PROMPT,
        "writing": WRITING_PROMPT,
    }

def get_prompt(prompt_name, user="default"):
    return get_prompt_code(prompt_name, user)