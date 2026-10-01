"""
=============================================================
Project : Statistical EDA, Hypothesis Testing & Visualization
Course  : Data Analytics with Gen & Agentic AI
File    : hypothesis_testing.py

Description:
Performs hypothesis testing using an independent two-sample
t-test to compare payment values between Credit Card and
Boleto payment methods.
=============================================================
"""

import pandas as pd
from scipy.stats import ttest_ind

# ==========================================================
# Load Dataset
# ==========================================================

print("=" * 70)
print("Loading Processed Dataset...")
print("=" * 70)

df = pd.read_csv("output/processed_dataset.csv")

print("\nDataset Loaded Successfully!")
print(f"Dataset Shape : {df.shape}")

# ==========================================================
# Task 8 : Business Hypothesis
# ==========================================================

print("\n" + "=" * 70)
print("TASK 8 : HYPOTHESIS")
print("=" * 70)

print("\nBusiness Claim:")
print("The average payment value differs between Credit Card and Boleto transactions.")

print("\nNull Hypothesis (H0):")
print("There is no significant difference in the average payment value")
print("between Credit Card and Boleto payment methods.")

print("\nAlternative Hypothesis (H1):")
print("There is a significant difference in the average payment value")
print("between Credit Card and Boleto payment methods.")

alpha = 0.05

print(f"\nSignificance Level (α): {alpha}")

# ==========================================================
# Prepare Samples
# ==========================================================

credit_card = df[
    df["payment_type"] == "credit_card"
]["payment_value"].dropna()

boleto = df[
    df["payment_type"] == "boleto"
]["payment_value"].dropna()

print("\nSample Size")
print(f"Credit Card : {len(credit_card)}")
print(f"Boleto      : {len(boleto)}")

# ==========================================================
# Task 9 : Two-Sample T-Test
# ==========================================================

print("\n" + "=" * 70)
print("TASK 9 : TWO-SAMPLE T-TEST")
print("=" * 70)

t_statistic, p_value = ttest_ind(
    credit_card,
    boleto,
    equal_var=False
)

print(f"\nT-Statistic : {t_statistic:.4f}")
print(f"P-Value     : {p_value:.6f}")

# ==========================================================
# Decision
# ==========================================================

print("\nDecision")

if p_value < alpha:
    print("Reject the Null Hypothesis (H0).")
    print("There is a statistically significant difference")
    print("between Credit Card and Boleto payment values.")
else:
    print("Fail to Reject the Null Hypothesis (H0).")
    print("There is no statistically significant difference")
    print("between Credit Card and Boleto payment values.")

# ==========================================================
# Assumptions
# ==========================================================

print("\nAssumptions Checked")

print("1. Observations are assumed to be independent.")
print("2. Payment values are approximately suitable")
print("   for comparison due to the large sample size.")
print("3. Welch's t-test (equal_var=False) was used,")
print("   so equal variances were not assumed.")

print("\nHypothesis Testing Completed Successfully!")