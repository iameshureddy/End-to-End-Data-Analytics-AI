"""
TASK 5
Aspect-Based Sentiment Analysis

Objective
---------
Perform Aspect-Based Sentiment Analysis on 10 customer reviews using Gemini.

For each review:
- Identify at least two relevant aspects.
- Determine sentiment for each aspect.
- Generate an actionable phrase for each aspect.
- Determine the overall sentiment.
"""

import os
import pandas as pd

from data_loader import load_and_clean_data
from retry_handler import safe_call_llm
from json_parser import parse_json_response
from aspect_prompt import build_aspect_prompt


# =============================================================================
# Output Configuration
# =============================================================================

OUTPUT_DIR = "output/csv"

os.makedirs(
    OUTPUT_DIR,
    exist_ok=True
)

OUTPUT_FILE = os.path.join(
    OUTPUT_DIR,
    "aspect_sentiment_results.csv"
)


# =============================================================================
# Validate Structured Output
# =============================================================================

def validate_aspect_result(result):
    """
    Validate Gemini's Task 5 structured JSON.
    """

    if not isinstance(result, dict):
        return False

    aspects = result.get("aspects")

    if not isinstance(aspects, list):
        return False

    # At least two aspects are required
    if len(aspects) < 2:
        return False

    valid_sentiments = {
        "positive",
        "neutral",
        "negative"
    }

    for item in aspects:

        if not isinstance(item, dict):
            return False

        aspect = str(
            item.get("aspect", "")
        ).strip()

        sentiment = str(
            item.get("sentiment", "")
        ).lower().strip()

        action = str(
            item.get("action", "")
        ).strip()

        if not aspect:
            return False

        if sentiment not in valid_sentiments:
            return False

        if not action:
            return False

    overall = str(
        result.get("overall_sentiment", "")
    ).lower().strip()

    if overall not in valid_sentiments:
        return False

    return True


# =============================================================================
# Flatten JSON into CSV rows
# =============================================================================

def flatten_aspect_result(review_no, review, parsed):
    """
    Convert nested aspect JSON into one CSV row per aspect.
    """

    rows = []

    aspects = parsed.get("aspects", [])

    overall_sentiment = parsed.get(
        "overall_sentiment",
        ""
    )

    for item in aspects:

        rows.append({
            "Review No": review_no,
            "Review": review,
            "Aspect": item.get("aspect", ""),
            "Sentiment": item.get("sentiment", ""),
            "Action": item.get("action", ""),
            "Overall Sentiment": overall_sentiment,
            "Status": "Success"
        })

    return rows


# =============================================================================
# Main
# =============================================================================

if __name__ == "__main__":

    print("=" * 70)
    print("TASK 5 : Aspect-Based Sentiment Analysis")
    print("=" * 70)

    # -------------------------------------------------------------------------
    # Load cleaned data
    # -------------------------------------------------------------------------

    df = load_and_clean_data()

    reviews = df["Review Text"].head(10)

    results = []

    # -------------------------------------------------------------------------
    # Process 10 reviews
    # -------------------------------------------------------------------------

    for i, review in enumerate(reviews, start=1):

        print(f"\nProcessing Review {i}/10")

        # =====================================================================
        # First attempt
        # =====================================================================

        prompt = build_aspect_prompt(review)

        response = safe_call_llm(
            prompt=prompt,
            temperature=0.3,
            max_tokens=400
        )

        parsed = None

        if response is not None:
            parsed = parse_json_response(response)

        # =====================================================================
        # Retry if structured output is invalid
        # =====================================================================

        if not validate_aspect_result(parsed):

            print(f"Invalid output. Retrying Review {i}")

            retry_prompt = f"""
The previous response did not follow the required JSON structure.

Analyze the customer review again.

You MUST identify at least TWO distinct aspects that are supported
by the review.

For EVERY aspect provide:

- aspect
- sentiment
- action

Sentiment must be exactly one of:

positive
neutral
negative

The action must be a short actionable phrase of 3-6 words.

Return ONLY valid JSON.

Required format:

{{
  "aspects": [
    {{
      "aspect": "size/fit",
      "sentiment": "negative",
      "action": "Improve sizing accuracy"
    }},
    {{
      "aspect": "design/style",
      "sentiment": "positive",
      "action": "Maintain current design"
    }}
  ],
  "overall_sentiment": "positive|neutral|negative"
}}

Customer Review:

{review}

Return JSON only.
"""

            retry_response = safe_call_llm(
                prompt=retry_prompt,
                temperature=0.2,
                max_tokens=400
            )

            if retry_response is not None:
                retry_parsed = parse_json_response(
                    retry_response
                )

                if validate_aspect_result(retry_parsed):
                    parsed = retry_parsed

        # =====================================================================
        # If still invalid
        # =====================================================================

        if not validate_aspect_result(parsed):

            print(
                f"Review {i} failed structured-output validation."
            )

            results.append({
                "Review No": i,
                "Review": review,
                "Aspect": "",
                "Sentiment": "",
                "Action": "",
                "Overall Sentiment": "",
                "Status": "Invalid Structured Output"
            })

            continue

        # =====================================================================
        # Convert valid JSON to rows
        # =====================================================================

        aspect_rows = flatten_aspect_result(
            review_no=i,
            review=review,
            parsed=parsed
        )

        results.extend(aspect_rows)

    # =========================================================================
    # Create DataFrame
    # =========================================================================

    output_df = pd.DataFrame(
        results,
        columns=[
            "Review No",
            "Review",
            "Aspect",
            "Sentiment",
            "Action",
            "Overall Sentiment",
            "Status"
        ]
    )

    # =========================================================================
    # Save CSV
    # =========================================================================

    output_df.to_csv(
        OUTPUT_FILE,
        index=False
    )

    print("\n" + "=" * 70)
    print("TASK 5 COMPLETED")
    print("=" * 70)

    print(f"\nCSV Saved : {OUTPUT_FILE}")

    # =========================================================================
    # Preview
    # =========================================================================

    print("\nPreview:\n")

    print(
        output_df[
            [
                "Review No",
                "Aspect",
                "Sentiment",
                "Action",
                "Overall Sentiment",
                "Status"
            ]
        ].head(15)
    )

    # =========================================================================
    # Summary
    # =========================================================================

    successful_reviews = (
        output_df[
            output_df["Status"] == "Success"
        ]["Review No"]
        .nunique()
    )

    total_aspects = len(
        output_df[
            output_df["Status"] == "Success"
        ]
    )

    failed_reviews = 10 - successful_reviews

    print("\n" + "=" * 70)
    print("TASK 5 SUMMARY")
    print("=" * 70)

    print(f"Reviews processed  : 10")
    print(f"Successful reviews : {successful_reviews}")
    print(f"Failed reviews     : {failed_reviews}")
    print(f"Aspect records     : {total_aspects}")