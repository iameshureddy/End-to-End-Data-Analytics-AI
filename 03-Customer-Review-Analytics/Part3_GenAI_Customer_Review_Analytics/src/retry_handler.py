"""
===============================================================================
TASK 3
Retry-on-Failure Handler

Objective
---------
Provide a reusable retry mechanism for all LLM API calls.

This module wraps the reusable `call_llm()` function from Task 2 and
automatically retries failed API requests.

Features
--------
✔ Retries failed requests up to 3 times.
✔ Handles temporary API failures gracefully.
✔ Prevents the entire program from crashing.
✔ Logs descriptive error messages.
✔ Returns None after exhausting all retry attempts.

Workflow
--------
Prompt
   │
   ▼
safe_call_llm()
   │
   ▼
call_llm()
   │
   ▼
Success?
 ├── Yes → Return Response
 └── No
        │
        ▼
Retry (Maximum 3 Attempts)
        │
        ▼
Still Failed?
 ├── Yes → Return None
 └── No  → Return Response
===============================================================================
"""

# =============================================================================
# Import Required Libraries
# =============================================================================

import time

from llm_wrapper import call_llm


# =============================================================================
# Retry Function
# =============================================================================

def safe_call_llm(
    prompt,
    temperature=0.3,
    max_tokens=512,
    max_retries=3
):
    """
    Safely call the Gemini API with retry support.

    Parameters
    ----------
    prompt : str
        Input prompt.

    temperature : float
        Controls randomness.

    max_tokens : int
        Maximum output tokens.

    max_retries : int
        Maximum retry attempts.

    Returns
    -------
    str
        Generated response.

    None
        If all retries fail.
    """

    attempt = 1

    while attempt <= max_retries:

        try:

            response = call_llm(
                prompt=prompt,
                temperature=temperature,
                max_tokens=max_tokens
            )

            if response:

                return response

            raise Exception("Empty response received from Gemini.")

        except Exception as error:

            print("\n" + "=" * 70)
            print(f"Retry Attempt {attempt} of {max_retries}")
            print("=" * 70)
            print(error)

            if attempt == max_retries:

                print("\nMaximum retry attempts reached.")
                print("Skipping this request.\n")

                return None

            print("Retrying in 5 seconds...\n")

            time.sleep(5)

            attempt += 1


# =============================================================================
# Test Module
# =============================================================================

if __name__ == "__main__":

    sample_prompt = """
Explain what Artificial Intelligence is in one sentence.
"""

    response = safe_call_llm(
        prompt=sample_prompt,
        temperature=0.2,
        max_tokens=100
    )

    print("\nGenerated Response:\n")

    print(response)