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

import pandas as pd
import sqlite3
import seaborn as sns
import matplotlib.pyplot as plt

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

df = pd.read_sql_query(query, conn)
conn.close()

# Visualization: compare ranks
plt.figure(figsize=(8,6))
sns.barplot(x="subject", y="grade", hue="rank", data=df, palette="viridis")

plt.title("Day113 — Exam Grades with Rank")
plt.xlabel("Subject")
plt.ylabel("Grade")
plt.legend(title="Rank")
plt.show()
