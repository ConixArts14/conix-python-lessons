import pandas as pd

# Dataset A
data_a = {
    "subject": ["Math", "Science", "English", "History"],
    "grade": [95, 92, 88, 85]
}
df_a = pd.DataFrame(data_a)

df_a["rank"] = df_a["grade"].rank(method="min", ascending=False).astype(int)
df_a["percentile"] = df_a["grade"].rank(pct=True).round(2)
df_a["cumulative_avg"] = df_a["grade"].expanding().mean().round(2)
df_a["moving_avg"] = df_a["grade"].rolling(window=2).mean().round(2)

# Dataset B
data_b = {
    "subject": ["PE", "Art", "Music", "ICT"],
    "grade": [90, 87, 93, 89]
}
df_b = pd.DataFrame(data_b)

df_b["rank"] = df_b["grade"].rank(method="min", ascending=False).astype(int)
df_b["percentile"] = df_b["grade"].rank(pct=True).round(2)
df_b["cumulative_avg"] = df_b["grade"].expanding().mean().round(2)
df_b["moving_avg"] = df_b["grade"].rolling(window=2).mean().round(2)

# Print datasets
print("=== Day122 Dataset A ===")
print(df_a)
print("\n=== Day122 Dataset B ===")
print(df_b)

import matplotlib.pyplot as plt

plt.figure(figsize=(10,6))

# Dataset A plots
plt.plot(df_a["subject"], df_a["grade"], marker="o", label="A Grade", color="green")
plt.plot(df_a["subject"], df_a["percentile"]*100, marker="s", label="A Percentile (%)", color="blue")
plt.plot(df_a["subject"], df_a["cumulative_avg"], marker="^", label="A Cumulative Avg", color="red")
plt.plot(df_a["subject"], df_a["moving_avg"], marker="D", label="A Moving Avg (2)", color="purple")

# Dataset B plots
plt.plot(df_b["subject"], df_b["grade"], marker="o", label="B Grade", linestyle="--", color="darkgreen")
plt.plot(df_b["subject"], df_b["percentile"]*100, marker="s", label="B Percentile (%)", linestyle="--", color="navy")
plt.plot(df_b["subject"], df_b["cumulative_avg"], marker="^", label="B Cumulative Avg", linestyle="--", color="darkred")
plt.plot(df_b["subject"], df_b["moving_avg"], marker="D", label="B Moving Avg (2)", linestyle="--", color="indigo")

plt.title("Day122 — Dataset A vs Dataset B Trend Comparison")
plt.xlabel("Subject")
plt.ylabel("Value")
plt.legend()
plt.show()

# Dataset A summary
print("=== Dataset A Descriptive Statistics ===")
print(df_a.describe())

print("\n=== Dataset A Average Grade by Rank ===")
print(df_a.groupby("rank")["grade"].mean())

print("\n=== Dataset A Average Percentile by Rank ===")
print(df_a.groupby("rank")["percentile"].mean())

print("\n=== Dataset A Average Cumulative Avg by Rank ===")
print(df_a.groupby("rank")["cumulative_avg"].mean())

print("\n=== Dataset A Average Moving Avg by Rank ===")
print(df_a.groupby("rank")["moving_avg"].mean())

# Dataset B summary
print("\n=== Dataset B Descriptive Statistics ===")
print(df_b.describe())

print("\n=== Dataset B Average Grade by Rank ===")
print(df_b.groupby("rank")["grade"].mean())

print("\n=== Dataset B Average Percentile by Rank ===")
print(df_b.groupby("rank")["percentile"].mean())

print("\n=== Dataset B Average Cumulative Avg by Rank ===")
print(df_b.groupby("rank")["cumulative_avg"].mean())

print("\n=== Dataset B Average Moving Avg by Rank ===")
print(df_b.groupby("rank")["moving_avg"].mean())

import pandas as pd
import matplotlib.pyplot as plt

# Dataset A
data_a = {
    "subject": ["Math", "Science", "English", "History"],
    "grade": [95, 92, 88, 85]
}
df_a = pd.DataFrame(data_a)
df_a["rank"] = df_a["grade"].rank(method="min", ascending=False).astype(int)
df_a["percentile"] = df_a["grade"].rank(pct=True).round(2)
df_a["cumulative_avg"] = df_a["grade"].expanding().mean().round(2)
df_a["moving_avg"] = df_a["grade"].rolling(window=2).mean().round(2)

# Dataset B
data_b = {
    "subject": ["PE", "Art", "Music", "ICT"],
    "grade": [90, 87, 93, 89]
}
df_b = pd.DataFrame(data_b)
df_b["rank"] = df_b["grade"].rank(method="min", ascending=False).astype(int)
df_b["percentile"] = df_b["grade"].rank(pct=True).round(2)
df_b["cumulative_avg"] = df_b["grade"].expanding().mean().round(2)
df_b["moving_avg"] = df_b["grade"].rolling(window=2).mean().round(2)

# Print raw data
print("=== Day122 Dataset A ===")
print(df_a)
print("\n=== Day122 Dataset B ===")
print(df_b)

# Visualization
plt.figure(figsize=(10,6))
plt.plot(df_a["subject"], df_a["grade"], marker="o", label="A Grade", color="green")
plt.plot(df_a["subject"], df_a["percentile"]*100, marker="s", label="A Percentile (%)", color="blue")
plt.plot(df_a["subject"], df_a["cumulative_avg"], marker="^", label="A Cumulative Avg", color="red")
plt.plot(df_a["subject"], df_a["moving_avg"], marker="D", label="A Moving Avg (2)", color="purple")

plt.plot(df_b["subject"], df_b["grade"], marker="o", label="B Grade", linestyle="--", color="darkgreen")
plt.plot(df_b["subject"], df_b["percentile"]*100, marker="s", label="B Percentile (%)", linestyle="--", color="navy")
plt.plot(df_b["subject"], df_b["cumulative_avg"], marker="^", label="B Cumulative Avg", linestyle="--", color="darkred")
plt.plot(df_b["subject"], df_b["moving_avg"], marker="D", label="B Moving Avg (2)", linestyle="--", color="indigo")

plt.title("Day122 — Dataset A vs Dataset B Trend Comparison")
plt.xlabel("Subject")
plt.ylabel("Value")
plt.legend()
plt.show()

# Statistical summary
print("\n=== Dataset A Descriptive Statistics ===")
print(df_a.describe())
print("\n=== Dataset A Grouped Averages by Rank ===")
print
# Export Dataset A
df_a.to_csv("Day122_Dataset_A_Trend_Comparison.csv", index=False)

# Export Dataset B
df_b.to_csv("Day122_Dataset_B_Trend_Comparison.csv", index=False)

print("=== Export Complete: Dataset A & B ===")
