import seaborn as sns
import matplotlib.pyplot as plt
import sqlite3
import pandas as pd

def seaborn_lineplot():
    conn = sqlite3.connect("student_records.db")
    df = pd.read_sql_query("SELECT exam_date, grade FROM exams", conn)

    sns.set(style="darkgrid")
    plt.figure(figsize=(8,5))
    sns.lineplot(x="exam_date", y="grade", data=df, marker="o", color="blue")

    plt.title("Grade Trends Over Time")
    plt.xlabel("Exam Date")
    plt.ylabel("Grade")
    plt.tight_layout()
    plt.show()

    conn.close()

seaborn_lineplot()

import seaborn as sns
import matplotlib.pyplot as plt
import sqlite3
import pandas as pd

def seaborn_histogram():
    conn = sqlite3.connect("student_records.db")
    df = pd.read_sql_query("SELECT grade FROM exams", conn)

    sns.set(style="whitegrid")
    plt.figure(figsize=(8,5))
    sns.histplot(df["grade"], bins=10, kde=True, color="green")

    plt.title("Grade Distribution Histogram")
    plt.xlabel("Grades")
    plt.ylabel("Frequency")
    plt.tight_layout()
    plt.show()

    conn.close()

seaborn_histogram()

import seaborn as sns
import matplotlib.pyplot as plt
import sqlite3
import pandas as pd

def seaborn_scatterplot():
    conn = sqlite3.connect("student_records.db")
    df = pd.read_sql_query("SELECT study_hours, grade FROM exams", conn)

    sns.set(style="whitegrid")
    plt.figure(figsize=(8,5))
    sns.scatterplot(x="study_hours", y="grade", data=df, hue="grade", palette="coolwarm")

    plt.title("Study Hours vs Grades")
    plt.xlabel("Study Hours")
    plt.ylabel("Grade")
    plt.tight_layout()
    plt.show()

    conn.close()

seaborn_scatterplot()

import seaborn as sns
import matplotlib.pyplot as plt
import sqlite3
import pandas as pd

def seaborn_violinplot():
    conn = sqlite3.connect("student_records.db")
    df = pd.read_sql_query("SELECT subject, grade FROM exams", conn)

    sns.set(style="whitegrid")
    plt.figure(figsize=(8,5))
    sns.violinplot(x="subject", y="grade", data=df, palette="muted")

    plt.title("Grade Distribution per Subject (Violin Plot)")
    plt.xlabel("Subjects")
    plt.ylabel("Grades")
    plt.tight_layout()
    plt.show()

    conn.close()

seaborn_violinplot()

import sqlite3
conn = sqlite3.connect("student_records.db")
cursor = conn.cursor()

cursor.execute("""
CREATE TABLE exams (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    exam_date TEXT,
    subject TEXT,
    study_hours INTEGER,
    grade INTEGER
)
""")

# Insert sample data
cursor.executemany("""
INSERT INTO exams (exam_date, subject, study_hours, grade)
VALUES (?, ?, ?, ?)
""", [
    ("2026-08-01", "Math", 3, 85),
    ("2026-08-05", "Science", 4, 90),
    ("2026-08-10", "English", 2, 78),
    ("2026-08-15", "History", 5, 88)
])

conn.commit()
conn.close()
