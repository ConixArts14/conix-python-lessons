import seaborn as sns
import matplotlib.pyplot as plt
import sqlite3
import pandas as pd

def seaborn_pointplot_ci():
    conn = sqlite3.connect("student_records.db")
    df = pd.read_sql_query("SELECT subject, grade FROM exams", conn)

    sns.set(style="whitegrid")
    plt.figure(figsize=(8,6))

    sns.pointplot(x="subject", y="grade", data=df, ci=95, join=True, markers="o", linestyles="-", palette="Dark2")

    plt.title("Day103 Activity 1: Pointplot of Average Grades with CI")
    plt.show()
    conn.close()

seaborn_pointplot_ci()
