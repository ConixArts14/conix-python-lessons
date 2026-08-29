import sqlite3
import seaborn as sns
import matplotlib.pyplot as plt

def seaborn_subject_avg():
    conn = sqlite3.connect("student_records.db")
    cursor = conn.cursor()

    cursor.execute("""
        SELECT sub.subject, AVG(sub.grade) AS avg_grade
        FROM subjects sub
        GROUP BY sub.subject
    """)

    results = cursor.fetchall()
    subjects = [row[0] for row in results]
    averages = [row[1] for row in results]

    sns.set(style="whitegrid")
    plt.figure(figsize=(8,5))
    sns.barplot(x=subjects, y=averages, palette="Blues_d")

    plt.title("Average Grades per Subject (Seaborn)")
    plt.xlabel("Subjects")
    plt.ylabel("Average Grade")
    plt.tight_layout()
    plt.show()

    conn.close()

seaborn_subject_avg()

import seaborn as sns
import matplotlib.pyplot as plt
import sqlite3
import pandas as pd

def seaborn_percentile_heatmap():
    conn = sqlite3.connect("student_records.db")
    df = pd.read_sql_query("SELECT subject, grade FROM subjects", conn)

    pivot = df.pivot_table(values="grade", index="subject", aggfunc=lambda x: pd.qcut(x, 4, labels=False))
    sns.heatmap(pivot, cmap="YlGnBu", annot=True)

    plt.title("Percentile Distribution per Subject")
    plt.xlabel("Quartile")
    plt.ylabel("Subject")
    plt.tight_layout()
    plt.show()

    conn.close()

seaborn_percentile_heatmap()

def seaborn_boxplot():
    conn = sqlite3.connect("student_records.db")
    df = pd.read_sql_query("SELECT subject, grade FROM subjects", conn)

    sns.set(style="whitegrid")
    plt.figure(figsize=(8,5))
    sns.boxplot(x="subject", y="grade", data=df, palette="Set2")

    plt.title("Grade Spread per Subject (Boxplot)")
    plt.xlabel("Subjects")
    plt.ylabel("Grades")
    plt.tight_layout()
    plt.show()

    conn.close()

seaborn_boxplot()
