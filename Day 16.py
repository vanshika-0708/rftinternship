import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# 1. CREATE DATASET
np.random.seed(42)
n = 300

products = ['Laptop', 'Phone', 'Tablet', 'Headphones', 'Smartwatch']
regions = ['North', 'South', 'East', 'West']
dates = pd.date_range(start='2024-01-01', end='2024-12-31', periods=n)

df = pd.DataFrame({
    'Date': dates,
    'Product': np.random.choice(products, n),
    'Region': np.random.choice(regions, n),
    'Sales': np.random.randint(500, 15000, n).astype(float)
})

# Add missing values
idx = np.random.choice(df.index, size=25, replace=False)
df.loc[idx, 'Sales'] = np.nan

# 2. DATA CLEANING
print("Missing values:", df['Sales'].isna().sum())
df['Sales'] = df['Sales'].fillna(df['Sales'].median())
print("After cleaning:", df['Sales'].isna().sum())

# 3. AGGREGATION
# Total sales per product
product_sales = df.groupby('Product')['Sales'].sum().sort_values(ascending=False)
print("\nTotal Sales per Product:")
print(product_sales)

# Region wise performance
region_sales = df.groupby('Region')['Sales'].sum().sort_values(ascending=False)
print("\nRegion-wise Sales:")
print(region_sales)

# Monthly sales
df['Month'] = df['Date'].dt.to_period('M')
monthly_sales = df.groupby('Month')['Sales'].sum()

# 4. VISUALIZATION
# Line chart - Sales Trend
plt.figure(figsize=(10, 4))
monthly_sales.plot()
plt.title('Monthly Sales Trend')
plt.xlabel('Month')
plt.ylabel('Sales')
plt.tight_layout()
plt.savefig('sales_trend.png')
plt.show()

# Bar chart - Top Products
plt.figure(figsize=(8, 4))
product_sales.plot(kind='bar', color='skyblue')
plt.title('Total Sales by Product')
plt.xlabel('Product')
plt.ylabel('Sales')
plt.tight_layout()
plt.savefig('top_products.png')
plt.show()

# 5. KEY INSIGHTS
print("\n--- KEY INSIGHTS ---")
print("1. Best selling product:", product_sales.idxmax())
print("2. Best region:", region_sales.idxmax())
print("3. Peak sales month:", monthly_sales.idxmax())
print("4. Total revenue: ₹", round(df['Sales'].sum(), 2))
print("5. Average sale: ₹", round(df['Sales'].mean(), 2))

# BONUS - Monthly Growth
monthly_sales_list = monthly_sales.reset_index()
monthly_sales_list['Growth'] = monthly_sales_list['Sales'].pct_change() * 100
print("\n--- MONTHLY GROWTH ---")
print(monthly_sales_list[['Month', 'Sales', 'Growth']])