import seaborn as sns
import matplotlib.pyplot as plt
import sqlite3
import pandas as pd

def seaborn_histogram_refined():
    conn = sqlite3.connect("student_records.db")
    df = pd.read_sql_query("SELECT grade FROM exams", conn)

    sns.set(style="darkgrid")
    plt.figure(figsize=(8,5))
    sns.histplot(df["grade"], bins=12, kde=True, color="skyblue")

    plt.title("Grade Distribution (Day95)")
    plt.xlabel("Grades")
    plt.ylabel("Frequency")
    plt.tight_layout()
    plt.show()

    conn.close()

seaborn_histogram_refined()
