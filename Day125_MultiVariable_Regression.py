import pandas as pd

# Dataset A
data_a = {
    "subject": ["Math", "Science", "English", "History"],
    "grade": [95, 92, 88, 85],
    "study_hours": [10, 9, 8, 7]
}
df_a = pd.DataFrame(data_a)
df_a["rank"] = df_a["grade"].rank(method="min", ascending=False).astype(int)
df_a["percentile"] = df_a["grade"].rank(pct=True).round(2)
df_a["cumulative_avg"] = df_a["grade"].expanding().mean().round(2)
df_a["moving_avg"] = df_a["grade"].rolling(window=2).mean().round(2)

# Dataset B
data_b = {
    "subject": ["PE", "Art", "Music", "ICT"],
    "grade": [90, 87, 93, 89],
    "practice_hours": [6, 5, 7, 6]
}
df_b = pd.DataFrame(data_b)
df_b["rank"] = df_b["grade"].rank(method="min", ascending=False).astype(int)
df_b["percentile"] = df_b["grade"].rank(pct=True).round(2)
df_b["cumulative_avg"] = df_b["grade"].expanding().mean().round(2)
df_b["moving_avg"] = df_b["grade"].rolling(window=2).mean().round(2)

print("=== Day125 Dataset A ===")
print(df_a)
print("\n=== Day125 Dataset B ===")
print(df_b)
