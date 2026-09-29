import pandas as pd

# Dataset A
data_a = {
    "subject": ["Math", "Science", "English", "History"],
    "grade": [95, 92, 88, 85],
    "study_hours": [10, 9, 8, 7],
    "assignments_completed": [12, 11, 10, 9]
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
    "practice_hours": [6, 5, 7, 6],
    "sessions_attended": [8, 7, 9, 8]
}
df_b = pd.DataFrame(data_b)
df_b["rank"] = df_b["grade"].rank(method="min", ascending=False).astype(int)
df_b["percentile"] = df_b["grade"].rank(pct=True).round(2)
df_b["cumulative_avg"] = df_b["grade"].expanding().mean().round(2)
df_b["moving_avg"] = df_b["grade"].rolling(window=2).mean().round(2)

print("=== Day126 Dataset A ===")
print(df_a)
print("\n=== Day126 Dataset B ===")
print(df_b)

import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
import numpy as np

# Dataset A regression (study_hours + assignments_completed)
X_a = df_a[["study_hours","assignments_completed"]]
y_a = df_a["grade"]
model_a = LinearRegression().fit(X_a, y_a)
pred_a = model_a.predict(X_a)

# Dataset B regression (practice_hours + sessions_attended)
X_b = df_b[["practice_hours","sessions_attended"]]
y_b = df_b["grade"]
model_b = LinearRegression().fit(X_b, y_b)
pred_b = model_b.predict(X_b)

# Visualization
plt.figure(figsize=(12,6))

# Dataset A plot
plt.subplot(1,2,1)
plt.scatter(df_a["study_hours"], df_a["grade"], color="green", label="Study Hours vs Grade")
plt.scatter(df_a["assignments_completed"], df_a["grade"], color="orange", label="Assignments vs Grade")
plt.plot(df_a["study_hours"], pred_a, color="black", linestyle="--", label="A Regression")
plt.title("Dataset A: Multi‑Predictor Regression")
plt.xlabel("Study Hours / Assignments")
plt.ylabel("Grades")
plt.legend()

# Dataset B plot
plt.subplot(1,2,2)
plt.scatter(df_b["practice_hours"], df_b["grade"], color="blue", label="Practice Hours vs Grade")
plt.scatter(df_b["sessions_attended"], df_b["grade"], color="purple", label="Sessions vs Grade")
plt.plot(df_b["practice_hours"], pred_b, color="black", linestyle="--", label="B Regression")
plt.title("Dataset B: Multi‑Predictor Regression")
plt.xlabel("Practice Hours / Sessions")
plt.ylabel("Grades")
plt.legend()

plt.tight_layout()
plt.show()

# Dataset A summary
print("=== Dataset A Descriptive Statistics ===")
print(df_a.describe())

print("\n=== Dataset A Grouped Averages by Rank ===")
print(df_a.groupby("rank")[["grade","study_hours","assignments_completed","percentile","cumulative_avg","moving_avg"]].mean())

# Dataset B summary
print("\n=== Dataset B Descriptive Statistics ===")
print(df_b.describe())

print("\n=== Dataset B Grouped Averages by Rank ===")
print(df_b.groupby("rank")[["grade","practice_hours","sessions_attended","percentile","cumulative_avg","moving_avg"]].mean())

import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
import numpy as np

# === Dataset A ===
data_a = {
    "subject": ["Math", "Science", "English", "History"],
    "grade": [95, 92, 88, 85],
    "study_hours": [10, 9, 8, 7],
    "assignments_completed": [12, 11, 10, 9]
}
df_a = pd.DataFrame(data_a)
df_a["rank"] = df_a["grade"].rank(method="min", ascending=False).astype(int)
df_a["percentile"] = df_a["grade"].rank(pct=True).round(2)
df_a["cumulative_avg"] = df_a["grade"].expanding().mean().round(2)
df_a["moving_avg"] = df_a["grade"].rolling(window=2).mean().round(2)

# === Dataset B ===
data_b = {
    "subject": ["PE", "Art", "Music", "ICT"],
    "grade": [90, 87, 93, 89],
    "practice_hours": [6, 5, 7, 6],
    "sessions_attended": [8, 7, 9, 8]
}
df_b = pd.DataFrame(data_b)
df_b["rank"] = df_b["grade"].rank(method="min", ascending=False).astype(int)
df_b["percentile"] = df_b["grade"].rank(pct=True).round(2)
df_b["cumulative_avg"] = df_b["grade"].expanding().mean().round(2)
df_b["moving_avg"] = df_b["grade"].rolling(window=2).mean().round(2)

# === Regression Models ===
X_a = df_a[["study_hours","assignments_completed"]]
y_a = df_a["grade"]
model_a = LinearRegression().fit(X_a, y_a)
pred_a = model_a.predict(X_a)

X_b = df_b[["practice_hours","sessions_attended"]]
y_b = df_b["grade"]
model_b = LinearRegression().fit(X_b, y_b)
pred_b = model_b.predict(X_b)

# === Visualization ===
plt.figure(figsize=(12,6))

plt.subplot(1,2,1)
plt.scatter(df_a["study_hours"], df_a["grade"], color="green", label="Study Hours vs Grade")
plt.scatter(df_a["assignments_completed"], df_a["grade"], color="orange", label="Assignments vs Grade")
plt.plot(df_a["study_hours"], pred_a, color="black", linestyle="--", label="A Regression")
plt.title("Dataset A: Multi‑Predictor Regression")
plt.xlabel("Study Hours / Assignments")
plt.ylabel("Grades")
plt.legend()

plt.subplot(1,2,2)
plt.scatter(df_b["practice_hours"], df_b["grade"], color="blue", label="Practice Hours vs Grade")
plt.scatter(df_b["sessions_attended"], df_b["grade"], color="purple", label="Sessions vs Grade")
plt.plot(df_b["practice_hours"], pred_b, color="black", linestyle="--", label="B Regression")
plt.title("Dataset B: Multi‑Predictor Regression")
plt.xlabel("Practice Hours / Sessions")
plt.ylabel("Grades")
plt.legend()

plt.tight_layout()
plt.show()

# === Summary ===
print("=== Dataset A Descriptive Statistics ===")
print(df_a.describe())
print("\n=== Dataset B Descriptive Statistics ===")
print(df_b.describe())

# Export Dataset A
df_a.to_csv("Day126_Dataset_A_MultiPredictor.csv", index=False)

# Export Dataset B
df_b.to_csv("Day126_Dataset_B_MultiPredictor.csv", index=False)

print("CSV export complete: Day126_Dataset_A_MultiPredictor.csv & Day126_Dataset_B_MultiPredictor.csv")
