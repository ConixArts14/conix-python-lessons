import pandas as pd

data = {
    "subject": ["Math", "Science", "English", "History", "PE", "Art"],
    "grade": [95, 92, 88, 85, 90, 87]
}
df = pd.DataFrame(data)

# Ranking + percentile setup
df["rank"] = df["grade"].rank(method="min", ascending=False).astype(int)
df["dense_rank"] = df["grade"].rank(method="dense", ascending=False).astype(int)
df["row_num"] = range(1, len(df) + 1)
df["percentile"] = df["grade"].rank(pct=True).round(2)

# Cumulative average
df["cumulative_avg"] = df["grade"].expanding().mean().round(2)

# Print dataset
print("=== Day120 Dataset with Percentiles & Cumulative Avg ===")
print(df)

import matplotlib.pyplot as plt

# Line chart for grades + percentiles + cumulative average
plt.figure(figsize=(8,6))
plt.plot(df["subject"], df["grade"], marker="o", label="Grade", color="green")
plt.plot(df["subject"], df["percentile"]*100, marker="s", label="Percentile (%)", color="blue")
plt.plot(df["subject"], df["cumulative_avg"], marker="^", label="Cumulative Avg", color="red")

plt.title("Day120 — Grades, Percentiles, and Cumulative Average")
plt.xlabel("Subject")
plt.ylabel("Value")
plt.legend()

# Add labels above points
for i, (g, p, c) in enumerate(zip(df["grade"], df["percentile"], df["cumulative_avg"])):
    plt.text(i, g+1, f"{g}", ha="center", color="green")
    plt.text(i, p*100+1, f"{p:.2f}", ha="center", color="blue")
    plt.text(i, c+1, f"{c:.2f}", ha="center", color="red")

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

# Grouped cumulative averages by rank
print("\n=== Average Cumulative Avg by Rank ===")
print(df.groupby("rank")["cumulative_avg"].mean())

import pandas as pd
import matplotlib.pyplot as plt

# Dataset
data = {
    "subject": ["Math", "Science", "English", "History", "PE", "Art"],
    "grade": [95, 92, 88, 85, 90, 87]
}
df = pd.DataFrame(data)

# Ranking + percentile setup
df["rank"] = df["grade"].rank(method="min", ascending=False).astype(int)
df["dense_rank"] = df["grade"].rank(method="dense", ascending=False).astype(int)
df["row_num"] = range(1, len(df) + 1)
df["percentile"] = df["grade"].rank(pct=True).round(2)

# Cumulative average
df["cumulative_avg"] = df["grade"].expanding().mean().round(2)

# Print raw data
print("=== Day120 Dataset with Percentiles & Cumulative Avg ===")
print(df)

# Visualization
plt.figure(figsize=(8,6))
plt.plot(df["subject"], df["grade"], marker="o", label="Grade", color="green")
plt.plot(df["subject"], df["percentile"]*100, marker="s", label="Percentile (%)", color="blue")
plt.plot(df["subject"], df["cumulative_avg"], marker="^", label="Cumulative Avg", color="red")

plt.title("Day120 — Grades, Percentiles, and Cumulative Average")
plt.xlabel("Subject")
plt.ylabel("Value")
plt.legend()

for i, (g, p, c) in enumerate(zip(df["grade"], df["percentile"], df["cumulative_avg"])):
    plt.text(i, g+1, f"{g}", ha="center", color="green")
    plt.text(i, p*100+1, f"{p:.2f}", ha="center", color="blue")
    plt.text(i, c+1, f"{c:.2f}", ha="center", color="red")

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

# Export to CSV
df.to_csv("Day120_SQL_Window_Functions_Cumulative_Percentile_Comparison.csv", index=False)

print("=== Export Complete ===")
