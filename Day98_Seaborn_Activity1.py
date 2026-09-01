import seaborn as sns
import matplotlib.pyplot as plt
import sqlite3
import pandas as pd

def seaborn_violinplot():
    conn = sqlite3.connect("student_records.db")
    df = pd.read_sql_query("SELECT subject, grade FROM exams", conn)

    sns.set(style="whitegrid")
    plt.figure(figsize=(7,5))
    sns.violinplot(x="subject", y="grade", data=df, palette="Pastel1")
    plt.title("Violinplot of Grades per Subject (Day98)")
    plt.xlabel("Subjects")
    plt.ylabel("Grades")
    plt.tight_layout()
    plt.show()

    conn.close()

seaborn_violinplot()
