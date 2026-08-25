import sqlite3
import matplotlib.pyplot as plt

def subject_avg_chart():
    conn = sqlite3.connect("student_records.db")
    cursor = conn.cursor()

    cursor.execute("""
        SELECT sub.subject, AVG(sub.grade) AS avg_grade
        FROM subjects sub
        GROUP BY sub.subject
    """)

    results = cursor.fetchall()
    subjects = [row[0] for row in results]
    averages = [row[1] for row in results]

    plt.bar(subjects, averages, color="skyblue")
    plt.title("Average Grades per Subject")
    plt.xlabel("Subjects")
    plt.ylabel("Average Grade")
    plt.show()

    conn.close()

subject_avg_chart()

import sqlite3
import matplotlib.pyplot as plt

def percentile_distribution_plot():
    conn = sqlite3.connect("student_records.db")
    cursor = conn.cursor()

    cursor.execute("""
        SELECT sub.subject,
               sub.grade,
               CAST(100.0 *
                    RANK() OVER (
                        PARTITION BY sub.subject
                        ORDER BY sub.grade DESC
                    )
                    / COUNT(*) OVER (PARTITION BY sub.subject)
               AS INT) AS percentile
        FROM subjects sub
        JOIN students s ON s.id = sub.student_id
    """)

    results = cursor.fetchall()
    subjects = [row[0] for row in results]
    percentiles = [row[2] for row in results]

    plt.figure(figsize=(8,5))
    plt.plot(subjects, percentiles, marker="o", linestyle="--", color="green")
    plt.title("Percentile Distribution per Subject")
    plt.xlabel("Subjects")
    plt.ylabel("Percentile Rank (%)")
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()

    conn.close()

percentile_distribution_plot()

import sqlite3
import matplotlib.pyplot as plt

def combined_dashboard():
    conn = sqlite3.connect("student_records.db")
    cursor = conn.cursor()

    # Query averages
    cursor.execute("""
        SELECT sub.subject, AVG(sub.grade) AS avg_grade
        FROM subjects sub
        GROUP BY sub.subject
    """)
    avg_results = cursor.fetchall()
    subjects = [row[0] for row in avg_results]
    averages = [row[1] for row in avg_results]

    # Query percentiles
    cursor.execute("""
        SELECT sub.subject,
               CAST(100.0 *
                    RANK() OVER (
                        PARTITION BY sub.subject
                        ORDER BY sub.grade DESC
                    )
                    / COUNT(*) OVER (PARTITION BY sub.subject)
               AS INT) AS percentile
        FROM subjects sub
        JOIN students s ON s.id = sub.student_id
    """)
    perc_results = cursor.fetchall()
    perc_subjects = [row[0] for row in perc_results]
    percentiles = [row[1] for row in perc_results]

    # Plot combined dashboard
    fig, ax1 = plt.subplots(figsize=(9,6))

    # Bar chart for averages
    ax1.bar(subjects, averages, color="skyblue", label="Average Grade")
    ax1.set_xlabel("Subjects")
    ax1.set_ylabel("Average Grade", color="blue")
    ax1.tick_params(axis="y", labelcolor="blue")

    # Line plot for percentiles
    ax2 = ax1.twinx()
    ax2.plot(perc_subjects, percentiles, marker="o", linestyle="--", color="green", label="Percentile")
    ax2.set_ylabel("Percentile Rank (%)", color="green")
    ax2.tick_params(axis="y", labelcolor="green")

    plt.title("Combined Dashboard: Averages + Percentiles")
    fig.tight_layout()
    plt.show()

    conn.close()

combined_dashboard()
