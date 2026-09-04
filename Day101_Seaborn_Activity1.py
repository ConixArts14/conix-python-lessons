import seaborn as sns
import matplotlib.pyplot as plt
import sqlite3
import pandas as pd

def seaborn_violin_swarm():
    conn = sqlite3.connect("student_records.db")
    df = pd.read_sql_query("SELECT subject, grade FROM exams", conn)

    sns.set(style="whitegrid")
    plt.figure(figsize=(8,6))

    # Violinplot for distribution
    sns.violinplot(x="subject", y="grade", data=df, inner=None, palette="Pastel1")

    # Swarmplot overlay for individual points
    sns.swarmplot(x="subject", y="grade", data=df, color="k", alpha=0.6)

    plt.title("Day101 Activity 1: Violin + Swarmplot of Grades")
    plt.show()
    conn.close()

seaborn_violin_swarm()
