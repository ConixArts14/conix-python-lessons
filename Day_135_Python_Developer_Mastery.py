# Day 135 - Activity 1: Task Filtering and Search Interface

class TaskFilter:
    def matches(self, task):
        raise NotImplementedError("Subclasses must implement the matches method.")

class StatusFilter(TaskFilter):
    def __init__(self, is_completed):
        self.is_completed = is_completed

    def matches(self, task):
        # Checks if the task has an 'is_completed' attribute matching our filter
        if hasattr(task, 'is_completed'):
            return task.is_completed == self.is_completed
        return False

if __name__ == "__main__":
    print("🚀 Initializing Day 135 Activity 1 Program...")
    
    # Quick test setup
    from Day_134_Python_Developer_Mastery import ChecklistTask, TextTask
    
    tasks = [
        TextTask("Study advanced Python design patterns"),
        ChecklistTask("Finish Day 135 Activity 1", is_completed=True),
        ChecklistTask("Push changes to GitHub", is_completed=False)
    ]
    
    completed_filter = StatusFilter(is_completed=True)
    
    print("\n--- Filtering Completed Tasks ---")
    for task in tasks:
        if completed_filter.matches(task):
            print(f"Matched: {task.render()}")