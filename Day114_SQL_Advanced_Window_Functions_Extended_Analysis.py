import pandas as pd

# Sample dataset
data = {
    "subject": ["Math", "Science", "English", "History"],
    "grade": [95, 92, 88, 85]
}
df = pd.DataFrame(data)

# Ranking functions
df["rank"] = df["grade"].rank(method="min", ascending=False).astype(int)
df["dense_rank"] = df["grade"].rank(method="dense", ascending=False).astype(int)
df["row_num"] = range(1, len(df) + 1)

# Extended analysis
df["cumulative_avg"] = df["grade"].expanding().mean().round(2)
df["percentile"] = df["grade"].rank(pct=True).round(2)

print(df)

import matplotlib.pyplot as plt
import seaborn as sns

# Bar chart for grades
plt.figure(figsize=(8,6))
sns.barplot(x="subject", y="grade", data=df, palette="viridis")
plt.title("Day114 — Exam Grades by Subject")
plt.xlabel("Subject")
plt.ylabel("Grade")

# Add cumulative average line
plt.plot(df["subject"], df["cumulative_avg"], marker="o", color="red", label="Cumulative Avg")

# Add percentile markers
for i, p in enumerate(df["percentile"]):
    plt.text(i, df["grade"][i] + 1, f"{p:.2f}", ha="center", color="blue")

plt.legend()
plt.show()

# Descriptive statistics
print("=== Descriptive Statistics ===")
print(df.describe())

# Grouped averages by rank
print("\n=== Average Grade by Rank ===")
print(df.groupby("rank")["grade"].mean())

# Grouped cumulative averages
print("\n=== Average Cumulative by Rank ===")
print(df.groupby("rank")["cumulative_avg"].mean())

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Dataset
data = {
    "subject": ["Math", "Science", "English", "History"],
    "grade": [95, 92, 88, 85]
}
df = pd.DataFrame(data)

# Ranking + extended analysis
df["rank"] = df["grade"].rank(method="min", ascending=False).astype(int)
df["dense_rank"] = df["grade"].rank(method="dense", ascending=False).astype(int)
df["row_num"] = range(1, len(df) + 1)
df["cumulative_avg"] = df["grade"].expanding().mean().round(2)
df["percentile"] = df["grade"].rank(pct=True).round(2)

# Print raw data
print("=== Extended Dataset ===")
print(df)

# Visualization
plt.figure(figsize=(8,6))
sns.barplot(x="subject", y="grade", data=df, palette="viridis")
plt.title("Day114 — Exam Grades by Subject")
plt.xlabel("Subject")
plt.ylabel("Grade")
plt.plot(df["subject"], df["cumulative_avg"], marker="o", color="red", label="Cumulative Avg")
for i, p in enumerate(df["percentile"]):
    plt.text(i, df["grade"][i] + 1, f"{p:.2f}", ha="center", color="blue")
plt.legend()
plt.show()

# Statistical summary
print("\n=== Descriptive Statistics ===")
print(df.describe())
print("\n=== Average Grade by Rank ===")
print(df.groupby("rank")["grade"].mean())
print("\n=== Average Cumulative by Rank ===")
print(df.groupby("rank")["cumulative_avg"].mean())
