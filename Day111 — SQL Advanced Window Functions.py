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

import seaborn as sns
import matplotlib.pyplot as plt

# Barplot showing grades with rank styles
plt.figure(figsize=(10,6))
sns.barplot(x="subject", y="grade", data=df, palette="viridis")

# Annotate each bar with rank, dense_rank, and row_num
for i, row in df.iterrows():
    plt.text(i, row['grade']+1,
             f"R:{row['rank']} D:{row['dense_rank']} N:{row['row_num']}",
             ha='center', fontsize=10, color='black')

plt.title("Day111 Activity 2 — SQL Window Functions Visualization")
plt.xlabel("Subject")
plt.ylabel("Grade")
plt.show()

# Activity 3 — Statistical Summary of Rankings

# Show descriptive statistics of grades
print("Grade Statistics:")
print(df['grade'].describe())

# Compare ranking styles side by side
print("\nRanking Comparison:")
print(df[['subject', 'grade', 'rank', 'dense_rank', 'row_num']])

# Highlight top performer(s)
top_students = df[df['rank'] == 1]
print("\nTop Performer(s):")
print(top_students)

import seaborn as sns
import matplotlib.pyplot as plt

# Activity 4 — Combined Report

# 1. Print summary
print("=== Grade Statistics ===")
print(df['grade'].describe())

print("\n=== Ranking Comparison ===")
print(df[['subject', 'grade', 'rank', 'dense_rank', 'row_num']])

print("\n=== Top Performer(s) ===")
print(df[df['rank'] == 1])

# 2. Visualization
plt.figure(figsize=(10,6))
sns.barplot(x="subject", y="grade", data=df, palette="mako")

for i, row in df.iterrows():
    plt.text(i, row['grade']+1,
             f"R:{row['rank']} D:{row['dense_rank']} N:{row['row_num']}",
             ha='center', fontsize=9, color='black')

plt.title("Day111 Activity 4 — Combined Report")
plt.xlabel("Subject")
plt.ylabel("Grade")
plt.tight_layout()
plt.show()
