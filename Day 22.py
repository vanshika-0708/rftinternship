import pandas as pd
import matplotlib.pyplot as plt
# load dataset
df=pd.read_csv('sales_dataset.csv')
print(df.columns.tolist())
# clean data
df=df.drop_duplicates()
df=df.dropna() # remove rows with missing values
 # ---------- 3. BASIC CALCULATIONS ----------
total_sales = df["Sales"].sum()
average_revenue = df["Sales"].mean()

print("Total Sales:", total_sales)
print("Average Revenue:", average_revenue)

# Top 5 customers by Sales
top_customers = df.groupby("Customer_ID")["Sales"].sum().sort_values(ascending=False).head(5)
print("\nTop 5 Customers:\n", top_customers)

# CHARTS
# Line Chart - Sales Trend over time
df["Date"] = pd.to_datetime(df["Date"])
sales_by_date = df.groupby("Date")["Sales"].sum()
plt.plot(sales_by_date.index, sales_by_date.values)
plt.title("Sales Trend")
plt.xlabel("Date")
plt.ylabel("Sales")
plt.show()

# Bar Chart - Top 5 Categories (no "product" column, so using Category)
top_categories = df.groupby("Category")["Sales"].sum().sort_values(ascending=False).head(5)
plt.bar(top_categories.index, top_categories.values)
plt.title("Top 5 Categories")
plt.xlabel("Category")
plt.ylabel("Sales")
plt.show()

# Pie Chart - Region Distribution
region_sales = df.groupby("Region")["Sales"].sum()
plt.pie(region_sales.values, labels=region_sales.index, autopct="%1.1f%%")
plt.title("Sales Distribution by Region")
plt.show()

# BUSINESS INSIGHTS 
print("\nBusiness Insights:")
print("1. Total sales is", total_sales)
print("2. Average sales per order is", average_revenue)
print("3. Top customer ID is", top_customers.index[0])
print("4. Best-selling category is", top_categories.index[0])
print("5. Leading region is", region_sales.idxmax())