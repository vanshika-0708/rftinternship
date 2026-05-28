# STOCK / TIME-SERIES ANALYSIS PROJECT
# Import Libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Create Sample Dataset
data = {
    "Date": pd.date_range(start="2025-01-01", periods=20, freq='D'),
    "Stock_Price": [100, 102, 101, 105, 108, 110, 107, 111, 115, 117,
                    120, 118, 122, 125, 123, 128, 130, 127, 132, 135]
}

df = pd.DataFrame(data)
# Moving Average Calculation
df["Moving_Average"] = df["Stock_Price"].rolling(window=3).mean()
# Identify Peaks & Drops
# Peak = Higher than previous and next value
# Drop = Lower than previous and next value
peaks = []
drops = []
for i in range(1, len(df)-1):
    # Peak Detection
    if df["Stock_Price"][i] > df["Stock_Price"][i-1] and df["Stock_Price"][i] > df["Stock_Price"][i+1]:
        peaks.append(i)
    # Drop Detection
    if df["Stock_Price"][i] < df["Stock_Price"][i-1] and df["Stock_Price"][i] < df["Stock_Price"][i+1]:
        drops.append(i)

# Volatility Detection
volatility = np.std(df["Stock_Price"])

print("Stock Price Volatility:", round(volatility, 2))
# Display Dataset
print("\nFinal Dataset:\n")
print(df)
# Visualization
plt.figure(figsize=(12,6))

# Original Stock Price
plt.plot(df["Date"], df["Stock_Price"],
         label="Stock Price",
         marker='o')

# Moving Average Line
plt.plot(df["Date"], df["Moving_Average"],
         label="Moving Average",
         linestyle='--')

# Peaks
plt.scatter(df["Date"][peaks],
            df["Stock_Price"][peaks],
            color='green',
            s=100,
            label='Peaks')

# Drops
plt.scatter(df["Date"][drops],
            df["Stock_Price"][drops],
            color='red',
            s=100,
            label='Drops')

# Graph Details
plt.title("Stock Price Time-Series Analysis")
plt.xlabel("Date")
plt.ylabel("Stock Price")
plt.legend()
plt.grid(True)
plt.savefig("stock_analysis_graph.png")
# Show Graph
plt.show()