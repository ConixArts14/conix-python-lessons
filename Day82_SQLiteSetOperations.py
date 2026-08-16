import sqlite3

def intersect_students():
    conn = sqlite3.connect("student_records.db")
    cursor = conn.cursor()

    cursor.execute("""
        SELECT s.name
        FROM students s
        JOIN subjects sub ON s.id = sub.student_id
        WHERE sub.subject = 'Math'
        
        INTERSECT
        
        SELECT s.name
        FROM students s
        JOIN subjects sub ON s.id = sub.student_id
        WHERE sub.subject = 'Science'
    """)

    print("\n📊 Students Enrolled in BOTH Math and Science:")
    for row in cursor.fetchall():
        print(f"{row[0]}")

    conn.close()

intersect_students()

def except_students():
    conn = sqlite3.connect("student_records.db")
    cursor = conn.cursor()

    cursor.execute("""
        SELECT s.name
        FROM students s
        JOIN subjects sub ON s.id = sub.student_id
        WHERE sub.subject = 'Math'
        
        EXCEPT
        
        SELECT s.name
        FROM students s
        JOIN subjects sub ON s.id = sub.student_id
        WHERE sub.subject = 'Science'
    """)

    print("\n📊 Students Enrolled in Math but NOT in Science:")
    for row in cursor.fetchall():
        print(f"{row[0]}")

    conn.close()

except_students()

def union_students():
    conn = sqlite3.connect("student_records.db")
    cursor = conn.cursor()

    cursor.execute("""
        SELECT s.name
        FROM students s
        JOIN subjects sub ON s.id = sub.student_id
        WHERE sub.subject = 'Math'
        
        UNION
        
        SELECT s.name
        FROM students s
        JOIN subjects sub ON s.id = sub.student_id
        WHERE sub.subject = 'Science'
    """)

    print("\n📊 Students Enrolled in Math OR Science:")
    for row in cursor.fetchall():
        print(f"{row[0]}")

    conn.close()

union_students()

def union_all_students():
    conn = sqlite3.connect("student_records.db")
    cursor = conn.cursor()

    cursor.execute("""
        SELECT s.name, sub.subject
        FROM students s
        JOIN subjects sub ON s.id = sub.student_id
        WHERE sub.subject = 'Math'
        
        UNION ALL
        
        SELECT s.name, sub.subject
        FROM students s
        JOIN subjects sub ON s.id = sub.student_id
        WHERE sub.subject = 'Science'
    """)

    print("\n📊 Students Enrolled in Math OR Science (with duplicates):")
    for row in cursor.fetchall():
        print(f"{row[0]} | Subject: {row[1]}")

    conn.close()

union_all_students()
