import sqlite3
import pandas as pd

def sql_window_demo():
    conn = sqlite3.connect("student_records.db")
    query = """
    SELECT name, subject, grade,
           RANK() OVER (PARTITION BY subject ORDER BY grade DESC) AS rank
    FROM student_report s
    INNER JOIN exams e ON s.id = e.id
    """
    df = pd.read_sql_query(query, conn)
    conn.close()
    print(df)

sql_window_demo()

query = """
    SELECT s.name, e.subject, e.grade,
           RANK() OVER (PARTITION BY e.subject ORDER BY e.grade DESC) AS rank
    FROM student_report s
    INNER JOIN exams e ON s.id = e.id
"""

cursor.execute("INSERT INTO exams (subject, grade) VALUES (?, ?)", (subject, grade))

query = """
SELECT s.name, e.subject, e.grade,
       RANK() OVER (PARTITION BY e.subject ORDER BY e.grade DESC) AS rank
FROM student_report s
INNER JOIN exams e ON s.id = e.id
"""
conn.commit()
conn.close()

query = """
SELECT s.name, e.subject, e.grade,
       RANK() OVER (PARTITION BY e.subject ORDER BY e.grade DESC) AS rank
FROM student_report s
INNER JOIN exams e ON s.id = e.id
"""
