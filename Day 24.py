import pandas as pd
import matplotlib.pyplot as plt

# Read CSV file
df = pd.read_csv("transactions.csv")

print("First 5 Transactions:")
print(df.head())

# 1. Detect Duplicate Transactions
duplicates = df[df.duplicated()]

print("\nDuplicate Transactions:")
print(duplicates)

# 2. Identify High-Value Transactions
threshold = 50000
high_value = df[df["Amount"] > threshold]
print("\nHigh Value Transactions:")
print(high_value)

# 3. Find Suspicious Accounts
account_count = df["Account"].value_counts()
suspicious_accounts = account_count[account_count > 3].index
suspicious = df[df["Account"].isin(suspicious_accounts)]
print("\nSuspicious Accounts:")
print(suspicious)

# 4. Transaction Category Chart

df["Category"].value_counts().plot(kind="bar")
plt.title("Transaction Category")
plt.xlabel("Category")
plt.ylabel("Number of Transactions")
plt.show()

# 5. Daily Transaction Trend

df["Date"] = pd.to_datetime(df["Date"])
daily = df.groupby("Date")["Amount"].sum()
daily.plot(kind="line", marker="o")
plt.title("Daily Transaction Trend")
plt.xlabel("Date")
plt.ylabel("Total Amount")
plt.xticks(rotation=45)
plt.show()

# 6. Top 10 Highest Transactions
top10 = df.nlargest(10, "Amount")

print("\nTop 10 Highest Transactions:")
print(top10)

top10.plot(
    x="Account",
    y="Amount",
    kind="bar"
)
plt.title("Top 10 Highest Transactions")
plt.xlabel("Account")
plt.ylabel("Amount")
plt.show()

# 7. Risk Score

df["Risk Score"] = 0
# High amount = higher risk
df.loc[df["Amount"] > 50000, "Risk Score"] += 40
# Duplicate transactions = higher risk
df.loc[df.duplicated(), "Risk Score"] += 30
# Frequent accounts = higher risk
df.loc[df["Account"].isin(suspicious_accounts), "Risk Score"] += 30

print("\nTransactions with Risk Score:")
print(df)

# 8. Export Suspicious Transactions
suspicious_transactions = df[df["Risk Score"] >= 40]
suspicious_transactions.to_csv(
    "suspicious_transactions.csv",
    index=False
)
print("\nSuspicious transactions exported successfully!")