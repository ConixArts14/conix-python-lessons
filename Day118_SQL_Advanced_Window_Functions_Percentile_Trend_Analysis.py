import pandas as pd

data = {
    "subject": ["Math", "Science", "English", "History"],
    "grade": [95, 92, 88, 85]
}
df = pd.DataFrame(data)

# Ranking + percentile trend setup
df["rank"] = df["grade"].rank(method="min", ascending=False).astype(int)
df["dense_rank"] = df["grade"].rank(method="dense", ascending=False).astype(int)
df["row_num"] = range(1, len(df) + 1)
df["percentile"] = df["grade"].rank(pct=True).round(2)

# Print dataset
print("=== Day118 Dataset with Percentiles ===")
print(df)

import matplotlib.pyplot as plt

# Line chart for grades + percentiles
plt.figure(figsize=(8,6))
plt.plot(df["subject"], df["grade"], marker="o", label="Grade", color="green")
plt.plot(df["subject"], df["percentile"]*100, marker="s", label="Percentile (%)", color="blue")

plt.title("Day118 — Exam Grades vs Percentile Trend")
plt.xlabel("Subject")
plt.ylabel("Value")
plt.legend()

# Add labels above points
for i, (g, p) in enumerate(zip(df["grade"], df["percentile"])):
    plt.text(i, g+1, f"{g}", ha="center", color="green")
    plt.text(i, p*100+1, f"{p:.2f}", ha="center", color="blue")

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

# Dataset
data = {
    "subject": ["Math", "Science", "English", "History"],
    "grade": [95, 92, 88, 85]
}
df = pd.DataFrame(data)

# Ranking + percentile setup
df["rank"] = df["grade"].rank(method="min", ascending=False).astype(int)
df["dense_rank"] = df["grade"].rank(method="dense", ascending=False).astype(int)
df["row_num"] = range(1, len(df) + 1)
df["percentile"] = df["grade"].rank(pct=True).round(2)

# Print raw data
print("=== Day118 Dataset with Percentiles ===")
print(df)

# Visualization
plt.figure(figsize=(8,6))
plt.plot(df["subject"], df["grade"], marker="o", label="Grade", color="green")
plt.plot(df["subject"], df["percentile"]*100, marker="s", label="Percentile (%)", color="blue")

plt.title("Day118 — Exam Grades vs Percentile Trend")
plt.xlabel("Subject")
plt.ylabel("Value")
plt.legend()

for i, (g, p) in enumerate(zip(df["grade"], df["percentile"])):
    plt.text(i, g+1, f"{g}", ha="center", color="green")
    plt.text(i, p*100+1, f"{p:.2f}", ha="center", color="blue")

plt.show()

# Statistical summary
print("\n=== Descriptive Statistics ===")
print(df.describe())
print("\n=== Average Grade by Rank ===")
print(df.groupby("rank")["grade"].mean())
print("\n=== Average Percentile by Rank ===")
print(df.groupby("rank")["percentile"].mean())

# Export to CSV
df.to_csv("Day118_SQL_Advanced_Window_Functions_Percentile_Trend_Analysis.csv", index=False)

print("=== Export Complete ===")
