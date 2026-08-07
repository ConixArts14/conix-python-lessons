import sqlite3

conn = sqlite3.connect("student_records.db")
cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS subjects (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    student_id INTEGER,
    subject TEXT,
    grade INTEGER,
    FOREIGN KEY(student_id) REFERENCES students(id)
)
""")

conn.commit()
conn.close()
conn = sqlite3.connect("student_records.db")
cursor = conn.cursor()

cursor.executemany("""
INSERT INTO subjects (student_id, subject, grade)
VALUES (?, ?, ?)
""", [
    (1, "Math", 85),
    (1, "Science", 90),
    (2, "Math", 70),
    (2, "Science", 60),
    (3, "Math", 95),
    (3, "Science", 88)
])

conn.commit()
conn.close()
def join_students_subjects():
    conn = sqlite3.connect("student_records.db")
    cursor = conn.cursor()
    cursor.execute("""
        SELECT students.name, subjects.subject, subjects.grade
        FROM students
        INNER JOIN subjects ON students.id = subjects.student_id
    """)
    results = cursor.fetchall()
    conn.close()

    print("\n📘 Student Grades by Subject:")
    for name, subject, grade in results:
        print(f"{name} - {subject}: {grade}")

def group_by_subject():
    conn = sqlite3.connect("student_records.db")
    cursor = conn.cursor()
    cursor.execute("""
        SELECT subject, AVG(grade) 
        FROM subjects 
        GROUP BY subject
    """)
    results = cursor.fetchall()
    conn.close()

    print("\n📊 Average Grade per Subject:")
    for subject, avg in results:
        print(f"{subject}: {avg:.2f}")
