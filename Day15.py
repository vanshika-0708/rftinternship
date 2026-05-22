# Day 15 Internship Task

import pandas as pd
import matplotlib.pyplot as plt
# STEP 1: CREATE SAMPLE DATASET
data = {
    "Month": ["Jan", "Feb", "Mar", "Apr", "May", "Jun"],
    "Sales": [120, 150, 170, 160, 210, 250],
    "Profit": [20, 35, 40, 30, 50, 65]
}

df = pd.DataFrame(data)
# STEP 2: CREATE SUBPLOTS
fig, axes = plt.subplots(2, 2, figsize=(12, 8))

# LINE CHART (TREND)

axes[0, 0].plot(df["Month"], df["Sales"], marker='o')
axes[0, 0].set_title("Sales Trend")
axes[0, 0].set_xlabel("Month")
axes[0, 0].set_ylabel("Sales")


# BAR CHART (COMPARISON)

axes[0, 1].bar(df["Month"], df["Profit"])
axes[0, 1].set_title("Profit Comparison")
axes[0, 1].set_xlabel("Month")
axes[0, 1].set_ylabel("Profit")

# HISTOGRAM (DISTRIBUTION)

axes[1, 0].hist(df["Sales"], bins=5)
axes[1, 0].set_title("Sales Distribution")
axes[1, 0].set_xlabel("Sales")
axes[1, 0].set_ylabel("Frequency")

# OUTLIER DETECTION (BONUS)

axes[1, 1].boxplot(df["Sales"])
axes[1, 1].set_title("Outlier Detection - Sales")

# ADJUST LAYOUT

plt.tight_layout()
plt.show()

# INSIGHTS

print("\nINSIGHTS:")
print("1. Sales show an increasing trend over the months.")
print("2. Highest sales were recorded in June.")
print("3. Profit also increased with sales.")
print("4. Histogram shows most sales values are between 150 and 250.")
print("5. Boxplot helps detect possible outliers visually.")