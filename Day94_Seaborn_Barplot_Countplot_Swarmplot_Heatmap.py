import seaborn as sns
import matplotlib.pyplot as plt
import sqlite3
import pandas as pd

def seaborn_barplot_hue():
    conn = sqlite3.connect("student_records.db")
    df = pd.read_sql_query("SELECT subject, grade, gender FROM exams", conn)

    sns.set(style="whitegrid")
    plt.figure(figsize=(8,5))
    sns.barplot(x="subject", y="grade", hue="gender", data=df, palette="pastel")

    plt.title("Average Grades per Subject by Gender")
    plt.xlabel("Subjects")
    plt.ylabel("Average Grade")
    plt.tight_layout()
    plt.show()

    conn.close()

seaborn_barplot_hue()

def seaborn_heatmap():
    conn = sqlite3.connect("student_records.db")
    df = pd.read_sql_query("SELECT study_hours, grade FROM exams", conn)

    corr = df.corr()

    sns.set(style="white")
    plt.figure(figsize=(6,4))
    sns.heatmap(corr, annot=True, cmap="coolwarm", fmt=".2f")

    plt.title("Correlation Heatmap: Study Hours vs Grades")
    plt.tight_layout()
    plt.show()

    conn.close()

seaborn_heatmap()

def seaborn_swarmplot():
    conn = sqlite3.connect("student_records.db")
    df = pd.read_sql_query("SELECT subject, grade FROM exams", conn)

    sns.set(style="whitegrid")
    plt.figure(figsize=(8,5))
    sns.swarmplot(x="subject", y="grade", data=df, palette="deep")

    plt.title("Individual Grade Distribution per Subject")
    plt.xlabel("Subjects")
    plt.ylabel("Grades")
    plt.tight_layout()
    plt.show()

    conn.close()

seaborn_swarmplot()

import seaborn as sns
import matplotlib.pyplot as plt
import sqlite3
import pandas as pd

def seaborn_countplot():
    conn = sqlite3.connect("student_records.db")
    df = pd.read_sql_query("SELECT subject FROM exams", conn)

    sns.set(style="whitegrid")
    plt.figure(figsize=(8,5))
    sns.countplot(x="subject", data=df, palette="Set2")

    plt.title("Number of Students per Subject")
    plt.xlabel("Subjects")
    plt.ylabel("Count")
    plt.tight_layout()
    plt.show()

    conn.close()

seaborn_countplot()
