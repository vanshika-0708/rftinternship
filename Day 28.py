import pandas as pd
import matplotlib.pyplot as plt

# Read CSV file
df = pd.read_csv("stock_data.csv")

# Convert Date column
df["Date"] = pd.to_datetime(df["Date"])

# Calculate investment
df["Investment"] = df["Buy_Price"] * df["Quantity"]

# Calculate current value
df["Current_Value"] = df["Current_Price"] * df["Quantity"]

# Calculate Profit/Loss
df["Profit_Loss"] = df["Current_Value"] - df["Investment"]

# Calculate return percentage
df["Return_%"] = (df["Profit_Loss"] / df["Investment"]) * 100

# Display stock data
print("\n===== STOCK PORTFOLIO =====")
print(df)

# Best performing stock
best_stock = df.loc[df["Return_%"].idxmax()]
print("\nBest Performing Stock:")
print(best_stock["Stock"], "-", round(best_stock["Return_%"], 2), "%")

# Worst performing stock
worst_stock = df.loc[df["Return_%"].idxmin()]
print("\nWorst Performing Stock:")
print(worst_stock["Stock"], "-", round(worst_stock["Return_%"], 2), "%")

# Overall portfolio return
total_investment = df["Investment"].sum()
total_current_value = df["Current_Value"].sum()

overall_profit = total_current_value - total_investment
overall_return = (overall_profit / total_investment) * 100

print("\n===== PORTFOLIO SUMMARY =====")
print("Total Investment:", total_investment)
print("Current Value:", total_current_value)
print("Overall Profit/Loss:", overall_profit)
print("Overall Return:", round(overall_return, 2), "%")

# 1. Portfolio Growth Chart

daily_value = df.groupby("Date")["Current_Value"].sum()

plt.figure(figsize=(8, 5))
plt.plot(daily_value.index, daily_value.values, marker="o")
plt.title("Portfolio Growth")
plt.xlabel("Date")
plt.ylabel("Portfolio Value")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

# 2. Sector-wise Investment Chart

sector_investment = df.groupby("Sector")["Investment"].sum()

plt.figure(figsize=(7, 5))
sector_investment.plot(kind="bar")
plt.title("Sector-wise Investment")
plt.xlabel("Sector")
plt.ylabel("Investment")
plt.xticks(rotation=0)
plt.tight_layout()
plt.show()

# 3. Daily Return Analysis

daily_return = df.groupby("Date")["Return_%"].mean()

plt.figure(figsize=(8, 5))
plt.plot(daily_return.index, daily_return.values, marker="o")
plt.title("Daily Return Analysis")
plt.xlabel("Date")
plt.ylabel("Average Return (%)")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

# Bonus: Moving Average

daily_price = df.groupby("Date")["Current_Price"].mean()

moving_average = daily_price.rolling(window=2).mean()

print("\n===== MOVING AVERAGE =====")
print(moving_average)

if daily_price.iloc[-1] > moving_average.iloc[-1]:
    print("\nPredicted Next Day Trend: UP 📈")
else:
    print("\nPredicted Next Day Trend: DOWN 📉")