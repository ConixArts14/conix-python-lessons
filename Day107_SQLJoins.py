import sqlite3
import pandas as pd

def sql_joins_demo():
    conn = sqlite3.connect("student_records.db")
    cursor = conn.cursor()

    # Example: join exams with student_report
    query = """
    SELECT s.name, s.section, e.subject, e.grade, e.exam_type
    FROM student_report s
    JOIN exams e ON s.id = e.id
    """
    df = pd.read_sql_query(query, conn)

    print(df.head())

    conn.close()

if __name__ == "__main__":
    sql_joins_demo()
