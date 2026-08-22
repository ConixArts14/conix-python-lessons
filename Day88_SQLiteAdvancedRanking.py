import sqlite3

def ntile_quartiles():
    conn = sqlite3.connect("student_records.db")
    cursor = conn.cursor()

    cursor.execute("""
        SELECT s.name, sub.subject, sub.grade,
               NTILE(4) OVER (
                   PARTITION BY sub.subject 
                   ORDER BY sub.grade DESC
               ) AS quartile
        FROM students s
        JOIN subjects sub ON s.id = sub.student_id
    """)

    print("\n📊 NTILE Quartiles per Subject:")
    for row in cursor.fetchall():
        print(f"{row[0]} | Subject: {row[1]} | Grade: {row[2]} | Quartile: {row[3]}")

    conn.close()

ntile_quartiles()

def percentile_ranks():
    conn = sqlite3.connect("student_records.db")
    cursor = conn.cursor()

    cursor.execute("""
        SELECT s.name, sub.subject, sub.grade,
               CAST(100.0 * 
                    RANK() OVER (
                        PARTITION BY sub.subject 
                        ORDER BY sub.grade DESC
                    ) 
                    / COUNT(*) OVER (PARTITION BY sub.subject) 
               AS INT) AS percentile
        FROM students s
        JOIN subjects sub ON s.id = sub.student_id
    """)

    print("\n📊 Percentile Ranks per Subject:")
    for row in cursor.fetchall():
        print(f"{row[0]} | Subject: {row[1]} | Grade: {row[2]} | Percentile: {row[3]}%")

    conn.close()

percentile_ranks()

def buckets_with_percentiles():
    conn = sqlite3.connect("student_records.db")
    cursor = conn.cursor()

    cursor.execute("""
        SELECT s.name, sub.subject, sub.grade,
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
               AS INT) AS percentile
        FROM students s
        JOIN subjects sub ON s.id = sub.student_id
    """)

    print("\n📊 Buckets with Percentiles per Subject:")
    for row in cursor.fetchall():
        print(f"{row[0]} | Subject: {row[1]} | Grade: {row[2]} | Quartile: {row[3]} | Percentile: {row[4]}%")

    conn.close()

buckets_with_percentiles()

def distribution_reports():
    conn = sqlite3.connect("student_records.db")
    cursor = conn.cursor()

    cursor.execute("""
        SELECT s.name, sub.subject, sub.grade,
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
               ) AS subject_avg
        FROM students s
        JOIN subjects sub ON s.id = sub.student_id
    """)

    print("\n📊 Distribution Report per Subject:")
    for row in cursor.fetchall():
        print(f"{row[0]} | Subject: {row[1]} | Grade: {row[2]} | Quartile: {row[3]} | Percentile: {row[4]}% | Subject Avg: {row[5]:.2f}")

    conn.close()

distribution_reports()
