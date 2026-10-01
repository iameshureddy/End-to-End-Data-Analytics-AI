"""
=============================================================
Project : Statistical EDA, Hypothesis Testing & Visualization
Course  : Data Analytics with Gen & Agentic AI
File    : statistics.py

Description:
Performs correlation analysis using Pearson correlation,
identifies the highest and lowest correlation pairs,
handles NaN values, and saves the correlation matrix.
=============================================================
"""

import pandas as pd
import numpy as np

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
# Select Numeric Columns
# ==========================================================

numeric_df = df.select_dtypes(include=["number"])

print("\nNumeric Columns Used:")
print(numeric_df.columns.tolist())

# ==========================================================
# Correlation Matrix
# ==========================================================

print("\n" + "=" * 70)
print("TASK 7 : CORRELATION ANALYSIS")
print("=" * 70)

correlation_matrix = numeric_df.corr(method="pearson")

print("\nPearson Correlation Matrix\n")
print(correlation_matrix)

# ==========================================================
# Handle NaN Values
# ==========================================================

correlation_matrix = correlation_matrix.fillna(0)

# ==========================================================
# Remove Self Correlations
# ==========================================================

corr = correlation_matrix.copy()

np.fill_diagonal(corr.values, np.nan)

# ==========================================================
# Highest Absolute Correlation
# ==========================================================

highest_pair = corr.abs().stack().idxmax()
highest_value = corr.loc[highest_pair]

# ==========================================================
# Lowest Correlation
# ==========================================================

lowest_pair = corr.stack().idxmin()
lowest_value = corr.loc[lowest_pair]

# ==========================================================
# Save Correlation Matrix
# ==========================================================

correlation_matrix.to_csv(
    "output/correlation_matrix.csv"
)

# ==========================================================
# Display Results
# ==========================================================

print("\n" + "=" * 70)
print("Correlation Summary")
print("=" * 70)

print(f"\nHighest Correlation Pair")
print(f"{highest_pair[0]}  <-->  {highest_pair[1]}")
print(f"Correlation : {highest_value:.4f}")

print(f"\nLowest Correlation Pair")
print(f"{lowest_pair[0]}  <-->  {lowest_pair[1]}")
print(f"Correlation : {lowest_value:.4f}")

print("\nNaN Handling")
print("NaN correlation values were replaced with 0 before analysis.")

print("\nTie Handling")
print("If multiple pairs had the same correlation value,")
print("the first pair returned by Pandas was reported.")

print("\nCorrelation matrix saved successfully.")
print("File : output/correlation_matrix.csv")

print("\nStatistics Analysis Completed Successfully!")