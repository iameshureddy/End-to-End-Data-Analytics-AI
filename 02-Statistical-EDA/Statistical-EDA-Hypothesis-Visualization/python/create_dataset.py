"""
=============================================================
Project : Statistical EDA, Hypothesis Testing & Visualization
Course  : Data Analytics with Gen & Agentic AI
File    : create_dataset.py

Description:
Reads the original Olist CSV files, merges them into a single
flat dataset, and saves the processed dataset for analysis.
=============================================================
"""

import pandas as pd
from pathlib import Path

# ============================================================
# Project Paths
# ============================================================

BASE_DIR = Path(__file__).resolve().parent.parent

RAW_DATA = BASE_DIR / "data" / "raw"
OUTPUT_DIR = BASE_DIR / "output"

OUTPUT_DIR.mkdir(exist_ok=True)

# ============================================================
# Load CSV Files
# ============================================================

print("Loading datasets...\n")

customers = pd.read_csv(RAW_DATA / "olist_customers_dataset.csv")
orders = pd.read_csv(RAW_DATA / "olist_orders_dataset.csv")
order_items = pd.read_csv(RAW_DATA / "olist_order_items_dataset.csv")
payments = pd.read_csv(RAW_DATA / "olist_order_payments_dataset.csv")
reviews = pd.read_csv(RAW_DATA / "olist_order_reviews_dataset.csv")
products = pd.read_csv(RAW_DATA / "olist_products_dataset.csv")

print("Datasets loaded successfully.\n")

# ============================================================
# Merge Tables
# ============================================================

print("Merging datasets...\n")

df = orders.merge(
    customers,
    on="customer_id",
    how="left"
)

df = df.merge(
    order_items,
    on="order_id",
    how="left"
)

df = df.merge(
    payments,
    on="order_id",
    how="left"
)

df = df.merge(
    reviews,
    on="order_id",
    how="left"
)

df = df.merge(
    products,
    on="product_id",
    how="left"
)

print("Merge completed.\n")

# ============================================================
# Select Required Columns
# ============================================================

df = df[
    [
        "order_id",
        "customer_id",
        "customer_state",
        "product_id",
        "product_category_name",
        "payment_type",
        "payment_value",
        "price",
        "freight_value",
        "review_score",
        "order_purchase_timestamp"
    ]
]

# ============================================================
# Remove Duplicate Records
# ============================================================

duplicates = df.duplicated().sum()

print(f"Duplicate rows found : {duplicates}")

df.drop_duplicates(inplace=True)

print(f"Dataset shape after removing duplicates : {df.shape}\n")

# ============================================================
# Missing Values Summary
# ============================================================

print("Missing Values\n")
print(df.isnull().sum())

# ============================================================
# Save Processed Dataset
# ============================================================

output_file = OUTPUT_DIR / "processed_dataset.csv"

df.to_csv(output_file, index=False)

# ============================================================
# Display Summary
# ============================================================

print("\nProcessed dataset created successfully.")

print(f"\nSaved to : {output_file}")

print("\nDataset Shape")
print(df.shape)

print("\nColumns")
print(df.columns.tolist())

print("\nFirst Five Records")
print(df.head())

print("\nDone.")