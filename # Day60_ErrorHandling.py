try:
    age = int(input("Enter age: "))
except ValueError:
    print("Invalid input! Age must be a number.")
try:
    with open("students.json", "r") as file:
        students = json.load(file)
except FileNotFoundError:
    print("No student records found. Please add students first.")
    students = []
try:
    choice = int(input("Enter menu choice: "))
except ValueError:
    print("Invalid choice! Please enter a number.")
    choice = -1


class InvalidAgeError(Exception):
    pass

try:
    age = int(input("Enter age: "))
    if age <= 0:
        raise InvalidAgeError("Age must be greater than 0.")
except ValueError:
    print("Invalid input! Age must be a number.")
except InvalidAgeError as e:
    print(e)
class InvalidChoiceError(Exception):
    pass

try:
    choice = int(input("Enter menu choice: "))
    if choice not in range(0, 10):
        raise InvalidChoiceError("Menu choice must be between 0 and 9.")
except ValueError:
    print("Invalid choice! Please enter a number.")
except InvalidChoiceError as e:
    print(e)
class NoStudentsError(Exception):
    pass

try:
    if len(students) == 0:
        raise NoStudentsError("No students available to export.")
    export_csv(students)
except NoStudentsError as e:
    print(e)
