"""
=============================================================
Project : Statistical EDA, Hypothesis Testing & Visualization
Course  : Data Analytics with Gen & Agentic AI
File    : visualizations.py

Description:
Generates four required visualizations for the project and
saves them as PNG files in the images folder.
=============================================================
"""

import os
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# ----------------------------------------------------------
# Create Images Folder
# ----------------------------------------------------------

os.makedirs("images", exist_ok=True)

# ----------------------------------------------------------
# Load Dataset
# ----------------------------------------------------------

print("=" * 70)
print("Loading Processed Dataset...")
print("=" * 70)

df = pd.read_csv("output/processed_dataset.csv")

print("\nDataset Loaded Successfully!")
print(f"Dataset Shape : {df.shape}")

# ----------------------------------------------------------
# Plot Style
# ----------------------------------------------------------

sns.set_style("whitegrid")

# ==========================================================
# Visualization 1 : Correlation Heatmap
# ==========================================================

plt.figure(figsize=(8,6))

corr = df.select_dtypes(include="number").corr()

sns.heatmap(
    corr,
    annot=True,
    cmap="coolwarm",
    fmt=".2f"
)

plt.title("Correlation Heatmap")
plt.xlabel("Variables")
plt.ylabel("Variables")

plt.tight_layout()

plt.savefig(
    "images/correlation_heatmap.png",
    dpi=300,
    bbox_inches="tight"
)

plt.close()

print("✓ Correlation Heatmap Saved")

# ==========================================================
# Visualization 2 : Scatter Plot
# ==========================================================

plt.figure(figsize=(8,6))

sns.scatterplot(
    data=df,
    x="price",
    y="payment_value",
    hue="payment_type",
    alpha=0.7
)

plt.title("Price vs Payment Value")
plt.xlabel("Product Price")
plt.ylabel("Payment Value")

plt.tight_layout()

plt.savefig(
    "images/scatter_plot.png",
    dpi=300
)

plt.close()

print("✓ Scatter Plot Saved")

# ==========================================================
# Visualization 3 : Bar Plot
# ==========================================================

plt.figure(figsize=(8,6))

bar_data = (
    df.groupby("payment_type")["payment_value"]
      .mean()
      .sort_values(ascending=False)
)

sns.barplot(
    x=bar_data.index,
    y=bar_data.values
)

plt.title("Average Payment Value by Payment Type")
plt.xlabel("Payment Type")
plt.ylabel("Average Payment Value")

plt.tight_layout()

plt.savefig(
    "images/bar_plot.png",
    dpi=300
)

plt.close()

print("✓ Bar Plot Saved")

# ==========================================================
# Visualization 4 : Distribution Plot
# ==========================================================

plt.figure(figsize=(8,6))

sns.histplot(
    df["payment_value"].dropna(),
    bins=40,
    kde=True
)

plt.title("Distribution of Payment Value")
plt.xlabel("Payment Value")
plt.ylabel("Frequency")

plt.tight_layout()

plt.savefig(
    "images/distribution_plot.png",
    dpi=300
)

plt.close()

print("✓ Distribution Plot Saved")

# ==========================================================
# Completed
# ==========================================================

print("\n" + "=" * 70)
print("All Visualizations Generated Successfully!")
print("=" * 70)

print("\nSaved Files:")

print("images/correlation_heatmap.png")
print("images/scatter_plot.png")
print("images/bar_plot.png")
print("images/distribution_plot.png")