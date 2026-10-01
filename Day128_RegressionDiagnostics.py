from sklearn.metrics import r2_score, mean_absolute_error

# Predict with integrated model
X = df_combined[["study_hours","assignments_completed","practice_hours","sessions_attended"]].fillna(0)
y = df_combined["grade"]
pred = model.predict(X)

# R² score
r2 = r2_score(y, pred)

# Residuals
residuals = y - pred

# Mean Absolute Error
mae = mean_absolute_error(y, pred)

print("=== Day128 Regression Diagnostics ===")
print(f"R² Score: {r2:.3f}")
print(f"Mean Absolute Error: {mae:.2f}")
print("\nResiduals:")
print(residuals)

import matplotlib.pyplot as plt

# Residuals
residuals = y - pred

# Visualization
plt.figure(figsize=(8,6))
plt.scatter(df_combined["subject"], residuals, color="crimson", label="Residuals")
plt.axhline(y=0, color="black", linestyle="--", label="Perfect Prediction")
plt.title("Day128 Residuals Visualization")
plt.xlabel("Subjects")
plt.ylabel("Residuals (Actual - Predicted)")
plt.legend()
plt.show()
