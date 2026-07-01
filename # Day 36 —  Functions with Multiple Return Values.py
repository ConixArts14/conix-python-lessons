# Day 36 - Functions with Multiple Return Values
# Activity 1: Returning Multiple Values

#def calculate_stats(numbers):
    #total = sum(numbers)
    #average = total / len(numbers)
    #return total, average

# Calling the function
#stats = calculate_stats([10, 20, 30, 40, 50])
#print(stats)   # prints: (100, 25.0)

# Unpacking the values
#total, average = calculate_stats([10, 20, 30, 40,])
#print("Total:", total)   # prints: Total: 100
#print("Average:", average) # prints: Average: 25.0

# Day 36 - Functions with Multiple Return Values
# Activity 2: Returning Multiple Types

#def student_info(name, scores):
    #total = sum(scores)
    #average = total / len(scores)
    #return name, average

# Calling the function
#info = student_info("Conix", [90, 85, 88])
#print(info)  
# prints: ('Conix', 87.666...)

#Unpacking the values
#student_name, avg_score = student_info("Conix", [90, 85, 88])
#print("Name:", student_name)     # prints: Name: Conix
#print("Average Score:", avg_score)  # prints: Average Score: 87.666...

# Day 36 - Functions with Multiple Return Values
# Activity 3: Returning Lists and Tuples Together

#def analyze_numbers(numbers):
    #total = sum(numbers)
    #average = total / len(numbers)
    #extremes = (min(numbers), max(numbers))  # <-- define extremes first
    

# Calling the function
#data, extremes = analyze_numbers([5, 10, 15, 20])
#print("Data:", data)          # prints: Data: [5, 10, 15, 20]
#print("Extremes:", extremes)  # prints: Extremes: (5, 20)

# Day 36 - Functions with Multiple Return Values
# Activity 4: Practical Use Case

def exam_report(scores):
    total = sum(scores)
    average = total / len(scores)
    extremes = (min(scores), max(scores))
    passed = average >= 75
    return total, average, extremes, passed

# Calling the function
report = exam_report([80, 90, 70, 85])
print(report)
# prints: (325, 81.25, (70, 90), True)

# Unpacking
total, average, extremes, passed = exam_report([80, 90, 70, 85])
print("Total:", total)
print("Average:", average)
print("Lowest/Highest:", extremes)
print("Passed:", passed)
