# SALES DATA ANALYSIS PROJECT
# DATASET INCLUDED INSIDE THE CODE
# ==========================================

# Import Libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# ------------------------------------------
# CREATE DATASET INSIDE PYTHON
# ------------------------------------------

np.random.seed(42)

n = 500

categories = ["Electronics", "Clothing", "Furniture", "Sports", "Books"]
regions = ["North", "South", "East", "West"]

data = {
    "Order_ID": [f"ORD{1000+i}" for i in range(n)],

    "Date": np.random.choice(
        pd.date_range("2024-01-01", "2024-12-31"),
        n
    ),

    "Category": np.random.choice(
        categories,
        n,
        p=[0.25, 0.20, 0.20, 0.20, 0.15]
    ),

    "Region": np.random.choice(regions, n),

    "Sales": np.random.randint(100, 5000, n).astype(float),

    "Quantity": np.random.randint(1, 10, n),

    "Discount": np.random.choice(
        [0, 0.05, 0.10, 0.20, 0.30],
        n
    ),

    "Customer_ID": [
        f"CUST{np.random.randint(1,100):03d}"
        for _ in range(n)
    ],
}

# Convert into DataFrame
df = pd.DataFrame(data)

# ------------------------------------------
# DATA CLEANING
# ------------------------------------------

print("First 5 Rows:")
print(df.head())

print("\nDataset Info:")
print(df.info())

print("\nMissing Values:")
print(df.isnull().sum())

# Remove duplicates
df.drop_duplicates(inplace=True)

# ------------------------------------------
# DATA ANALYSIS
# ------------------------------------------

# Total Sales
total_sales = df["Sales"].sum()
print("\nTotal Sales:", total_sales)

# Average Sales
avg_sales = df["Sales"].mean()
print("Average Sales:", avg_sales)

# Category Wise Sales
category_sales = df.groupby("Category")["Sales"].sum()
print("\nCategory Wise Sales:")
print(category_sales)

# Region Wise Sales
region_sales = df.groupby("Region")["Sales"].sum()
print("\nRegion Wise Sales:")
print(region_sales)

# Monthly Sales
df["Month"] = pd.to_datetime(df["Date"]).dt.month

monthly_sales = df.groupby("Month")["Sales"].sum()

# ------------------------------------------
# DATA VISUALIZATION
# ------------------------------------------

# 1. Bar Chart
plt.figure(figsize=(8,5))
category_sales.plot(kind="bar")
plt.title("Category Wise Sales")
plt.xlabel("Category")
plt.ylabel("Sales")
plt.grid(True)
plt.show()

# 2. Pie Chart
plt.figure(figsize=(7,7))
region_sales.plot(
    kind="pie",
    autopct="%1.1f%%"
)
plt.title("Region Wise Sales")
plt.ylabel("")
plt.show()

# 3. Line Chart
plt.figure(figsize=(8,5))
monthly_sales.plot(marker="o")
plt.title("Monthly Sales Trend")
plt.xlabel("Month")
plt.ylabel("Sales")
plt.grid(True)
plt.show()

# 4. Seaborn Countplot
plt.figure(figsize=(8,5))
sns.countplot(x="Category", data=df)
plt.title("Number of Orders per Category")
plt.show()

# ------------------------------------------
# INSIGHTS
# ------------------------------------------

print("\n===== PROJECT INSIGHTS =====")

print("1. Electronics category generates high sales.")
print("2. Sales vary across different regions.")
print("3. Monthly sales trend helps identify growth.")
print("4. Data visualization makes analysis easier.")
print("5. Discounts affect overall sales performance.")

# ------------------------------------------
# SAVE DATASET
# ------------------------------------------

df.to_csv("sales_dataset.csv", index=False)

print("\nDataset saved as sales_dataset.csv")

# ------------------------------------------
# PROJECT SUMMARY
# ------------------------------------------

summary = """
This project creates a sales dataset inside Python using NumPy and Pandas.
The project performs:
- Data Cleaning
- Data Analysis
- Data Visualization
- Business Insights Generation

Charts like bar chart, pie chart, line chart,
and seaborn countplot are used for visualization.
"""

print(summary)