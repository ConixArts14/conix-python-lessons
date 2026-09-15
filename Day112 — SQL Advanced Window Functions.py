import pandas as pd
import sqlite3

# Connect to the database
conn = sqlite3.connect("student_records.db")

# Query with window functions
query = """
SELECT subject, grade,
       RANK() OVER (ORDER BY grade DESC) AS rank,
       DENSE_RANK() OVER (ORDER BY grade DESC) AS dense_rank,
       ROW_NUMBER() OVER (ORDER BY grade DESC) AS row_num
FROM exams
"""

# Load results into DataFrame
df = pd.read_sql_query(query, conn)
print(df)

# Close connection
conn.close()

import sqlite3
conn = sqlite3.connect("student_records.db")
cursor = conn.cursor()
cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
print(cursor.fetchall())
conn.close()

import sqlite3
conn = sqlite3.connect("student_records.db")
cursor = conn.cursor()
cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
print(cursor.fetchall())
conn.close()
