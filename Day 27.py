import pandas as pd
import matplotlib.pyplot as plt

# Read CSV
df = pd.read_csv("social_media_data.csv")

# Calculate engagement
df["Engagement"] = df["Likes"] + df["Comments"] + df["Shares"]

# Top hashtags
top_hashtags = df.groupby("Hashtag")["Engagement"].sum().sort_values(ascending=False)

print("\nTop Trending Hashtags:")
print(top_hashtags)

# Most active users
active_users = df["User"].value_counts()

print("\nMost Active Users:")
print(active_users)

# Most popular posting time
popular_time = df["Post_Time"].value_counts().idxmax()

print("\nMost Popular Posting Time:", popular_time)

# Daily engagement
daily_engagement = df.groupby("Date")["Engagement"].sum()

print("\nDaily Engagement:")
print(daily_engagement)

# Category distribution
category = df["Category"].value_counts()

print("\nContent Category Distribution:")
print(category)

# Charts

# Top Hashtags Chart
top_hashtags.plot(kind="bar")
plt.title("Top Trending Hashtags")
plt.xlabel("Hashtag")
plt.ylabel("Engagement")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

# Daily Engagement Trend
daily_engagement.plot(kind="line", marker="o")
plt.title("Daily Engagement Trend")
plt.xlabel("Date")
plt.ylabel("Engagement")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

# Content Category Distribution
category.plot(kind="pie", autopct="%1.1f%%")
plt.title("Content Category Distribution")
plt.ylabel("")
plt.show()

# Export Report

report = df[[
    "Date", "User", "Hashtag", "Likes",
    "Comments", "Shares", "Engagement",
    "Category", "Post_Time"
]]

report.to_csv("social_media_analytics_report.csv", index=False)

print("\nAnalytics report exported successfully!")

from textblob import TextBlob

def sentiment(text):
    score = TextBlob(str(text)).sentiment.polarity

    if score > 0:
        return "Positive"
    elif score < 0:
        return "Negative"
    else:
        return "Neutral"

df["Sentiment"] = df["Text"].apply(sentiment)

print("\nSentiment Analysis:")
print(df["Sentiment"].value_counts())

df.to_csv("social_media_analytics_report.csv", index=False)