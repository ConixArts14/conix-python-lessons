# Day97_Seaborn_Heatmap_Swarmplot_Catplot.py

import seaborn as sns
import matplotlib.pyplot as plt
import sqlite3
import pandas as pd

# --- Setup: Create table + sample data ---
def setup_database():
    conn = sqlite3.connect("student_records.db")
    cursor = conn.cursor()

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS exams (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        exam_date TEXT,
        subject TEXT,
        study_hours INTEGER,
        grade INTEGER,
        gender TEXT
    )
    """)

    # Insert sample rows only if table is empty
    cursor.execute("SELECT COUNT(*) FROM exams")
    if cursor.fetchone()[0] == 0:
        cursor.executemany("""
        INSERT INTO exams (exam_date, subject, study_hours, grade, gender)
        VALUES (?, ?, ?, ?, ?)
        """, [
            ("2026-08-01", "Math", 3, 85, "Male"),
            ("2026-08-05", "Science", 4, 90, "Female"),
            ("2026-08-10", "English", 2, 78, "Male"),
            ("2026-08-15", "History", 5, 88, "Female"),
            ("2026-08-20", "Math", 4, 92, "Female"),
            ("2026-08-25", "Science", 3, 80, "Male")
        ])
        conn.commit()

    conn.close()

# --- Activity 1: Heatmap ---
def seaborn_heatmap():
    conn = sqlite3.connect("student_records.db")
    df = pd.read_sql_query("SELECT study_hours, grade FROM exams", conn)

    corr = df.corr()
    sns.set(style="white")
    plt.figure(figsize=(6,5))
    sns.heatmap(corr, annot=True, cmap="coolwarm", fmt=".2f")
    plt.title("Correlation Heatmap (Day97)")
    plt.tight_layout()
    plt.show()

    conn.close()

# --- Activity 2: Swarmplot ---
def seaborn_swarmplot():
    conn = sqlite3.connect("student_records.db")
    df = pd.read_sql_query("SELECT subject, grade FROM exams", conn)

    sns.set(style="whitegrid")
    plt.figure(figsize=(7,5))
    sns.swarmplot(x="subject", y="grade", data=df, palette="Set1")
    plt.title("Swarmplot of Grades per Subject (Day97)")
    plt.xlabel("Subjects")
    plt.ylabel("Grades")
    plt.tight_layout()
    plt.show()

    conn.close()

# --- Activity 3: Catplot ---
def seaborn_catplot():
    conn = sqlite3.connect("student_records.db")
    df = pd.read_sql_query("SELECT subject, grade, gender FROM exams", conn)

    sns.set(style="whitegrid")
    sns.catplot(x="subject", y="grade", hue="gender", data=df, kind="bar", palette="muted")
    plt.title("Catplot: Grades by Subject and Gender (Day97)")
    plt.tight_layout()
    plt.show()

    conn.close()

# --- Run everything ---
setup_database()
seaborn_heatmap()
seaborn_swarmplot()
seaborn_catplot()

def seaborn_swarmplot():
    conn = sqlite3.connect("student_records.db")
    df = pd.read_sql_query("SELECT subject, grade FROM exams", conn)

    sns.set(style="whitegrid")
    plt.figure(figsize=(7,5))
    sns.swarmplot(x="subject", y="grade", data=df, palette="Set1")
    plt.title("Swarmplot of Grades per Subject (Day97)")
    plt.xlabel("Subjects")
    plt.ylabel("Grades")
    plt.tight_layout()
    plt.show()

    conn.close()

def seaborn_catplot():
    conn = sqlite3.connect("student_records.db")
    df = pd.read_sql_query("SELECT subject, grade, gender FROM exams", conn)

    sns.set(style="whitegrid")
    sns.catplot(x="subject", y="grade", hue="gender", data=df, kind="bar", palette="muted")
    plt.title("Catplot: Grades by Subject and Gender (Day97)")
    plt.tight_layout()
    plt.show()

    conn.close()

def seaborn_pairplot():
    conn = sqlite3.connect("student_records.db")
    df = pd.read_sql_query("SELECT study_hours, grade, subject FROM exams", conn)

    sns.set(style="ticks")
    sns.pairplot(df, hue="subject", palette="husl")
    plt.suptitle("Pairplot: Study Hours, Grades, Subjects (Day97)", y=1.02)
    plt.show()

    conn.close()
