"""
===============================================================================
TASK 1 (Project Foundation)
-------------------------------------------------------------------------------
Module: data_loader.py

Objective
---------
Before building Prompt Engineering and LLM functionality, we first need a clean
customer review dataset.

Large Language Models (LLMs) perform better when the input data is clean,
consistent, and free from missing or duplicate records.

This module prepares the dataset that will be used throughout the remaining
tasks of Part 3.

Why is this module required?
----------------------------
The original dataset contains thousands of customer reviews. Some records may
contain missing review text or duplicate reviews.

Since our project analyses review text using Google Gemini, these unnecessary
records should be removed before making API calls.

This improves:
• Data quality
• Prompt consistency
• API efficiency
• Reliability of evaluation

Project Flow
------------
Raw CSV Dataset
        │
        ▼
Load Dataset
        │
        ▼
Remove Missing Reviews
        │
        ▼
Remove Duplicate Reviews
        │
        ▼
Save Clean Dataset
        │
        ▼
Used by:
    • Task 1 - Prompt Engineering
    • Task 2 - Gemini API Wrapper
    • Task 3 - Retry Logic
    • Task 4 - Prompt Comparison
    • Task 5 - Aspect-Based Sentiment
    • Task 6 - Response Generation
    • Task 7 - Multi-turn Conversation

===============================================================================
"""

# ============================================================================
# Import Required Libraries
# ============================================================================

# Pandas is used for reading and manipulating tabular datasets.
import pandas as pd

# Import centralized file paths.
# Keeping paths in one file avoids hardcoding file locations.
from config import RAW_DATA, CLEAN_DATA


# ============================================================================
# Function : load_and_clean_data()
# ============================================================================

def load_and_clean_data():
    """
    Load the original customer review dataset and perform basic preprocessing.

    Processing Steps
    ----------------
    1. Load the dataset.
    2. Display dataset information.
    3. Remove records with missing review text.
    4. Remove duplicate reviews.
    5. Save the cleaned dataset.
    6. Return the cleaned DataFrame.

    Returns
    -------
    pandas.DataFrame
        Clean customer review dataset.
    """

    print("=" * 70)
    print("Loading Customer Review Dataset")
    print("=" * 70)

    # Read the original CSV dataset.
    # The DataFrame stores the complete dataset in memory.
    df = pd.read_csv(RAW_DATA)

    print(f"\nOriginal Dataset Shape : {df.shape}")

    # Display all available columns.
    print("\nAvailable Columns")
    print(df.columns.tolist())

    # Remove rows where customer review text is missing.
    # Reviews without text cannot be analysed by the LLM.
    df = df.dropna(subset=["Review Text"])

    # Remove duplicate review text.
    # Duplicate reviews unnecessarily increase API usage.
    df = df.drop_duplicates(subset=["Review Text"])

    print(f"\nCleaned Dataset Shape : {df.shape}")

    # Save the cleaned dataset.
    # Every remaining module will use this file instead of repeating cleaning.
    df.to_csv(CLEAN_DATA, index=False)

    print("\nClean dataset saved successfully.")
    print(f"\nLocation : {CLEAN_DATA}")

    return df


# ============================================================================
# Main Execution
# ============================================================================

# Execute this file only when it is run directly.
# It will not execute when imported into another module.
if __name__ == "__main__":
    load_and_clean_data()