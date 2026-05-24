import pandas as pd
from io import StringIO

# Given dataset
csv_data = """PRODUCT,QUANTITY,PRICE
A,2,100
B,1,200
A,3,100
C,5,50"""

# Read CSV
df = pd.read_csv(StringIO(csv_data))

print("=" * 40)
print("        SALES DATA ANALYZER")
print("=" * 40)

# BONUS: Add TOTAL column (QUANTITY * PRICE)
df['TOTAL'] = df['QUANTITY'] * df['PRICE']

print("\n Dataset with TOTAL column:")
print(df.to_string(index=False))

# Calculate total sales per product
sales_per_product = df.groupby('PRODUCT')['TOTAL'].sum()

print("\n Total Sales per Product:")
for product, total in sales_per_product.items():
    print(f"  Product {product}: ₹{total}")

# Total Revenue
total_revenue = df['TOTAL'].sum()
print(f"\n Total Revenue: ₹{total_revenue}")

# Top-Selling Product (by revenue)
top_product = sales_per_product.idxmax()
top_revenue = sales_per_product.max()
print(f" Top-Selling Product: {top_product} (₹{top_revenue})")

# BONUS: Sort by Revenue
print("\n Dataset Sorted by Revenue (Descending):")
sorted_df = df.sort_values('TOTAL', ascending=False)
print(sorted_df.to_string(index=False))