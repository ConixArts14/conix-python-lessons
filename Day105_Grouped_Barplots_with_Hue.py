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

    plt.title("Day105 Activity 1: Barplot of Grades by Subject and Exam Type")
    plt.show()
    conn.close()

seaborn_barplot_hue()

import sqlite3

conn = sqlite3.connect("student_records.db")
cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS exams (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    subject TEXT,
    grade INTEGER,
    exam_type TEXT
)
""")

cursor.executemany(
    "INSERT INTO exams (subject, grade, exam_type) VALUES (?, ?, ?)",
    [
        ("Math", 85, "Midterm"),
        ("Science", 90, "Final"),
        ("English", 78, "Midterm"),
        ("History", 88, "Final")
    ]
)

conn.commit()
conn.close()

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

    plt.title("Day105 Activity 2: Violinplot of Grade Distribution by Subject and Exam Type")
    plt.show()
    conn.close()

seaborn_violinplot()

import seaborn as sns
import matplotlib.pyplot as plt
import sqlite3
import pandas as pd

def seaborn_boxplot():
    conn = sqlite3.connect("student_records.db")
    df = pd.read_sql_query("SELECT subject, grade, exam_type FROM exams", conn)

    sns.set(style="whitegrid")
    plt.figure(figsize=(9,6))
    sns.boxplot(
        x="subject",
        y="grade",
        hue="exam_type",
        data=df,
        palette="Set3"
    )

    plt.title("Day105 Activity 3: Boxplot of Grade Distribution by Subject and Exam Type")
    plt.show()
    conn.close()

seaborn_boxplot()
