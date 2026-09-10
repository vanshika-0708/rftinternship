import pandas as pd
import matplotlib.pyplot as plt

# Load expense data
df = pd.read_csv("expenses.csv")

# Convert Date column
df["Date"] = pd.to_datetime(df["Date"])

# Function to categorize expenses
def categorize(description):
    description = description.lower()

    if "grocery" in description:
        return "Food"
    elif "restaurant" in description:
        return "Food"
    elif "uber" in description:
        return "Transport"
    elif "electricity" in description:
        return "Bills"
    elif "internet" in description:
        return "Bills"
    elif "shopping" in description:
        return "Shopping"
    elif "movie" in description:
        return "Entertainment"
    elif "medicine" in description:
        return "Healthcare"
    else:
        return "Other"

# Categorize expenses
df["Category"] = df["Description"].apply(categorize)

# Calculate total expenses
total_expense = df["Amount"].sum()

# Set monthly income
monthly_income = 25000

# Calculate savings
savings = monthly_income - total_expense

# Category-wise spending
category_expense = df.groupby("Category")["Amount"].sum()

# Budget summary
print("===== SMART EXPENSE TRACKER =====")
print("Monthly Income: ₹", monthly_income)
print("Total Expense: ₹", total_expense)
print("Monthly Savings: ₹", savings)

if savings > 0:
    print("Status: You are within your budget.")
else:
    print("Status: You exceeded your budget.")

print("\n===== CATEGORY-WISE EXPENSE =====")
print(category_expense)

# Daily spending
daily_expense = df.groupby("Date")["Amount"].sum()

print("\n===== DAILY EXPENSE =====")
print(daily_expense)

# Save final report
df.to_csv("final_expense_report.csv", index=False)

print("\nFinal report exported successfully!")

# -----------------------------
# Visualization 1: Category-wise spending
# -----------------------------

category_expense.plot(kind="bar")

plt.title("Category-wise Expense")
plt.xlabel("Category")
plt.ylabel("Amount (₹)")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

# -----------------------------
# Visualization 2: Spending trend
# -----------------------------

daily_expense.plot(kind="line", marker="o")

plt.title("Daily Spending Trend")
plt.xlabel("Date")
plt.ylabel("Amount (₹)")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

# -----------------------------
# Visualization 3: Expense distribution
# -----------------------------

category_expense.plot(kind="pie", autopct="%1.1f%%")

plt.title("Expense Distribution")
plt.ylabel("")
plt.show()

from sklearn.linear_model import LinearRegression
import numpy as np

# Prepare data
df["Day"] = np.arange(1, len(df) + 1)

X = df[["Day"]]
y = df["Amount"]

# Train model
model = LinearRegression()
model.fit(X, y)

# Predict next day
next_day = [[len(df) + 1]]
prediction = model.predict(next_day)

print("Predicted next day expense: ₹", round(prediction[0], 2))

import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

st.title("💰 Smart Expense Tracker")

df = pd.read_csv("expenses.csv")

st.subheader("Expense Data")
st.dataframe(df)

total = df["Amount"].sum()

st.metric("Total Expense", f"₹{total}")

st.subheader("Expense Summary")

category = df.groupby("Description")["Amount"].sum()

st.bar_chart(category)

st.subheader("Spending Trend")

st.line_chart(df["Amount"])