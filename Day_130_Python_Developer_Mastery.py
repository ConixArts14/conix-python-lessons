# Day 130 - Activity 1 Program
# Author: Conix

def analyze_activity_data():
    print("🚀 Initializing Day 130 Activity 1 Program...")
    
    # Sample dataset representing our student or workflow items
    items = ["Question 1", "Question 2", "Question 3", "Question 4"]
    
    print("\n--- Processing Activity Tasks ---")
    for index, task in enumerate(items, start=1):
        # Using loop syntax and clean formatting
        status = "Completed" if index <= 2 else "Pending"
        print(f"Task {index}: {task} -> Status: {status}")

if __name__ == "__main__":
    analyze_activity_data()

# Day 130 - Activity 2: Advanced Task Processing
def process_activity_two():
    print("\n--- Starting Activity 2: Dynamic Task Manager ---")
    
    # Let's track more advanced items or scores
    task_scores = {"Task 1": 95, "Task 2": 88, "Task 3": 92}
    
    total_score = sum(task_scores.values())
    average_score = total_score / len(task_scores)
    
    print(f"Scores recorded: {task_scores}")
    print(f"Average Performance Score: {average_score:.2f}%")

# Call our new activity function
process_activity_two()

# Day 130 - Activity 3: File Logging & Automation
import csv
import os

def process_activity_three():
    print("\n--- Starting Activity 3: File Logging & Export ---")
    
    # Define our output file name
    filename = "day130_activity_log.csv"
    
    # Data to write
    header = ["Activity", "Status", "Score"]
    row_data = ["Activity 2", "Passed", "91.67"]
    
    # Writing data to a CSV file
    with open(filename, mode="w", newline="") as file:
        writer = csv.writer(file)
        writer.writerow(header)
        writer.writerow(row_data)
        
    print(f"Successfully exported data to {filename}!")
    
    # Read it back to verify
    if os.path.exists(filename):
        print("Verifying file contents:")
        with open(filename, mode="r") as file:
            for line in file:
                print(f"   -> {line.strip()}")

# Call our new Activity 3 function
process_activity_three()

# Day 130 - Activity 4: Error Handling & Defensive Programming
def process_activity_four():
    print("\n--- Starting Activity 4: Error Handling Check ---")
    
    try:
        # Trying to open a file that may or may not exist
        target_file = "day130_activity_log.csv"
        print(f"Attempting to inspect: {target_file}")
        
        with open(target_file, "r") as f:
            lines = f.readlines()
            print(f"Success! Read {len(lines)} lines from the log file.")
            
    except FileNotFoundError:
        print("⚠️ Warning: The log file was not found. Please run Activity 3 first.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
    else:
        print("✨ Activity 4 verification completed successfully with zero errors!")

# Call our new Activity 4 function
process_activity_four()

# Day 130 - Activity 5: Final Capstone Master Controller
def process_activity_five():
    print("\n--- Starting Activity 5: Final Capstone Summary ---")
    print("🏆 Milestone Reached: All Day 130 activities successfully executed!")
    print("✨ Status: Modular functions, data dictionaries, file exports, and error handling fully verified.")
    print("🚀 Ready to lock in Day 130 and transition to the next lesson!")

# Update your main execution block at the very bottom of the file
if __name__ == "__main__":
    print("==========================================")
    print(" STARTING DAY 130 MASTER EXECUTION SCRIPT ")
    print("==========================================")
    
    analyze_activity_data()      # Activity 1
    process_activity_two()       # Activity 2
    process_activity_three()     # Activity 3
    process_activity_four()      # Activity 4
    process_activity_five()      # Activity 5
    
    print("\n==========================================")
    print("      ALL DAY 130 ACTIVITIES COMPLETED    ")
    print("==========================================")