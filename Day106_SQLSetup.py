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

cursor.execute("""
CREATE TABLE IF NOT EXISTS student_report (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT,
    section TEXT
)
""")

cursor.executemany("""
INSERT INTO student_report (name, section) VALUES (?, ?)
""", [
    ("Alice", "A"),
    ("Bob", "B"),
    ("Charlie", "A"),
    ("Diana", "B")
])

import sqlite3

conn = sqlite3.connect("student_records.db")
cursor = conn.cursor()

# Exams table
cursor.execute("""
CREATE TABLE IF NOT EXISTS exams (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    subject TEXT,
    grade INTEGER,
    exam_type TEXT
)
""")

cursor.executemany("""
INSERT INTO exams (subject, grade, exam_type) VALUES (?, ?, ?)
""", [
    ("Math", 85, "Midterm"),
    ("Science", 90, "Final"),
    ("English", 88, "Midterm"),
    ("History", 80, "Final")
])

# Student report table
cursor.execute("""
CREATE TABLE IF NOT EXISTS student_report (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT,
    section TEXT
)
""")

cursor.executemany("""
INSERT INTO student_report (name, section) VALUES (?, ?)
""", [
    ("Alice", "A"),
    ("Bob", "A"),
    ("Charlie", "B"),
    ("Diana", "B")
])

# Commit and close AFTER all tables are created
conn.commit()
conn.close()

import sqlite3

conn = sqlite3.connect("student_records.db")
cursor = conn.cursor()

# Exams table with exam_type included
cursor.execute("""
CREATE TABLE IF NOT EXISTS exams (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    subject TEXT,
    grade INTEGER,
    exam_type TEXT
)
""")

cursor.executemany("""
INSERT INTO exams (subject, grade, exam_type) VALUES (?, ?, ?)
""", [
    ("Math", 85, "Midterm"),
    ("Science", 90, "Final"),
    ("English", 88, "Midterm"),
    ("History", 80, "Final")
])

# Student report table
cursor.execute("""
CREATE TABLE IF NOT EXISTS student_report (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT,
    section TEXT
)
""")

cursor.executemany("""
INSERT INTO student_report (name, section) VALUES (?, ?)
""", [
    ("Alice", "A"),
    ("Bob", "B"),
    ("Charlie", "B"),
    ("Diana", "B")
])

# Commit and close AFTER all tables are created
conn.commit()
conn.close()

import sqlite3

conn = sqlite3.connect("student_records.db")
cursor = conn.cursor()

# Drop old tables to reset schema
cursor.execute("DROP TABLE IF EXISTS exams")
cursor.execute("DROP TABLE IF EXISTS student_report")

# Exams table with exam_type included
cursor.execute("""
CREATE TABLE exams (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    subject TEXT,
    grade TEXT,
    exam_type TEXT
)
""")

cursor.executemany("""
INSERT INTO exams (subject, grade, exam_type) VALUES (?, ?, ?)
""", [
    ("Math", "B", "Midterm"),
    ("Science", "B", "Final"),
    ("English", "B", "Midterm"),
    ("History", "B", "Final")
])

# Student report table
cursor.execute("""
CREATE TABLE student_report (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT,
    section TEXT
)
""")

cursor.executemany("""
INSERT INTO student_report (name, section) VALUES (?, ?)
""", [
    ("Alice", "A"),
    ("Bob", "B"),
    ("Charlie", "B"),
    ("Diana", "B")
])

# Commit and close AFTER all tables are created
conn.commit()
conn.close()

import sqlite3

conn = sqlite3.connect("student_records.db")
cursor = conn.cursor()

# Drop old tables to reset schema
cursor.execute("DROP TABLE IF EXISTS exams")
cursor.execute("DROP TABLE IF EXISTS student_report")

# Exams table with exam_type included
cursor.execute("""
CREATE TABLE exams (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    subject TEXT,
    grade TEXT,
    exam_type TEXT
)
""")

cursor.executemany("""
INSERT INTO exams (subject, grade, exam_type) VALUES (?, ?, ?)
""", [
    ("Math", "B", "Midterm"),
    ("Science", "B", "Final"),
    ("English", "A", "Midterm"),
    ("History", "B", "Final")
])

# Student report table
cursor.execute("""
CREATE TABLE student_report (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT,
    section TEXT
)
""")

cursor.executemany("""
INSERT INTO student_report (name, section) VALUES (?, ?)
""", [
    ("Alice", "A"),
    ("Bob", "B"),
    ("Charlie", "B"),
    ("Diana", "A")
])

# Commit and close AFTER all tables are created
conn.commit()
conn.close()
