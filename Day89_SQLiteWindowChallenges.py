import sqlite3

def mixed_window_challenge():
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
               NTILE(4) OVER (
                   PARTITION BY sub.subject 
                   ORDER BY sub.grade DESC
               ) AS quartile,
               CAST(100.0 * 
                    RANK() OVER (
                        PARTITION BY sub.subject 
                        ORDER BY sub.grade DESC
                    ) 
                    / COUNT(*) OVER (PARTITION BY sub.subject) 
               AS INT) AS percentile,
               AVG(sub.grade) OVER (
                   PARTITION BY sub.subject 
                   ORDER BY sub.grade 
                   ROWS BETWEEN 2 PRECEDING AND CURRENT ROW
               ) AS rolling_avg
        FROM students s
        JOIN subjects sub ON s.id = sub.student_id
    """)

    print("\n📊 Mixed Window Challenge Report:")
    for row in cursor.fetchall():
        print(f"{row[0]} | Subject: {row[1]} | Grade: {row[2]} | Row#: {row[3]} | RANK: {row[4]} | DENSE_RANK: {row[5]} | Quartile: {row[6]} | Percentile: {row[7]}% | Rolling Avg: {row[8]:.2f}")

    conn.close()

mixed_window_challenge()

def custom_challenge_queries():
    conn = sqlite3.connect("student_records.db")
    cursor = conn.cursor()

    cursor.execute("""
        SELECT s.name, sub.subject, sub.grade,
               RANK() OVER (
                   PARTITION BY sub.subject 
                   ORDER BY sub.grade DESC
               ) AS rank_pos,
               NTILE(3) OVER (
                   PARTITION BY sub.subject 
                   ORDER BY sub.grade DESC
               ) AS tercile,
               AVG(sub.grade) OVER (
                   PARTITION BY sub.subject 
                   ROWS BETWEEN 1 PRECEDING AND 1 FOLLOWING
               ) AS local_avg
        FROM students s
        JOIN subjects sub ON s.id = sub.student_id
        WHERE sub.grade >= 75
    """)

    print("\n📊 Custom Challenge Report (Passing Grades Only):")
    for row in cursor.fetchall():
        print(f"{row[0]} | Subject: {row[1]} | Grade: {row[2]} | Rank: {row[3]} | Tercile: {row[4]} | Local Avg: {row[5]:.2f}")

    conn.close()

custom_challenge_queries()

def challenge_leaderboards():
    conn = sqlite3.connect("student_records.db")
    cursor = conn.cursor()

    cursor.execute("""
        SELECT s.name, sub.subject, sub.grade,
               RANK() OVER (
                   PARTITION BY sub.subject 
                   ORDER BY sub.grade DESC
               ) AS rank_pos,
               NTILE(5) OVER (
                   PARTITION BY sub.subject 
                   ORDER BY sub.grade DESC
               ) AS quintile,
               AVG(sub.grade) OVER (
                   PARTITION BY sub.subject
               ) AS subject_avg
        FROM students s
        JOIN subjects sub ON s.id = sub.student_id
        WHERE sub.grade >= 80
    """)

    print("\n📊 Challenge Leaderboards (Grades ≥ 80):")
    for row in cursor.fetchall():
        print(f"{row[0]} | Subject: {row[1]} | Grade: {row[2]} | Rank: {row[3]} | Quintile: {row[4]} | Subject Avg: {row[5]:.2f}")

    conn.close()

challenge_leaderboards()

def final_challenge_report():
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
               NTILE(4) OVER (
                   PARTITION BY sub.subject 
                   ORDER BY sub.grade DESC
               ) AS quartile,
               CAST(100.0 * 
                    RANK() OVER (
                        PARTITION BY sub.subject 
                        ORDER BY sub.grade DESC
                    ) 
                    / COUNT(*) OVER (PARTITION BY sub.subject) 
               AS INT) AS percentile,
               AVG(sub.grade) OVER (
                   PARTITION BY sub.subject
                   ROWS BETWEEN 2 PRECEDING AND CURRENT ROW
               ) AS rolling_avg,
               AVG(sub.grade) OVER (
                   PARTITION BY sub.subject
               ) AS subject_avg
        FROM students s
        JOIN subjects sub ON s.id = sub.student_id
        WHERE sub.grade >= 70
    """)

    print("\n📊 Final Challenge Report (Grades ≥ 70):")
    for row in cursor.fetchall():
        print(f"{row[0]} | Subject: {row[1]} | Grade: {row[2]} | Row#: {row[3]} | RANK: {row[4]} | DENSE_RANK: {row[5]} | Quartile: {row[6]} | Percentile: {row[7]}% | Rolling Avg: {row[8]:.2f} | Subject Avg: {row[9]:.2f}")

    conn.close()

final_challenge_report()
