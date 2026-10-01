"""
=============================================================
Project : Statistical EDA, Hypothesis Testing & Visualization
Course  : Data Analytics with Gen & Agentic AI
File    : eda_analysis.py

Description:
Performs Exploratory Data Analysis (EDA), NumPy operations,
feature engineering, grouped analysis, and bucket segmentation.
=============================================================
"""

import numpy as np
import pandas as pd

# ==========================================================
# Load Processed Dataset
# ==========================================================

print("=" * 70)
print("Loading Processed Dataset...")
print("=" * 70)

df = pd.read_csv("output/processed_dataset.csv")

# Convert date column to datetime
df["order_purchase_timestamp"] = pd.to_datetime(
    df["order_purchase_timestamp"]
)

print("\nDataset Loaded Successfully!")

print(f"\nDataset Shape : {df.shape}")
# ==========================================================
# Task 1 : Initial Inspection
# ==========================================================

print("=" * 70)
print("TASK 1 : DATASET INFORMATION")
print("=" * 70)

print("\nDataFrame Info\n")
print(df.info())

print("\nDataFrame Description\n")
print(df.describe(include="all"))

# ==========================================================
# Task 2 : NumPy Fundamentals
# ==========================================================

print("\n" + "=" * 70)
print("TASK 2 : NUMPY FUNDAMENTALS")
print("=" * 70)

payment_array = df["payment_value"].to_numpy()

print("\nFirst 10 Payment Values")
print(payment_array[:10])

# Vectorized Arithmetic (10% Increase)

updated_payment = payment_array * 1.10

print("\nPayment Values After 10% Increase")
print(updated_payment[:10])

# Boolean Filtering

filtered_values = payment_array[
    (payment_array > 100) &
    (payment_array < 500)
]

print("\nPayments Between 100 and 500")
print(filtered_values[:20])

# ==========================================================
# Task 3 : Descriptive Statistics using NumPy
# ==========================================================

print("\n" + "=" * 70)
print("TASK 3 : DESCRIPTIVE STATISTICS")
print("=" * 70)

numeric_columns = ["payment_value", "freight_value"]

for column in numeric_columns:

    values = df[column].dropna().to_numpy()

    print(f"\nStatistics for {column}")

    print(f"Mean            : {np.mean(values):.2f}")
    print(f"Median          : {np.median(values):.2f}")
    print(f"Variance        : {np.var(values):.2f}")
    print(f"Std Deviation   : {np.std(values):.2f}")
    print(f"90th Percentile : {np.percentile(values,90):.2f}")

# ==========================================================
# Task 4 : Feature Engineering
# ==========================================================

print("\n" + "=" * 70)
print("TASK 4 : FEATURE ENGINEERING")
print("=" * 70)

df["total_order_value"] = (
    df["price"] +
    df["freight_value"]
)

print("\nNew Feature Created Successfully!")

print(df[
    [
        "price",
        "freight_value",
        "total_order_value"
    ]
].head())

# ==========================================================
# Task 5 : Pivot Tables
# ==========================================================

print("\n" + "=" * 70)
print("TASK 5 : GROUPED ANALYSIS")
print("=" * 70)

print("\nPivot Table 1")
print("-" * 70)

pivot1 = df.pivot_table(
    index="payment_type",
    values="payment_value",
    aggfunc="mean"
)

print(pivot1)

print("\nPivot Table 2")
print("-" * 70)

pivot2 = df.pivot_table(
    index="customer_state",
    values="total_order_value",
    aggfunc="mean"
)

print(pivot2)

print("\nMulti Aggregation GroupBy")
print("-" * 70)

grouped = df.groupby("payment_type").agg({

    "payment_value": ["mean", "max"],

    "freight_value": ["mean", "sum"]

})

print(grouped)

# ==========================================================
# Task 6 : Bucket Segmentation
# ==========================================================

print("\n" + "=" * 70)
print("TASK 6 : BUCKET SEGMENTATION")
print("=" * 70)


def order_bucket(value):

    if value < 100:
        return "Low"

    elif value < 300:
        return "Medium"

    else:
        return "High"


df["order_category"] = df["total_order_value"].apply(order_bucket)

print("\nBucket Distribution\n")

print(df["order_category"].value_counts())

print("\nDataset Preview")

print(df.head())

# ==========================================================
# Save Updated Dataset
# ==========================================================

df.to_csv(
    "output/processed_dataset.csv",
    index=False
)

print("\nUpdated dataset saved successfully.")

print("\nEDA Completed Successfully!")