import seaborn as sns
import matplotlib.pyplot as plt
import sqlite3
import pandas as pd

def seaborn_scatter_regression():
    conn = sqlite3.connect("student_records.db")
    df = pd.read_sql_query("SELECT subject, grade FROM exams", conn)

    sns.set(style="whitegrid")

    # lmplot creates scatter + regression line
    sns.lmplot(x="subject", y="grade", data=df, ci=95, markers="o", palette="muted")

    plt.title("Day103 Activity 2: Scatterplot with Regression Line of Grades")
    plt.show()
    conn.close()

seaborn_scatter_regression()
