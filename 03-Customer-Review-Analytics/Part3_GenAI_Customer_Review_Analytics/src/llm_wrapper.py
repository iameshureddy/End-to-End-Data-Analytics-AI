"""
===============================================================================
TASK 2
Reusable LLM API Wrapper

Objective
---------
Create a reusable Python function for interacting with Google's Gemini API.

This module provides a single function, `call_llm()`, that can be reused
throughout the project for all LLM interactions.

Features
--------
✔ Loads API key securely from the .env file.
✔ Never hardcodes the API key.
✔ Accepts prompt, temperature and max_tokens as parameters.
✔ Sends requests to the Gemini API.
✔ Returns only the generated response text.
✔ Handles API errors gracefully.

Workflow
--------
User Prompt
      │
      ▼
call_llm()
      │
      ▼
Gemini API
      │
      ▼
Generated Response
===============================================================================
"""

# =============================================================================
# Import Required Libraries
# =============================================================================

import os

from dotenv import load_dotenv
import google.generativeai as genai


# =============================================================================
# Load Environment Variables
# =============================================================================

load_dotenv()

API_KEY = os.getenv("GEMINI_API_KEY")

if not API_KEY:
    raise ValueError(
        "GEMINI_API_KEY not found. Please add it to your .env file."
    )


# =============================================================================
# Configure Gemini API
# =============================================================================

genai.configure(api_key=API_KEY)



# =============================================================================
# Load Gemini Model
# =============================================================================

MODEL_NAME = "gemini-3.5-flash-lite"

model = genai.GenerativeModel(MODEL_NAME)


# =============================================================================
# Reusable API Wrapper Function
# =============================================================================

def call_llm(
    prompt,
    temperature=0.3,
    max_tokens=512
):
    """
    Send a prompt to Google's Gemini model.

    Parameters
    ----------
    prompt : str
        The input prompt to send to the LLM.

    temperature : float, optional
        Controls randomness in the generated output.

        Lower values:
            More deterministic.

        Higher values:
            More creative.

        Default:
            0.3

    max_tokens : int, optional
        Maximum number of output tokens.

        Default:
            512

    Returns
    -------
    str
        Generated response text.

    None
        If an API error occurs.
    """

    try:

        response = model.generate_content(

            prompt,

            generation_config=genai.GenerationConfig(

                temperature=temperature,

                max_output_tokens=max_tokens

            )

        )

        if response.text:

            return response.text.strip()

        return None

    except Exception as error:

        print("\n" + "=" * 70)
        print("LLM API ERROR")
        print("=" * 70)
        print(error)
        print("=" * 70)

        return None


# =============================================================================
# Test Module
# =============================================================================

if __name__ == "__main__":

    print("=" * 70)
    print("Testing LLM Wrapper")
    print("=" * 70)

    sample_prompt = """
Say hello in one sentence.
"""

    result = call_llm(

        prompt=sample_prompt,

        temperature=0.2,

        max_tokens=50

    )

    print("\nGenerated Response:\n")

    print(result)