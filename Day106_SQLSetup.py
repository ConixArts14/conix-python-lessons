import sqlite3

# Connect to database (creates file if missing)
conn = sqlite3.connect("student_records.db")
cursor = conn.cursor()

# Create exams table
cursor.execute("""
CREATE TABLE IF NOT EXISTS exams (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    subject TEXT,
    grade INTEGER
)
""")

# Insert sample data
cursor.executemany("INSERT INTO exams (subject, grade) VALUES (?, ?)", [
    ("Math", 95),
    ("Science", 92),
    ("English", 88),
    ("History", 85)
])

conn.commit()
conn.close()

print("✅ Exams table created with sample data.")

import sqlite3
conn = sqlite3.connect("student_records.db")
cursor = conn.cursor()
cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
print(cursor.fetchall())
conn.close()
