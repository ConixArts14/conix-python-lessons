import pandas as pd

# Dataset A
data_a = {
    "subject": ["Math", "Science", "English", "History"],
    "grade": [95, 92, 88, 85],
    "study_hours": [10, 9, 8, 7],
    "assignments_completed": [12, 11, 10, 9]
}
df_a = pd.DataFrame(data_a)

# Dataset B
data_b = {
    "subject": ["PE", "Art", "Music", "ICT"],
    "grade": [90, 87, 93, 89],
    "practice_hours": [6, 5, 7, 6],
    "sessions_attended": [8, 7, 9, 8]
}
df_b = pd.DataFrame(data_b)

# Merge datasets
df_combined = pd.concat([df_a, df_b], ignore_index=True)

# Add rank, percentile, cumulative & moving averages
df_combined["rank"] = df_combined["grade"].rank(method="min", ascending=False).astype(int)
df_combined["percentile"] = df_combined["grade"].rank(pct=True).round(2)
df_combined["cumulative_avg"] = df_combined["grade"].expanding().mean().round(2)
df_combined["moving_avg"] = df_combined["grade"].rolling(window=2).mean().round(2)

print("=== Day127 Combined Dataset ===")
print(df_combined)

import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression

# Integrated regression (study_hours + assignments + practice_hours + sessions)
X = df_combined[["study_hours","assignments_completed","practice_hours","sessions_attended"]].fillna(0)
y = df_combined["grade"]

model = LinearRegression().fit(X, y)
pred = model.predict(X)

# Visualization
plt.figure(figsize=(8,6))
plt.scatter(y, pred, color="teal", label="Predicted vs Actual")
plt.plot([y.min(), y.max()], [y.min(), y.max()], color="black", linestyle="--", label="Perfect Fit")
plt.title("Day127 Integrated Multi‑Predictor Regression")
plt.xlabel("Actual Grades")
plt.ylabel("Predicted Grades")
plt.legend()
plt.show()

import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression

# === Combined Dataset ===
data_a = {
    "subject": ["Math", "Science", "English", "History"],
    "grade": [95, 92, 88, 85],
    "study_hours": [10, 9, 8, 7],
    "assignments_completed": [12, 11, 10, 9]
}
df_a = pd.DataFrame(data_a)

data_b = {
    "subject": ["PE", "Art", "Music", "ICT"],
    "grade": [90, 87, 93, 89],
    "practice_hours": [6, 5, 7, 6],
    "sessions_attended": [8, 7, 9, 8]
}
df_b = pd.DataFrame(data_b)

df_combined = pd.concat([df_a, df_b], ignore_index=True)
df_combined["rank"] = df_combined["grade"].rank(method="min", ascending=False).astype(int)
df_combined["percentile"] = df_combined["grade"].rank(pct=True).round(2)
df_combined["cumulative_avg"] = df_combined["grade"].expanding().mean().round(2)
df_combined["moving_avg"] = df_combined["grade"].rolling(window=2).mean().round(2)

# === Regression Model ===
X = df_combined[["study_hours","assignments_completed","practice_hours","sessions_attended"]].fillna(0)
y = df_combined["grade"]
model = LinearRegression().fit(X, y)
pred = model.predict(X)

# === Visualization ===
plt.figure(figsize=(8,6))
plt.scatter(y, pred, color="teal", label="Predicted vs Actual")
plt.plot([y.min(), y.max()], [y.min(), y.max()], color="black", linestyle="--", label="Perfect Fit")
plt.title("Day127 Integrated Multi‑Predictor Regression")
plt.xlabel("Actual Grades")
plt.ylabel("Predicted Grades")
plt.legend()
plt.show()

# === Summary ===
print("=== Day127 Combined Dataset Descriptive Statistics ===")
print(df_combined.describe())

print("\n=== Day127 Grouped Averages by Rank ===")
print(df_combined.groupby("rank")[["grade","study_hours","assignments_completed","practice_hours","sessions_attended","percentile","cumulative_avg","moving_avg"]].mean())

# Export Combined Dataset
df_combined.to_csv("Day127_Combined_MultiPredictor.csv", index=False)

print("CSV export complete: Day127_Combined_MultiPredictor.csv")
