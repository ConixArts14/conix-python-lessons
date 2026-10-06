# Day 131 - Activity 1: Object-Oriented Fundamentals
# Author: Conix

class TaskManager:
    def __init__(self, project_name):
        self.project_name = project_name
        self.tasks = []

    def add_task(self, task_name):
        self.tasks.append(task_name)
        print(f"[{self.project_name}] Added task: '{task_name}'")

    def display_tasks(self):
        print(f"\n--- Current Tasks for {self.project_name} ---")
        for index, task in enumerate(self.tasks, start=1):
            print(f"Task {index}: {task}")

if __name__ == "__main__":
    print("🚀 Initializing Day 131 Activity 1 Program...")
    manager = TaskManager("Python Mastery Day 131")
    manager.add_task("Initialize Class Structure")
    manager.add_task("Implement Methods")
    manager.display_tasks()

def remove_task(self, task_name):
        if task_name in self.tasks:
            self.tasks.remove(task_name)
            print(f"[{self.project_name}] Removed task: '{task_name}'")
        else:
            print(f"[{self.project_name}] Task '{task_name}' not found.")

if __name__ == "__main__":
    print("🚀 Initializing Day 131 Activity 2 Program...")
    manager = TaskManager("Python Mastery Day 131")
    manager.add_task("Initialize Class Structure")
    manager.add_task("Implement Methods")
    manager.display_tasks()
    
    # Testing Activity 2 removal feature
    print("\n--- Testing Task Removal ---")
    manager.remove_task("Initialize Class Structure")
    manager.display_tasks()

# Day 131 - Activity 1, 2, & 3: Object-Oriented Task Manager with File Export
# Author: Conix

import json

class TaskManager:
    def __init__(self, project_name):
        self.project_name = project_name
        self.tasks = []

    def add_task(self, task_name):
        self.tasks.append(task_name)
        print(f"[{self.project_name}] Added task: '{task_name}'")

    def display_tasks(self):
        print(f"\n--- Current Tasks for {self.project_name} ---")
        for index, task in enumerate(self.tasks, start=1):
            print(f"Task {index}: {task}")

    def remove_task(self, task_name):
        if task_name in self.tasks:
            self.tasks.remove(task_name)
            print(f"[{self.project_name}] Removed task: '{task_name}'")
        else:
            print(f"[{self.project_name}] Task '{task_name}' not found.")

    def export_tasks_to_file(self, filename="day131_tasks.json"):
        # Activity 3: Exporting class data to a JSON file
        data = {
            "project_name": self.project_name,
            "tasks": self.tasks
        }
        with open(filename, "w") as f:
            json.dump(data, f, indent=4)
        print(f"\n[{self.project_name}] Successfully exported tasks to {filename}!")

if __name__ == "__main__":
    print("🚀 Initializing Day 131 Master Program...")
    manager = TaskManager("Python Mastery Day 131")
    
    # Adding tasks
    manager.add_task("Initialize Class Structure")
    manager.add_task("Implement Methods")
    manager.display_tasks()
    
    # Testing removal (Activity 2)
    print("\n--- Testing Task Removal ---")
    manager.remove_task("Initialize Class Structure")
    manager.display_tasks()
    
    # Testing file export (Activity 3)
    manager.export_tasks_to_file()

def load_tasks_from_file(self, filename="day131_tasks.json"):
        # Activity 4: Robust file loading with error handling
        try:
            with open(filename, "r") as f:
                data = json.load(f)
                self.project_name = data.get("project_name", self.project_name)
                self.tasks = data.get("tasks", [])
            print(f"\n[{self.project_name}] Successfully loaded tasks from {filename}!")
        except FileNotFoundError:
            print(f"\n⚠️ Warning: The file '{filename}' was not found. Please export tasks first.")
        except json.JSONDecodeError:
            print(f"\n⚠️ Error: Failed to decode JSON from '{filename}'. File might be corrupted.")
        except Exception as e:
            print(f"\n⚠️ An unexpected error occurred: {e}")

if __name__ == "__main__":
    print("🚀 Initializing Day 131 Master Program...")
    manager = TaskManager("Python Mastery Day 131")
    
    # Adding tasks
    manager.add_task("Initialize Class Structure")
    manager.add_task("Implement Methods")
    manager.display_tasks()
    
    # Testing removal (Activity 2)
    print("\n--- Testing Task Removal ---")
    manager.remove_task("Initialize Class Structure")
    manager.display_tasks()
    
    # Testing file export (Activity 3)
    manager.export_tasks_to_file()
    
    # Testing error handling load (Activity 4)
    print("\n--- Testing Safe File Load ---")
    manager.load_tasks_from_file()

    def generate_summary_report(self):
        # Activity 5: Final capstone report generator
        print("\n" + "="*45)
        print(f" 📊 CAPSTONE SUMMARY REPORT: {self.project_name}")
        print("="*45)
        print(f" Total Active Tasks: {len(self.tasks)}")
        for i, task in enumerate(self.tasks, 1):
            print(f"   {i}. {task}")
        print(" Status: Object-Oriented Class, JSON Persistence, & Error Handling Verified.")
        print("="*45)

if __name__ == "__main__":
    print("🚀 Initializing Day 131 Final Master Program...")
    manager = TaskManager("Python Mastery Day 131")
    
    # 1. Add tasks
    manager.add_task("Initialize Class Structure")
    manager.add_task("Implement Methods")
    manager.add_task("Build File Export & Import")
    manager.display_tasks()
    
    # 2. Test removal (Activity 2)
    print("\n--- Testing Task Removal ---")
    manager.remove_task("Initialize Class Structure")
    
    # 3. Test file export (Activity 3)
    manager.export_tasks_to_file()
    
    # 4. Test safe file load with error handling (Activity 4)
    print("\n--- Testing Safe File Load ---")
    manager.load_tasks_from_file()
    
    # 5. Generate final capstone summary (Activity 5)
    manager.generate_summary_report()