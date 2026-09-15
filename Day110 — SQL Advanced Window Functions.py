import pandas as pd
import sqlite3

conn = sqlite3.connect("student_records.db")

query = """
SELECT subject, grade,
       RANK() OVER (ORDER BY grade DESC) AS rank,
       DENSE_RANK() OVER (ORDER BY grade DESC) AS dense_rank,
       ROW_NUMBER() OVER (ORDER BY grade DESC) AS row_num
FROM exams
"""

df = pd.read_sql_query(query, conn)
print(df)

import sqlite3

# 1. Open connection
conn = sqlite3.connect("student_records.db")
cursor = conn.cursor()

# 2. Create student_report table
cursor.execute("""
CREATE TABLE IF NOT EXISTS student_report (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT,
    section TEXT
)
""")

cursor.executemany("""
INSERT INTO student_report (name, section) VALUES (?, ?)
""", [
    ("Alice", "A"),
    ("Bob", "A"),
    ("Charlie", "B"),
    ("Diana", "B")
])

# 3. Create exams table
cursor.execute("""
CREATE TABLE IF NOT EXISTS exams (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    subject TEXT,
    grade INTEGER
)
""")

cursor.executemany("""
INSERT INTO exams (subject, grade) VALUES (?, ?)
""", [
    ("Math", 95),
    ("English", 88),
    ("Science", 92),
    ("History", 85)