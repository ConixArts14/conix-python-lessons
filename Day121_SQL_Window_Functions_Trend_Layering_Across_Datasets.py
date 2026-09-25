import pandas as pd

data = {
    "subject": ["Math", "Science", "English", "History", "PE", "Art", "Music"],
    "grade": [95, 92, 88, 85, 90, 87, 93]
}
df = pd.DataFrame(data)

# Ranking + percentile setup
df["rank"] = df["grade"].rank(method="min", ascending=False).astype(int)
df["dense_rank"] = df["grade"].rank(method="dense", ascending=False).astype(int)
df["row_num"] = range(1, len(df) + 1)
df["percentile"] = df["grade"].rank(pct=True).round(2)

# Cumulative average
df["cumulative_avg"] = df["grade"].expanding().mean().round(2)

# Moving average (window=3)
df["moving_avg"] = df["grade"].rolling(window=3).mean().round(2)

# Print dataset
print("=== Day121 Dataset with Percentiles, Cumulative & Moving Avg ===")
print(df)

import matplotlib.pyplot as plt

# Line chart for grades + percentiles + cumulative + moving average
plt.figure(figsize=(9,6))
plt.plot(df["subject"], df["grade"], marker="o", label="Grade", color="green")
plt.plot(df["subject"], df["percentile"]*100, marker="s", label="Percentile (%)", color="blue")
plt.plot(df["subject"], df["cumulative_avg"], marker="^", label="Cumulative Avg", color="red")
plt.plot(df["subject"], df["moving_avg"], marker="D", label="Moving Avg (3)", color="purple")

plt.title("Day121 — Grades, Percentiles, Cumulative & Moving Average Trends")
plt.xlabel("Subject")
plt.ylabel("Value")
plt.legend()

# Add labels above points
for i, (g, p, c, m) in enumerate(zip(df["grade"], df["percentile"], df["cumulative_avg"], df["moving_avg"])):
    plt.text(i, g+1, f"{g}", ha="center", color="green")
    plt.text(i, p*100+1, f"{p:.2f}", ha="center", color="blue")
    plt.text(i, c+1, f"{c:.2f}", ha="center", color="red")
    if not pd.isna(m):
        plt.text(i, m+1, f"{m:.2f}", ha="center", color="purple")

plt.show()

# Descriptive statistics
print("=== Descriptive Statistics ===")
print(df.describe())

# Grouped averages by rank
print("\n=== Average Grade by Rank ===")
print(df.groupby("rank")["grade"].mean())

print("\n=== Average Percentile by Rank ===")
print(df.groupby("rank")["percentile"].mean())

print("\n=== Average Cumulative Avg by Rank ===")
print(df.groupby("rank")["cumulative_avg"].mean())

print("\n=== Average Moving Avg by Rank ===")
print(df.groupby("rank")["moving_avg"].mean())

import pandas as pd
import matplotlib.pyplot as plt

# Dataset
data = {
    "subject": ["Math", "Science", "English", "History", "PE", "Art", "Music"],
    "grade": [95, 92, 88, 85, 90, 87, 93]
}
df = pd.DataFrame(data)

# Ranking + percentile setup
df["rank"] = df["grade"].rank(method="min", ascending=False).astype(int)
df["dense_rank"] = df["grade"].rank(method="dense", ascending=False).astype(int)
df["row_num"] = range(1, len(df) + 1)
df["percentile"] = df["grade"].rank(pct=True).round(2)

# Cumulative average
df["cumulative_avg"] = df["grade"].expanding().mean().round(2)

# Moving average (window=3)
df["moving_avg"] = df["grade"].rolling(window=3).mean().round(2)

# Print raw data
print("=== Day121 Dataset with Percentiles, Cumulative & Moving Avg ===")
print(df)

# Visualization
plt.figure(figsize=(9,6))
plt.plot(df["subject"], df["grade"], marker="o", label="Grade", color="green")
plt.plot(df["subject"], df["percentile"]*100, marker="s", label="Percentile (%)", color="blue")
plt.plot(df["subject"], df["cumulative_avg"], marker="^", label="Cumulative Avg", color="red")
plt.plot(df["subject"], df["moving_avg"], marker="D", label="Moving Avg (3)", color="purple")

plt.title("Day121 — Grades, Percentiles, Cumulative & Moving Average Trends")
plt.xlabel("Subject")
plt.ylabel("Value")
plt.legend()

for i, (g, p, c, m) in enumerate(zip(df["grade"], df["percentile"], df["cumulative_avg"], df["moving_avg"])):
    plt.text(i, g+1, f"{g}", ha="center", color="green")
    plt.text(i, p*100+1, f"{p:.2f}", ha="center", color="blue")
    plt.text(i, c+1, f"{c:.2f}", ha="center", color="red")
    if not pd.isna(m):
        plt.text(i, m+1, f"{m:.2f}", ha="center", color="purple")

plt.show()

# Statistical summary
print("\n=== Descriptive Statistics ===")
print(df.describe())
print("\n=== Average Grade by Rank ===")
print(df.groupby("rank")["grade"].mean())
print("\n=== Average Percentile by Rank ===")
print(df.groupby("rank")["percentile"].mean())
print("\n=== Average Cumulative Avg by Rank ===")
print(df.groupby("rank")["cumulative_avg"].mean())
print("\n=== Average Moving Avg by Rank ===")
print(df.groupby("rank")["moving_avg"].mean())
