

import pandas as pd
import matplotlib.pyplot as plt
# Step 1: Dataset

data = {
    "Movie_Name": ["Inception", "Avengers", "Titanic", "Joker", "Interstellar",
                   "Bahubali", "KGF", "Dangal", "Pushpa", "RRR"],

    "Rating":     [8.8, 8.5, 7.9, 8.4, 8.7, 8.2, 8.1, 8.5, 7.8, 8.0],

    "Genre":      ["Sci-Fi", "Action", "Romance", "Thriller", "Sci-Fi",
                   "Action", "Action", "Sports", "Action", "Action"],

    "Revenue":    [829, 1518, 2187, 1074, 677, 650, 250, 300, 350, 1200]
}

# Check array lengths
print("--- Array Lengths ---")
for key, value in data.items():
    print(f"{key} -> {len(value)}")

# Create DataFrame
df = pd.DataFrame(data)

print("\n--- Movie Dataset ---")
print(df)

# Step 2: Highest Rated Movies

print("\n--- Highest Rated Movies ---")
highest = df.sort_values("Rating", ascending=False)
print(highest[["Movie_Name", "Rating"]])

# Step 3: Most Profitable Genres

print("\n--- Most Profitable Genres ---")
genre_profit = df.groupby("Genre")["Revenue"].sum().sort_values(ascending=False)
print(genre_profit)

# Step 4: Top 5 Movies by Revenue
print("\n--- Top 5 Movies by Revenue ---")
top5 = df.sort_values("Revenue", ascending=False).head(5)
print(top5[["Movie_Name", "Revenue"]])

# Step 5: Correlation
corr = df["Rating"].corr(df["Revenue"])
print("\n--- Correlation ---")
print(f"Rating vs Revenue: {round(corr, 4)}")

if abs(corr) > 0.5:
    print("Strong Correlation")
elif abs(corr) > 0.3:
    print("Moderate Correlation")
else:
    print("Weak Correlation")

# Step 6: Plot 1 - Genre vs Revenue
fig, ax = plt.subplots(figsize=(8, 5))
genre_profit.plot(kind="bar", ax=ax, color="skyblue", edgecolor="black")
ax.set_title("Genre vs Revenue")
ax.set_xlabel("Genre")
ax.set_ylabel("Revenue (Million $)")
plt.tight_layout()
plt.show()

# Step 7: Plot 2 - Rating Distribution
plt.figure(figsize=(8, 5))
plt.hist(df["Rating"], bins=5, color="orange", edgecolor="black")
plt.title("Rating Distribution")
plt.xlabel("Rating")
plt.ylabel("Frequency")
plt.tight_layout()
plt.show()

# Step 8: Plot 3 - Scatter (Bonus)
plt.figure(figsize=(8, 5))
plt.scatter(df["Rating"], df["Revenue"], color="green", s=100, edgecolors="black")

for i, row in df.iterrows():
    plt.annotate(row["Movie_Name"],
                 (row["Rating"], row["Revenue"]),
                 textcoords="offset points",
                 xytext=(5, 5), fontsize=8)

plt.title("Rating vs Revenue")
plt.xlabel("Rating")
plt.ylabel("Revenue (Million $)")
plt.tight_layout()
plt.show()
print("\n✅ Project Completed!")
