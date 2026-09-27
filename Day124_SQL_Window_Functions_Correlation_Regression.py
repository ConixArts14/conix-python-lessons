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

print("=== Day124 Dataset A ===")
print(df_a)
print("\n=== Day124 Dataset B ===")
print(df_b)

# Dataset A summary
print("=== Dataset A Descriptive Statistics ===")
print(df_a.describe())

print("\n=== Dataset A Grouped Averages by Rank ===")
print(df_a.groupby("rank")[["grade","percentile","cumulative_avg","moving_avg"]].mean())

# Dataset B summary
print("\n=== Dataset B Descriptive Statistics ===")
print(df_b.describe())

print("\n=== Dataset B Grouped Averages by Rank ===")
print(df_b.groupby("rank")[["grade","percentile","cumulative_avg","moving_avg"]].mean())
