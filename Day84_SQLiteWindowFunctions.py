import sqlite3

def row_number_students():
    conn = sqlite3.connect("student_records.db")
    cursor = conn.cursor()

    cursor.execute("""
        SELECT s.name, sub.subject, sub.grade,
               ROW_NUMBER() OVER (ORDER BY sub.grade DESC) AS row_num
        FROM students s
        JOIN subjects sub ON s.id = sub.student_id
    """)

    print("\n📊 Students Ranked by Grade (ROW_NUMBER):")
    for row in cursor.fetchall():
        print(f"Rank {row[3]} | {row[0]} | Subject: {row[1]} | Grade: {row[2]}")

    conn.close()

row_number_students()

def rank_students():
    conn = sqlite3.connect("student_records.db")
    cursor = conn.cursor()

    cursor.execute("""
        SELECT s.name, sub.subject, sub.grade,
               RANK() OVER (ORDER BY sub.grade DESC) AS rank_pos
        FROM students s
        JOIN subjects sub ON s.id = sub.student_id
    """)

    print("\n📊 Students Ranked by Grade (RANK):")
    for row in cursor.fetchall():
        print(f"Rank {row[3]} | {row[0]} | Subject: {row[1]} | Grade: {row[2]}")

    conn.close()

rank_students()

def dense_rank_students():
    conn = sqlite3.connect("student_records.db")
    cursor = conn.cursor()

    cursor.execute("""
        SELECT s.name, sub.subject, sub.grade,
               DENSE_RANK() OVER (ORDER BY sub.grade DESC) AS dense_rank_pos
        FROM students s
        JOIN subjects sub ON s.id = sub.student_id
    """)

    print("\n📊 Students Ranked by Grade (DENSE_RANK):")
    for row in cursor.fetchall():
        print(f"Dense Rank {row[3]} | {row[0]} | Subject: {row[1]} | Grade: {row[2]}")

    conn.close()

dense_rank_students()

def combined_window_functions():
    conn = sqlite3.connect("student_records.db")
    cursor = conn.cursor()

    cursor.execute("""
        SELECT s.name, sub.subject, sub.grade,
               ROW_NUMBER() OVER (ORDER BY sub.grade DESC) AS row_num,
               RANK() OVER (ORDER BY sub.grade DESC) AS rank_pos,
               DENSE_RANK() OVER (ORDER BY sub.grade DESC) AS dense_rank_pos
        FROM students s
        JOIN subjects sub ON s.id = sub.student_id
    """)

    print("\n📊 Students Ranked by Grade (ROW_NUMBER, RANK, DENSE_RANK):")
    for row in cursor.fetchall():
        print(f"RowNum {row[3]} | Rank {row[4]} | DenseRank {row[5]} | {row[0]} | Subject: {row[1]} | Grade: {row[2]}")

    conn.close()

combined_window_functions()
