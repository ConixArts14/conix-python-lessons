import seaborn as sns
import matplotlib.pyplot as plt
import sqlite3
import pandas as pd

def seaborn_barplot_ci():
    conn = sqlite3.connect("student_records.db")
    df = pd.read_sql_query("SELECT subject, grade FROM exams", conn)

    sns.set(style="whitegrid")
    plt.figure(figsize=(8,6))

    sns.barplot(x="subject", y="grade", data=df, ci=95, palette="Set3")

    plt.title("Day102 Activity 1: Barplot of Average Grades with CI")
    plt.show()
    conn.close()

seaborn_barplot_ci()
