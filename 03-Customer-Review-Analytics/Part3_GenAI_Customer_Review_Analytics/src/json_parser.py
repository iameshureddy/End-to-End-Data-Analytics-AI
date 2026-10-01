"""
===============================================================================
TASK 2
JSON Response Parser

Objective
---------
This module converts the JSON response returned by the Gemini API into
a Python dictionary.

Why is this Required?
---------------------
Large Language Models (LLMs) always return text. Even if the model is
instructed to return JSON, Python still receives it as a string.

Before the response can be used in the application, it must be:

1. Validated.
2. Converted into a Python dictionary.
3. Checked for parsing errors.

Responsibilities
----------------
1. Validate the JSON response.
2. Convert JSON text into a Python dictionary.
3. Handle invalid JSON gracefully.
4. Log parsing failures without crashing the application.

Project Flow
------------
Gemini API Response (String)
            │
            ▼
parse_json_response()
            │
            ▼
Python Dictionary
            │
            ▼
Prompt Comparison / Sentiment Analysis
===============================================================================
"""

# =============================================================================
# Import Required Library
# =============================================================================

import json


# =============================================================================
# JSON Parser Function
# =============================================================================

def parse_json_response(response_text, review_no=None, prompt_type=None):
    """
    Convert the JSON string returned by Gemini into a Python dictionary.

    Parameters
    ----------
    response_text : str
        Raw response returned by the Gemini API.

    review_no : int, optional
        Customer review number (used for logging).

    prompt_type : str, optional
        Prompt strategy name (Zero-shot, Few-shot, Role Prompt).

    Returns
    -------
    dict | None
        Parsed dictionary if successful.
        Returns None if JSON parsing fails.
    """

    # If no response was received from Gemini
    if response_text is None:

        print("\nNo response received from Gemini API.")

        return None

    try:

        # Convert JSON string into Python dictionary
        parsed_response = json.loads(response_text)

        return parsed_response

    except json.JSONDecodeError:

        print("\n" + "=" * 70)
        print("JSON Parsing Failed")
        print("=" * 70)

        if review_no is not None:
            print(f"Review Number : {review_no}")

        if prompt_type is not None:
            print(f"Prompt Type   : {prompt_type}")

        print("\nInvalid JSON Response:\n")
        print(response_text)

        return None


# =============================================================================
# Testing
# =============================================================================

if __name__ == "__main__":

    sample_response = """
    {
        "label": "positive",
        "confidence": "high",
        "reason": "Customer liked the product."
    }
    """

    result = parse_json_response(
        sample_response,
        review_no=1,
        prompt_type="Zero-shot"
    )

    print("\n" + "=" * 70)
    print("Parsed Dictionary")
    print("=" * 70)

    print(result)

    print("\nData Type")

    print(type(result))