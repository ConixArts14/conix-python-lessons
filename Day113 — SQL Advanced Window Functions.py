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

df = pd.read_sql_query(query, conn)
conn.close()

# Statistical summary
print("📊 Statistical Summary")
print(df.describe(include="all"))

# Grouped summary by rank
print("\n📊 Average grade per rank")
print(df.groupby("rank")["grade"].mean())

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

# --- Activity 1: Raw Data ---
print("📊 Raw Data with Window Functions")
print(df)

# --- Activity 2: Visualization ---
plt.figure(figsize=(8,6))
sns.barplot(x="subject", y="grade", hue="rank", data=df, palette="viridis")
plt.title("Day113 — Exam Grades with Rank")
plt.xlabel("Subject")
plt.ylabel("Grade")
plt.legend(title="Rank")
plt.show()

# --- Activity 3: Statistical Summary ---
print("\n📊 Statistical Summary")
print(df.describe(include="all"))

print("\n📊 Average grade per rank")
print(df.groupby("rank")["grade"].mean())

import sqlite3
conn = sqlite3.connect("student_records.db")
print("✅ Connected")
conn.close()

import sqlite3
conn = sqlite3.connect("student_records.db")
cursor = conn.cursor()
cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
print(cursor.fetchall())
conn.close()

# plt.figure(figsize=(8,6))
# sns.barplot(x="subject", y="grade", hue="rank", data=df, palette="viridis")
# plt.title("Day113 — Exam Grades with Rank")
# plt.xlabel("Subject")
# plt.ylabel("Grade")
# plt.legend(title="Rank")
# plt.show()
plt.show()
plt.close()