import sqlite3

def row_number_per_subject():
    conn = sqlite3.connect("student_records.db")
    cursor = conn.cursor()

    cursor.execute("""
        SELECT s.name, sub.subject, sub.grade,
               ROW_NUMBER() OVER (
                   PARTITION BY sub.subject 
                   ORDER BY sub.grade DESC
               ) AS row_num
        FROM students s
        JOIN subjects sub ON s.id = sub.student_id
    """)

    print("\n📊 Row Number per Subject (Descending Grades):")
    for row in cursor.fetchall():
        print(f"{row[0]} | Subject: {row[1]} | Grade: {row[2]} | Row#: {row[3]}")

    conn.close()

row_number_per_subject()

def rank_vs_dense_rank():
    conn = sqlite3.connect("student_records.db")
    cursor = conn.cursor()

    cursor.execute("""
        SELECT s.name, sub.subject, sub.grade,
               RANK() OVER (
                   PARTITION BY sub.subject 
                   ORDER BY sub.grade DESC
               ) AS rank_pos,
               DENSE_RANK() OVER (
                   PARTITION BY sub.subject 
                   ORDER BY sub.grade DESC
               ) AS dense_rank_pos
        FROM students s
        JOIN subjects sub ON s.id = sub.student_id
    """)

    print("\n📊 RANK vs DENSE_RANK per Subject:")
    for row in cursor.fetchall():
        print(f"{row[0]} | Subject: {row[1]} | Grade: {row[2]} | RANK: {row[3]} | DENSE_RANK: {row[4]}")

    conn.close()

rank_vs_dense_rank()

def combined_rankings_with_frames():
    conn = sqlite3.connect("student_records.db")
    cursor = conn.cursor()

    cursor.execute("""
        SELECT s.name, sub.subject, sub.grade,
               ROW_NUMBER() OVER (
                   PARTITION BY sub.subject 
                   ORDER BY sub.grade DESC
               ) AS row_num,
               RANK() OVER (
                   PARTITION BY sub.subject 
                   ORDER BY sub.grade DESC
               ) AS rank_pos,
               DENSE_RANK() OVER (
                   PARTITION BY sub.subject 
                   ORDER BY sub.grade DESC
               ) AS dense_rank_pos,
               AVG(sub.grade) OVER (
                   PARTITION BY sub.subject 
                   ORDER BY sub.grade 
                   ROWS BETWEEN 2 PRECEDING AND CURRENT ROW
               ) AS rolling_avg
        FROM students s
        JOIN subjects sub ON s.id = sub.student_id
    """)

    print("\n📊 Combined Rankings with Rolling Average:")
    for row in cursor.fetchall():
        print(f"{row[0]} | Subject: {row[1]} | Grade: {row[2]} | Row#: {row[3]} | RANK: {row[4]} | DENSE_RANK: {row[5]} | Rolling Avg: {row[6]:.2f}")

    conn.close()

combined_rankings_with_frames()

def subject_leaderboards():
    conn = sqlite3.connect("student_records.db")
    cursor = conn.cursor()

    cursor.execute("""
        SELECT s.name, sub.subject, sub.grade,
               RANK() OVER (
                   PARTITION BY sub.subject 
                   ORDER BY sub.grade DESC
               ) AS rank_pos,
               AVG(sub.grade) OVER (
                   PARTITION BY sub.subject 
                   ORDER BY sub.grade 
                   ROWS BETWEEN 2 PRECEDING AND CURRENT ROW
               ) AS rolling_avg
        FROM students s
        JOIN subjects sub ON s.id = sub.student_id
    """)

    print("\n📊 Subject Leaderboards with Rolling Average:")
    for row in cursor.fetchall():
        print(f"{row[0]} | Subject: {row[1]} | Grade: {row[2]} | Rank: {row[3]} | Rolling Avg: {row[4]:.2f}")

    conn.close()

subject_leaderboards()
