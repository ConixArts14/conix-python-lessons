import pandas as pd

data = {
    "subject": ["Math", "Science", "English", "History"],
    "grade": [95, 92, 88, 85]
}
df = pd.DataFrame(data)

# Ranking + extended metrics
df["rank"] = df["grade"].rank(method="min", ascending=False).astype(int)
df["dense_rank"] = df["grade"].rank(method="dense", ascending=False).astype(int)
df["row_num"] = range(1, len(df) + 1)
df["percentile"] = df["grade"].rank(pct=True).round(2)

print("=== Day115 Dataset with Percentiles ===")
print(df)

import matplotlib.pyplot as plt
import seaborn as sns

# Bar chart for grades
plt.figure(figsize=(8,6))
sns.barplot(x="subject", y="grade", data=df, palette="mako")
plt.title("Day115 — Exam Grades with Percentiles")
plt.xlabel("Subject")
plt.ylabel("Grade")

# Add percentile markers
for i, p in enumerate(df["percentile"]):
    plt.text(i, df["grade"][i] + 1, f"{p:.2f}", ha="center", color="blue")

plt.show()

# Descriptive statistics
print("=== Descriptive Statistics ===")
print(df.describe())

# Grouped averages by rank
print("\n=== Average Grade by Rank ===")
print(df.groupby("rank")["grade"].mean())

# Grouped percentiles by rank
print("\n=== Average Percentile by Rank ===")
print(df.groupby("rank")["percentile"].mean())

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Dataset
data = {
    "subject": ["Math", "Science", "English", "History"],
    "grade": [95, 92, 88, 85]
}
df = pd.DataFrame(data)

# Ranking + percentile focus
df["rank"] = df["grade"].rank(method="min", ascending=False).astype(int)
df["dense_rank"] = df["grade"].rank(method="dense", ascending=False).astype(int)
df["row_num"] = range(1, len(df) + 1)
df["percentile"] = df["grade"].rank(pct=True).round(2)

# Print raw data
print("=== Day115 Dataset with Percentiles ===")
print(df)

# Visualization
plt.figure(figsize=(8,6))
sns.barplot(x="subject", y="grade", data=df, palette="mako")
plt.title("Day115 — Exam Grades with Percentiles")
plt.xlabel("Subject")
plt.ylabel("Grade")

for i, p in enumerate(df["percentile"]):
    plt.text(i, df["grade"][i] + 1, f"{p:.2f}", ha="center", color="blue")

plt.show()

# Statistical summary
print("\n=== Descriptive Statistics ===")
print(df.describe())
print("\n=== Average Grade by Rank ===")
print(df.groupby("rank")["grade"].mean())
print("\n=== Average Percentile by Rank ===")
print(df.groupby("rank")["percentile"].mean())
