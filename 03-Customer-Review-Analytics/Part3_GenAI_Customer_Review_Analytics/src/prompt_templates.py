"""
TASK 1
Prompt Engineering

Objective
---------
This module contains all prompt templates used in this project.

Three prompting strategies are implemented:

1. Zero-shot Prompt
2. Few-shot Prompt
3. Role-based Prompt

All three prompts instruct the model to return the same locked JSON schema
so that the responses can be parsed automatically in later tasks.

This module does not communicate with Gemini.
It only creates prompt strings.
"""


# =============================================================================
# Expected JSON Schema
# =============================================================================

JSON_SCHEMA = """
{
  "label": "positive|neutral|negative",
  "confidence": "low|medium|high",
  "reason": "short explanation"
}
"""


# =============================================================================
# Zero-shot Prompt
# =============================================================================

def build_zero_shot_prompt(review_text):
    """
    Create a Zero-shot prompt.

    Zero-shot prompting provides instructions without giving
    the model any worked examples.

    Parameters
    ----------
    review_text : str
        Customer review to classify.

    Returns
    -------
    str
        Complete prompt.
    """

    prompt = f"""
You are a customer review sentiment classifier.

Instruction:
Read the customer review carefully and classify its overall sentiment.

Classify the review into ONLY ONE of these labels:
- positive
- neutral
- negative

Constraints:
- Return ONLY valid JSON.
- Do not include markdown.
- Do not include any text outside the JSON object.
- The output must follow the exact schema below.

JSON Schema:
{JSON_SCHEMA}

Customer Review:
{review_text}

Return JSON only.
"""

    return prompt


# =============================================================================
# Few-shot Prompt
# =============================================================================

def build_few_shot_prompt(review_text):
    """
    Create a Few-shot prompt.

    Few-shot prompting provides three worked examples before
    asking the model to classify the actual review.

    Parameters
    ----------
    review_text : str
        Customer review to classify.

    Returns
    -------
    str
        Complete prompt.
    """

    prompt = f"""
You are a customer review sentiment classifier.

The following three examples demonstrate how customer reviews
should be classified.

Example 1

Review:
"The product quality is amazing and I love the fabric."

Output:
{{
  "label": "positive",
  "confidence": "high",
  "reason": "Customer is very satisfied with the product quality and fabric."
}}


Example 2

Review:
"Very poor stitching and terrible quality."

Output:
{{
  "label": "negative",
  "confidence": "high",
  "reason": "Customer is dissatisfied with the stitching and product quality."
}}


Example 3

Review:
"The design is nice, but I am unsure about the material."

Output:
{{
  "label": "neutral",
  "confidence": "medium",
  "reason": "The review contains positive feedback about design but uncertainty about material."
}}


Now classify the following customer review.

Constraints:
- Choose ONLY positive, neutral, or negative.
- Confidence must be low, medium, or high.
- Provide a short reason.
- Return ONLY valid JSON.
- Do not include markdown or additional text.
- Follow exactly the same JSON schema used in the examples.

JSON Schema:
{JSON_SCHEMA}

Customer Review:
{review_text}

Return JSON only.
"""

    return prompt


# =============================================================================
# Role-based Prompt
# =============================================================================

def build_role_prompt(review_text):
    """
    Create a Role-based prompt using the ECO framework.

    ECO:
    - Instruction
    - Context
    - Constraints
    - Output

    Parameters
    ----------
    review_text : str
        Customer review to classify.

    Returns
    -------
    str
        Complete prompt.
    """

    prompt = f"""
You are a Senior Customer Insights Analyst specializing in customer
feedback analysis for women's clothing products.

Instruction:
Analyze the customer review and classify its overall sentiment.

Context:
The review is customer feedback about a women's clothing product.
The goal is to identify whether the customer's overall experience
is positive, neutral, or negative.

Constraints:
- Use ONLY one sentiment label: positive, neutral, or negative.
- Confidence must be low, medium, or high.
- Provide a brief reason based only on the review.
- Do not invent information that is not present in the review.
- Return ONLY valid JSON.
- Do not include markdown.
- Do not include any text outside the JSON object.

Output:
{JSON_SCHEMA}

Customer Review:
{review_text}

Return JSON only.
"""

    return prompt


# =============================================================================
# Testing
# =============================================================================

if __name__ == "__main__":

    sample_review = (
        "The fabric is soft, but the size runs smaller than expected."
    )

    print("=" * 70)
    print("ZERO-SHOT PROMPT")
    print("=" * 70)
    print(build_zero_shot_prompt(sample_review))

    print("\n")

    print("=" * 70)
    print("FEW-SHOT PROMPT")
    print("=" * 70)
    print(build_few_shot_prompt(sample_review))

    print("\n")

    print("=" * 70)
    print("ROLE-BASED PROMPT")
    print("=" * 70)
    print(build_role_prompt(sample_review))