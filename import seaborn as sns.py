import sqlite3

conn = sqlite3.connect("student_records.db")
cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS exams (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    subject TEXT,
    grade INTEGER,
    exam_type TEXT
)
""")

cursor.executemany(
    "INSERT INTO exams (subject, grade, exam_type) VALUES (?, ?, ?)",
    [
        ("Math", 85, "Midterm"),
        ("Science", 90, "Final"),
        ("English", 78, "Midterm"),
        ("History", 88, "Final")
    ]
)

conn.commit()
conn.close()
