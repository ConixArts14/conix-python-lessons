import seaborn as sns
import matplotlib.pyplot as plt
import sqlite3
import pandas as pd

def seaborn_heatmap_corr():
    conn = sqlite3.connect("student_records.db")
    df = pd.read_sql_query("SELECT subject, grade FROM exams", conn)

    # Pivot to wide format: subjects as columns
    pivot_df = df.pivot_table(index=df.index, columns="subject", values="grade")

    sns.set(style="white")
    plt.figure(figsize=(8,6))

    # Correlation heatmap
    corr = pivot_df.corr()
    sns.heatmap(corr, annot=True, cmap="coolwarm", center=0)

    plt.title("Day103 Activity 3: Heatmap of Subject Grade Correlations")
    plt.show()
    conn.close()

seaborn_heatmap_corr()
