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

# Day 135 - Activity 2: Task Filtering and Search Implementation

class TaskFilter:
    def matches(self, task):
        raise NotImplementedError("Subclasses must implement the matches method.")

class StatusFilter(TaskFilter):
    def __init__(self, is_completed):
        self.is_completed = is_completed

    def matches(self, task):
        if hasattr(task, 'is_completed'):
            return task.is_completed == self.is_completed
        return False

class KeywordFilter(TaskFilter):
    def __init__(self, keyword):
        self.keyword = keyword.lower()

    def matches(self, task):
        # Check task title or content for the keyword
        text_to_check = ""
        if hasattr(task, 'title'):
            text_to_check += str(task.title)
        if hasattr(task, 'content'):
            text_to_check += str(task.content)
            
        return self.keyword in text_to_check.lower()

if __name__ == "__main__":
    print("🚀 Initializing Day 135 Activity 2 Program...")
    
    from Day_134_Python_Developer_Mastery import ChecklistTask, TextTask
    
    tasks = [
        TextTask("Study advanced Python design patterns"),
        ChecklistTask("Finish Day 135 Activity 1", is_completed=True),
        ChecklistTask("Push changes to GitHub", is_completed=False)
    ]
    
    keyword_filter = KeywordFilter("Python")
    
    print("\n--- Filtering Tasks by Keyword 'Python' ---")
    for task in tasks:
        if keyword_filter.matches(task):
            print(f"Matched Keyword: {task.render()}")