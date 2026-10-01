"""
===============================================================================
TASK 5
Aspect-Based Sentiment Extension Prompt

Objective
---------
Generate structured aspect-based sentiment with actionable phrases.

For every review, identify sentiment for at least two aspects and provide
a short actionable phrase (3–6 words) for each aspect.

Output must be valid JSON only.
===============================================================================
"""


def build_aspect_extension_prompt(review_text):
    """
    Build the prompt for Aspect-Based Sentiment Extension.

    Parameters
    ----------
    review_text : str
        Customer review.

    Returns
    -------
    str
        Complete prompt.
    """

    prompt = f"""
You are a Senior Customer Insights Analyst.

Analyse the customer review below.

Identify sentiment for these aspects if mentioned:

- quality
- size
- comfort
- design
- delivery

For every identified aspect:

1. sentiment
2. action (3–6 words only)

Return ONLY valid JSON.

Schema:

{{
    "quality": {{
        "sentiment": "...",
        "action": "..."
    }},
    "size": {{
        "sentiment": "...",
        "action": "..."
    }},
    "comfort": {{
        "sentiment": "...",
        "action": "..."
    }},
    "design": {{
        "sentiment": "...",
        "action": "..."
    }},
    "delivery": {{
        "sentiment": "...",
        "action": "..."
    }},
    "overall": "positive|neutral|negative"
}}

Customer Review:

{review_text}
"""

    return prompt


if __name__ == "__main__":

    sample = (
        "The dress is beautiful and the fabric is excellent, "
        "but the size runs small."
    )

    print(build_aspect_extension_prompt(sample))