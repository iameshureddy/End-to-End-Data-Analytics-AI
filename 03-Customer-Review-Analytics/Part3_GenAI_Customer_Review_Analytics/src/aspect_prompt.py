"""
TASK 5
Aspect-Based Sentiment Analysis with Actionable Insights

Objective
---------
This module creates a prompt for Aspect-Based Sentiment Analysis (ABSA).

Instead of predicting only one overall sentiment, the LLM identifies
relevant aspects mentioned in the customer review and determines:

1. Sentiment for each aspect
2. A short actionable phrase for each aspect
3. Overall sentiment

The prompt extends the selected Role-based prompt from Task 4.

The LLM must return ONLY valid JSON.
"""


# =============================================================================
# Aspect-Based Sentiment Prompt
# =============================================================================

def build_aspect_prompt(review_text):
    """
    Create an Aspect-Based Sentiment Analysis prompt.

    The prompt identifies at least two relevant aspects from the review
    when the review contains sufficient information. Each identified
    aspect must contain both sentiment and an actionable phrase.

    Parameters
    ----------
    review_text : str
        Customer review.

    Returns
    -------
    str
        Complete ABSA prompt.
    """

    prompt = f"""
You are a Senior Customer Insights Analyst specializing in women's
clothing customer feedback.

Instruction:
Analyze the customer review using aspect-based sentiment analysis.

Context:
The review is customer feedback about a women's clothing product.
Identify the specific product aspects discussed by the customer.

Possible aspects include:
- quality
- size/fit
- comfort
- design/style
- delivery

Constraints:
- Identify at least TWO distinct aspects when the review contains
  enough information to support them.
- Carefully extract multiple distinct aspects from the customer's
  wording, even when they are expressed in the same sentence.
- For example, a review mentioning "fun, flirty, and fabulous"
  may support separate design/style and appearance-related aspects.
- Do not invent an aspect or sentiment that is not supported by
  the review.
- If the review discusses product appearance, fit, comfort, quality,
  size, style, or customer experience, use the relevant supported
  aspects.
- For EVERY identified aspect, provide:
  1. The aspect name.
  2. Its sentiment: positive, neutral, or negative.
  3. A short actionable phrase of 3-6 words.
- The actionable phrase must be specific to that aspect.
- The action should be useful for a product, design, sizing,
  quality, or customer-experience improvement.
- Determine the overall sentiment separately.
- Use only information supported by the review.
- Return ONLY valid JSON.
- Do not include markdown.
- Do not include explanations outside the JSON object.

Required JSON format:

{{
  "aspects": [
    {{
      "aspect": "quality",
      "sentiment": "positive|neutral|negative",
      "action": "3-6 word actionable phrase"
    }},
    {{
      "aspect": "size",
      "sentiment": "positive|neutral|negative",
      "action": "3-6 word actionable phrase"
    }}
  ],
  "overall_sentiment": "positive|neutral|negative"
}}

Important:
- Include at least TWO aspects when the review provides sufficient
  evidence.
- Every aspect in the "aspects" array MUST contain both "sentiment"
  and "action".
- Do not add aspects that are not supported by the review.
- Keep each action concise and actionable.

Customer Review:
{review_text}

Return JSON only.
"""

    return prompt


# =============================================================================
# Testing
# =============================================================================

if __name__ == "__main__":

    sample = (
        "The fabric feels amazing and the dress looks beautiful, "
        "but the size is too small."
    )

    print("=" * 70)
    print("TASK 5 - ASPECT-BASED SENTIMENT PROMPT")
    print("=" * 70)

    print(build_aspect_prompt(sample))