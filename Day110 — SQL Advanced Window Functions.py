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