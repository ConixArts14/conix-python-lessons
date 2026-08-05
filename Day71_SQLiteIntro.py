import sqlite3

# Connect to database (creates file if not exists)
conn = sqlite3.connect("student_records.db")

# Create a cursor to execute SQL commands
cursor = conn.cursor()

# Create a table for students
cursor.execute("""
CREATE TABLE IF NOT EXISTS students (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    grade INTEGER NOT NULL
)
""")

conn.commit()
print("✅ Database connected and students table created.")

# Close connection
conn.close()


import sqlite3

# Connect to database
conn = sqlite3.connect("student_records.db")
cursor = conn.cursor()

# --- CREATE ---
cursor.execute("INSERT INTO students (name, grade) VALUES (?, ?)", ("Charlie", 88))
conn.commit()
print("✅ Record created: Charlie, 88")

# --- READ ---
cursor.execute("SELECT * FROM students")
rows = cursor.fetchall()
print("📖 Current Records:")
for row in rows:
    print(row)

# --- UPDATE ---
cursor.execute("UPDATE students SET grade = ? WHERE name = ?", (95, "Charlie"))
conn.commit()
print("✏️ Updated Charlie's grade to 95")

# --- DELETE ---
cursor.execute("DELETE FROM students WHERE name = ?", ("Charlie",))
conn.commit()
print("🗑️ Deleted Charlie's record")

# Close connection
conn.close()


import sqlite3

def connect_db():
    return sqlite3.connect("student_records.db")

def add_student(name, grade):
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute("INSERT INTO students (name, grade) VALUES (?, ?)", (name, grade))
    conn.commit()
    conn.close()
    print(f"✅ Added {name} with grade {grade}")

def view_students():
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM students")
    rows = cursor.fetchall()
    conn.close()
    print("📖 Student Records:")
    for row in rows:
        print(row)

def update_student(name, new_grade):
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute("UPDATE students SET grade = ? WHERE name = ?", (new_grade, name))
    conn.commit()
    conn.close()
    print(f"✏️ Updated {name}'s grade to {new_grade}")

def delete_student(name):
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM students WHERE name = ?", (name,))
    conn.commit()
    conn.close()
    print(f"🗑️ Deleted {name}'s record")

# --- Menu Loop ---
while True:
    print("\n--- Student Database Menu ---")
    print("1. Add Record")
    print("2. View Records")
    print("3. Update Record")
    print("4. Delete Record")
    print("5. Exit")

    choice = input("Enter choice (1-5): ")

    if choice == "1":
        name = input("Enter student name: ")
        grade = int(input("Enter grade: "))
        add_student(name, grade)
    elif choice == "2":
        view_students()
    elif choice == "3":
        name = input("Enter student name to update: ")
        grade = int(input("Enter new grade: "))
        update_student(name, grade)
    elif choice == "4":
        name = input("Enter student name to delete: ")
        delete_student(name)
    elif choice == "5":
        print("👋 Exiting program...")
        break
    else:
        print("⚠️ Invalid choice, try again.")


import sqlite3

def connect_db():
    return sqlite3.connect("student_records.db")

def add_student(name, grade):
    try:
        conn = connect_db()
        cursor = conn.cursor()
        cursor.execute("INSERT INTO students (name, grade) VALUES (?, ?)", (name, grade))
        conn.commit()
        print(f"✅ Added {name} with grade {grade}")
    except Exception as e:
        print(f"⚠️ Error adding student: {e}")
    finally:
        conn.close()

def view_students():
    try:
        conn = connect_db()
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM students")
        rows = cursor.fetchall()
        if rows:
            print("📖 Student Records:")
            for row in rows:
                print(row)
        else:
            print("⚠️ No records found.")
    except Exception as e:
        print(f"⚠️ Error viewing students: {e}")
    finally:
        conn.close()

def update_student(name, new_grade):
    try:
        conn = connect_db()
        cursor = conn.cursor()
        cursor.execute("UPDATE students SET grade = ? WHERE name = ?", (new_grade, name))
        if cursor.rowcount == 0:
            print(f"⚠️ No student named {name} found.")
        else:
            print(f"✏️ Updated {name}'s grade to {new_grade}")
        conn.commit()
    except Exception as e:
        print(f"⚠️ Error updating student: {e}")
    finally:
        conn.close()

def delete_student(name):
    try:
        conn = connect_db()
        cursor

while True:
    print("\n--- Student Database Menu ---")
    print("1. Add Record")
    print("2. View Records")
    print("3. Update Record")
    print("4. Delete Record")
    print("5. Exit")

    choice = input("Enter choice (1-5): ")

    if choice == "1":
        name = input("Enter student name: ")
        try:
            grade = int(input("Enter grade: "))
            add_student(name, grade)
        except ValueError:
            print("⚠️ Invalid grade. Please enter a number.")
    elif choice == "2":
        view_students()
    elif choice == "3":
        name = input("Enter student name to update: ")
        try:
            grade = int(input("Enter new grade: "))
            update_student(name, grade)
        except ValueError:
            print("⚠️ Invalid grade. Please enter a number.")
    elif choice == "4":
        name = input("Enter student name to delete: ")
        delete_student(name)
    elif choice == "5":
        print("👋 Exiting program...")
        break
    else:
        print("⚠️ Invalid choice, try again.")


def filter_students(min_grade):
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM students WHERE grade >= ?", (min_grade,))
    rows = cursor.fetchall()
    conn.close()
    print(f"📊 Students with grade >= {min_grade}:")
    for row in rows:
        print(row)

def sort_students():
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM students ORDER BY grade DESC")
    rows = cursor.fetchall()
    conn.close()
    print("📈 Students sorted by grade (high → low):")
    for row in rows:
        print(row)

def search_student(name):
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM students WHERE name = ?", (name,))
    rows = cursor.fetchall()
    conn.close()
    if rows:
        print(f"🔍 Search results for {name}:")
        for row in rows:
            print(row)
    else:
        print(f"⚠️ No student named {name} found.")


while True:
    print("\n--- Student Database Menu ---")
    print("1. Add Record")
    print("2. View Records")
    print("3. Update Record")
    print("4. Delete Record")
    print("5. Filter Records")
    print("6. Sort Records")
    print("7. Search Records")
    print("8. Exit")

    choice = input("Enter choice (1-8): ")

    if choice == "5":
        try:
            min_grade = int(input("Enter minimum grade: "))
            filter_students(min_grade)
        except ValueError:
            print("⚠️ Invalid grade. Please enter a number.")
    elif choice == "6":
        sort_students()
    elif choice == "7":
        name = input("Enter student name to search: ")
        search_student(name)
    elif choice == "8":
        print("👋 Exiting program...")
        break
    # keep your earlier options (1–4) here
