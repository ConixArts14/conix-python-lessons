import sqlite3

# Activity 1: Insert with Foreign Keys
def insert_student_with_subject(name, subject, grade):
    conn = sqlite3.connect("student_records.db")
    cursor = conn.cursor()

    # Insert student (only name)
    cursor.execute("INSERT INTO students (name) VALUES (?)", (name,))
    student_id = cursor.lastrowid

    # Insert subject linked to student
    cursor.execute("INSERT INTO subjects (student_id, subject, grade) VALUES (?, ?, ?)",
                   (student_id, subject, grade))

    conn.commit()
    conn.close()

    print(f"\n✅ Added {name} with subject {subject} (Grade: {grade})")

# Example inserts
insert_student_with_subject("Leonald", "Math", 92)
insert_student_with_subject("Leonald", "Science", 88)


# Activity 2: Update with Joins
def update_student_grade(name, subject, new_grade):
    conn = sqlite3.connect("student_records.db")
    cursor = conn.cursor()

    cursor.execute("""
        UPDATE subjects
        SET grade = ?
        WHERE subject = ?
        AND student_id = (
            SELECT id FROM students WHERE name = ?
        )
    """, (new_grade, subject, name))

    conn.commit()
    conn.close()

    print(f"\n✏️ Updated {name}'s grade in {subject} to {new_grade}")

# Example updates
update_student_grade("Leonald", "Science", 95)
update_student_grade("Leonald", "Math", 97)


def delete_student_subject(name, subject):
    conn = sqlite3.connect("student_records.db")
    cursor = conn.cursor()

    cursor.execute("""
        DELETE FROM subjects
        WHERE subject = ?
        AND student_id = (
            SELECT id FROM students WHERE name = ?
        )
    """, (subject, name))

    conn.commit()
    conn.close()

    print(f"\n🗑️ Deleted {subject} record for {name}")
def delete_student(name):
    conn = sqlite3.connect("student_records.db")
    cursor = conn.cursor()

    cursor.execute("DELETE FROM students WHERE name = ?", (name,))

    conn.commit()
    conn.close()

    print(f"\n🗑️ Deleted student {name} and all linked subjects")
delete_student_subject("Leonald", "Science")
# delete_student("Leonald")   # Uncomment if you want to remove Leonald entirely


def menu():
    while True:
        print("\n=== Student Records Menu ===")
        print("1. Insert Student with Subject")
        print("2. Update Student Grade")
        print("3. Delete Student Subject")
        print("4. Delete Student")
        print("5. Exit")

        choice = input("Enter choice (1-5): ")

        if choice == "1":
            name = input("Enter student name: ")
            subject = input("Enter subject: ")
            grade = int(input("Enter grade: "))
            insert_student_with_subject(name, subject, grade)

        elif choice == "2":
            name = input("Enter student name: ")
            subject = input("Enter subject: ")
            new_grade = int(input("Enter new grade: "))
            update_student_grade(name, subject, new_grade)

        elif choice == "3":
            name = input("Enter student name: ")
            subject = input("Enter subject to delete: ")
            delete_student_subject(name, subject)

        elif choice == "4":
            name = input("Enter student name to delete: ")
            delete_student(name)

        elif choice == "5":
            print("\n👋 Exiting menu. Goodbye!")
            break

        else:
            print("\n⚠️ Invalid choice, try again.")
menu()





elif choice == "5":
    print("\n👋 Exiting menu. Goodbye!")
    break
