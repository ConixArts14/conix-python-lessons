import seaborn as sns
import matplotlib.pyplot as plt
import sqlite3
import pandas as pd

def seaborn_boxplot():
    conn = sqlite3.connect("student_records.db")
    df = pd.read_sql_query("SELECT subject, grade FROM exams", conn)

    sns.set(style="whitegrid")
    plt.figure(figsize=(8,5))
    sns.boxplot(x="subject", y="grade", data=df, palette="Set3")

    plt.title("Grade Distribution per Subject (Day96)")
    plt.xlabel("Subjects")
    plt.ylabel("Grades")
    plt.tight_layout()
    plt.show()

    conn.close()

seaborn_boxplot()
