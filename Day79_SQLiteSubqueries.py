import sqlite3

def above_average_students():
    conn = sqlite3.connect("student_records.db")
    cursor = conn.cursor()

    cursor.execute("""
        SELECT s.name, AVG(sub.grade) AS avg_grade
        FROM students s
        JOIN subjects sub ON s.id = sub.student_id
        GROUP BY s.name
        HAVING AVG(sub.grade) > (
            SELECT AVG(grade) FROM subjects
        )
    """)

    print("\n📊 Students with average grade above overall average:")
    for row in cursor.fetchall():
        print(f"{row[0]} | Avg Grade: {row[1]:.2f}")

    conn.close()

above_average_students()

def top_performers():
    conn = sqlite3.connect("student_records.db")
    cursor = conn.cursor()

    cursor.execute("""
        SELECT s.name, sub.subject, sub.grade
        FROM students s
        JOIN subjects sub ON s.id = sub.student_id
        WHERE sub.grade = (
            SELECT MAX(grade) FROM subjects
        )
    """)

    print("\n🏆 Students with the highest grade in any subject:")
    for row in cursor.fetchall():
        print(f"{row[0]} | Subject: {row[1]} | Grade: {row[2]}")

    conn.close()

top_performers()

def subject_leaders():
    conn = sqlite3.connect("student_records.db")
    cursor = conn.cursor()

    cursor.execute("""
        SELECT s.name, sub.subject, sub.grade
        FROM students s
        JOIN subjects sub ON s.id = sub.student_id
        WHERE sub.grade = (
            SELECT MAX(sub2.grade)
            FROM subjects sub2
            WHERE sub2.subject = sub.subject
        )
    """)

    print("\n🏅 Best performer per subject:")
    for row in cursor.fetchall():
        print(f"{row[0]} | Subject: {row[1]} | Grade: {row[2]}")

    conn.close()

subject_leaders()

def nested_subquery_report():
    conn = sqlite3.connect("student_records.db")
    cursor = conn.cursor()

    cursor.execute("""
        SELECT s.name,
               (SELECT COUNT(*) 
                FROM subjects sub 
                WHERE sub.student_id = s.id) AS subject_count,
               (SELECT AVG(sub.grade) 
                FROM subjects sub 
                WHERE sub.student_id = s.id) AS avg_grade,
               (SELECT MAX(sub.grade) 
                FROM subjects sub 
                WHERE sub.student_id = s.id) AS max_grade
        FROM students s
    """)

    print("\n📊 Nested Subquery Report (Subjects, Avg, Max per Student):")
    for row in cursor.fetchall():
        print(f"{row[0]} | Subjects: {row[1]} | Avg: {row[2]:.2f} | Max: {row[3]}")

    conn.close()

nested_subquery_report()
