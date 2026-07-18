# Day 37 - Functions with Multiple Return Values (Advanced)
# Activity 1: Grading System

#def grade_report(name, scores):
#total = sum(scores)
#average = total / len(scores)
#passed = average >= 75
#grade = "Pass" if passed else "Fail"
#return name, total, average, grade

# Calling the function
#report = grade_report("Conix", [85, 90, 78, 88])
#print(report)
# prints: ('Conix', 341, 85.25, 'Pass')

# Unpacking
#student, total, average, grade = grade_report("Conix", [85, 90, 78, 88])
#print("Student:", student)
#print("Total:", total)
#print("Average:", average)
#print("Grade:", grade)

# Day 37 - Functions with Multiple Return Values
# Activity 2: Returning Dictionaries

#def student_report(name, scores):
#total = sum(scores)
#average = total / len(scores)
#grade = "Pass" if average >= 75 else "Fail"
#return {
    #"Name": name,
    #"Total": total,
    #"Average": average,
    #"Grade": grade
}

# Calling the function
#report = student_report("Conix", [85, 90, 78, 88])
#print(report)
# prints: {'Name': 'Conix', 'Total': 341, 'Average': 85.25, 'Grade': 'Pass'}

# Accessing values
#print("Student:", report["Name"])
#print("Average:", report["Average"])
#print("Grade:", report["Grade"])

# Day 37 - Returning Values for Grading System.py

#def student_report(name, scores):
    #total = sum(scores)
    #average = total / len(scores)
    #grade = "Pass" if average >= 75 else "Fail"
    #return {
        #"Name": name,
        #"Total": total,
        #"Grade": grade
        #"Average": average,
        #"Grade": grade
    }  # <-- only ONE closing brace, aligned with return

#report = student_report("Conix", [85, 90, 78, 88])
#print(report)
#print(report["Name"])
#print(report["Average"])
#print(report["Grade"])

#def student_report(name, scores):
    #total = sum(scores)
    #average = total / len(scores)
    #grade = "Pass" if average >= 75 else "Fail"
    #return {
        #"Name": name,
        #"Total": total,
        #"Average": average,
        #"Grade": grade
    }

#def class_database(students):
    #reports = []
    #for name, scores in students.items():
        #reports.append(student_report(name, scores))
    #return reports

# Sample data
#students = {
    #"Conix": [85, 90, 78, 88],
    #"Leonald": [70, 65, 80, 72],
    #"Alex": [95, 92, 89, 96]
}

# Generate database
#database = class_database(students)

# Print each student’s report
#for report in database:
    #
    # print(report)
