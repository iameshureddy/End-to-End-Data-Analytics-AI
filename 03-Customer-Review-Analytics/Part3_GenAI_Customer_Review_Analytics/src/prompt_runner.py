"""
===============================================================================
TASK 4
Prompt Runner

Objective
---------
Run all three prompt templates on the same five customer reviews and compare
their outputs.

Outputs
-------
- 15 API calls (5 reviews × 3 prompts)
- JSON parsing
- CSV report
===============================================================================
"""

import json
import os
import pandas as pd

from retry_handler import safe_call_llm
from prompt_templates import (
    build_zero_shot_prompt,
    build_few_shot_prompt,
    build_role_prompt
)
from data_loader import load_and_clean_data


OUTPUT_DIR = "output/csv"
os.makedirs(OUTPUT_DIR, exist_ok=True)

OUTPUT_FILE = os.path.join(OUTPUT_DIR, "prompt_comparison.csv")


def run_prompt(review, prompt_name, prompt):

    response = safe_call_llm(
        prompt=prompt,
        temperature=0.3,
        max_tokens=300
    )

    if response is None:
        return {
            "Prompt": prompt_name,
            "Valid JSON": False,
            "Label": "",
            "Confidence": "",
            "Reason": "",
            "Raw Response": ""
        }

    try:

        data = json.loads(response)

        return {
            "Prompt": prompt_name,
            "Valid JSON": True,
            "Label": data.get("label", ""),
            "Confidence": data.get("confidence", ""),
            "Reason": data.get("reason", ""),
            "Raw Response": response
        }

    except Exception:

        return {
            "Prompt": prompt_name,
            "Valid JSON": False,
            "Label": "",
            "Confidence": "",
            "Reason": "",
            "Raw Response": response
        }


if __name__ == "__main__":

    print("=" * 70)
    print("TASK 4 : Prompt Comparison")
    print("=" * 70)

    df = load_and_clean_data()

    reviews = df["Review Text"].head(5)

    results = []

    for idx, review in enumerate(reviews, start=1):

        print(f"\nProcessing Review {idx}/5")

        prompts = [
            ("Zero-shot", build_zero_shot_prompt(review)),
            ("Few-shot", build_few_shot_prompt(review)),
            ("Role-based", build_role_prompt(review))
        ]

        for prompt_name, prompt in prompts:

            print(f"  Running {prompt_name}")

            result = run_prompt(review, prompt_name, prompt)

            result["Review No"] = idx
            result["Review"] = review

            results.append(result)

    output_df = pd.DataFrame(results)

    output_df.to_csv(OUTPUT_FILE, index=False)

    print("\n" + "=" * 70)
    print("TASK 4 COMPLETED")
    print("=" * 70)

    print(f"\nCSV Saved : {OUTPUT_FILE}")

    print("\nJSON Validity Summary")

    print(
        output_df.groupby("Prompt")["Valid JSON"]
        .sum()
    )

    print("\nPreview\n")

    print(output_df.head())