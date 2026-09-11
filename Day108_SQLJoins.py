import sqlite3
import pandas as pd

def sql_joins_demo():
    conn = sqlite3.connect("student_records.db")
    query = """
    SELECT s.name, s.section, e.subject, e.grade, e.exam_type
    FROM student_report s
    INNER JOIN exams e ON s.id = e.id
    """
    df = pd.read_sql_query(query, conn)
    conn.close()
    print(df)

sql_joins_demo()
