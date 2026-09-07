import seaborn as sns
import matplotlib.pyplot as plt
import sqlite3
import pandas as pd

def seaborn_barplot_hue():
    conn = sqlite3.connect("student_records.db")
    df = pd.read_sql_query("SELECT subject, grade, exam_type FROM exams", conn)

    sns.set(style="whitegrid")
    plt.figure(figsize=(9,6))
    sns.barplot(
        x="subject",
        y="grade",
        hue="exam_type",
        data=df,
        ci=None,
        palette="Paired"
    )

    plt.title("Day104 Activity 1: Barplot of Grades by Subject and Exam Type")
    plt.show()
    conn.close()

seaborn_barplot_hue()

import seaborn as sns
import matplotlib.pyplot as plt
import sqlite3
import pandas as pd

def seaborn_violinplot():
    conn = sqlite3.connect("student_records.db")
    df = pd.read_sql_query("SELECT subject, grade, exam_type FROM exams", conn)

    sns.set(style="whitegrid")
    plt.figure(figsize=(9,6))
    sns.violinplot(
        x="subject",
        y="grade",
        hue="exam_type",
        data=df,
        split=True,
        palette="Set2"
    )

    plt.title("Day104 Activity 2: Violinplot of Grade Distribution by Subject and Exam Type")
    plt.show()
    conn.close()

seaborn_violinplot()
