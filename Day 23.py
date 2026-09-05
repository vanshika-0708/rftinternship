
# DAY 23 - WEATHER DATA ANALYTICS SYSTEM
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# STEP 1: Load Dataset
# If your file is named weather.csv
df = pd.read_csv("weather.csv")

print("First 5 rows:")
print(df.head())

print("\nDataset Information:")
print(df.info())

print("\nMissing Values:")
print(df.isnull().sum())

# STEP 2: Data Preprocessing
# Convert Date column to datetime
df["Date"] = pd.to_datetime(df["Date"])

# Remove rows with missing important values
df = df.dropna(subset=["City", "Temperature", "Weather"])

print("\nCleaned Dataset:")
print(df.head())

# STEP 3: Average Temperature for Each City

average_temperature = (
    df.groupby("City")["Temperature"]
    .mean()
    .sort_values(ascending=False)
)

print("\nAverage Temperature of Each City:")
print(average_temperature)


# --------------------------------------------
# STEP 4: Hottest and Coldest Cities
# --------------------------------------------

hottest_city = average_temperature.idxmax()
hottest_temperature = average_temperature.max()

coldest_city = average_temperature.idxmin()
coldest_temperature = average_temperature.min()

print("\nHottest City:")
print(hottest_city, "-", round(hottest_temperature, 2), "°C")

print("\nColdest City:")
print(coldest_city, "-", round(coldest_temperature, 2), "°C")


# --------------------------------------------
# STEP 5: Rainy and Sunny Days
# --------------------------------------------

rainy_days = (df["Weather"].str.lower() == "rainy").sum()
sunny_days = (df["Weather"].str.lower() == "sunny").sum()

print("\nRainy Days:", rainy_days)
print("Sunny Days:", sunny_days)

# STEP 6: Weather Distribution


weather_distribution = df["Weather"].value_counts()

print("\nWeather Distribution:")
print(weather_distribution)

# STEP 7: Temperature Trend
daily_temperature = (
    df.groupby("Date")["Temperature"]
    .mean()
    .reset_index()
)

plt.figure(figsize=(10, 5))

plt.plot(
    daily_temperature["Date"],
    daily_temperature["Temperature"],
    marker="o"
)

plt.title("Temperature Trend")
plt.xlabel("Date")
plt.ylabel("Average Temperature (°C)")
plt.xticks(rotation=45)
plt.grid(True)
plt.tight_layout()
plt.show()
# STEP 8: Weather Distribution Visualization
plt.figure(figsize=(7, 5))

weather_distribution.plot(
    kind="bar"
)

plt.title("Weather Distribution")
plt.xlabel("Weather Condition")
plt.ylabel("Number of Days")
plt.xticks(rotation=0)
plt.tight_layout()
plt.show()

# STEP 9: Average Temperature Per City
plt.figure(figsize=(9, 5))

average_temperature.plot(
    kind="bar"
)

plt.title("Average Temperature per City")
plt.xlabel("City")
plt.ylabel("Average Temperature (°C)")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

# STEP 10: Bonus - Tomorrow Temperature
# Calculate moving average using last 3 days
daily_temperature["Moving_Average"] = (
    daily_temperature["Temperature"]
    .rolling(window=3)
    .mean()
)

print("\nDaily Temperature with Moving Average:")
print(daily_temperature)

# Prediction for tomorrow
tomorrow_temperature = daily_temperature["Temperature"].tail(3).mean()

print(
    "\nPredicted Temperature for Tomorrow:",
    round(tomorrow_temperature, 2),
    "°C"
)

# STEP 11: Create Final Report
report = pd.DataFrame({
    "Metric": [
        "Hottest City",
        "Hottest Temperature",
        "Coldest City",
        "Coldest Temperature",
        "Rainy Days",
        "Sunny Days",
        "Predicted Tomorrow Temperature"
    ],

    "Value": [
        hottest_city,
        round(hottest_temperature, 2),
        coldest_city,
        round(coldest_temperature, 2),
        rainy_days,
        sunny_days,
        round(tomorrow_temperature, 2)
    ]
})

print("\n========== FINAL WEATHER REPORT ==========")
print(report)

# STEP 12: Export Report

report.to_csv(
    "weather_final_report.csv",
    index=False
)

average_temperature.to_csv(
    "average_temperature_by_city.csv"
)

daily_temperature.to_csv(
    "temperature_trend_report.csv",
    index=False
)

print("\nReports exported successfully!")