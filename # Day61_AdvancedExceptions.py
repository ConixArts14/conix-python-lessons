try:
    age = int(input("Enter age: "))
    if age <= 0:
        raise ValueError("Age must be greater than 0.")
except ValueError as e:
    print("Invalid input:", e)
except FileNotFoundError:
    print("Student file not found.")
try:
    choice = int(input("Enter menu choice: "))
    if choice not in range(0, 10):
        raise ValueError("Choice must be between 0 and 9.")
except (ValueError, TypeError) as e:
    print("Invalid choice:", e)
try:
    file = open("students.json", "r")
    students = json.load(file)
except FileNotFoundError:
    print("No student records found.")
finally:
    print("Closing program safely...")

import logging
logging.basicConfig(filename="error_log.txt", level=logging.ERROR)
try:
    age = int(input("Enter age: "))
    if age <= 0:
        raise ValueError("Age must be greater than 0.")
except ValueError as e:
    print("Invalid input:", e)
    logging.error("Age input error: %s", e)
