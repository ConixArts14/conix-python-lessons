import seaborn as sns
import matplotlib.pyplot as plt
import sqlite3
import pandas as pd

def seaborn_pairplot():
    conn = sqlite3.connect("student_records.db")
    df = pd.read_sql_query("SELECT subject, grade FROM exams", conn)

    # Pivot to wide format: subjects as columns
    pivot_df = df.pivot_table(index=df.index, columns="subject", values="grade")

    sns.set(style="ticks")
    sns.pairplot(pivot_df, diag_kind="kde", plot_kws={"alpha":0.6, "s":60, "edgecolor":"k"})

    plt.suptitle("Day103 Activity 4: Pairplot of Subject Grade Relationships", y=1.02)
    plt.show()
    conn.close()

seaborn_pairplot()
