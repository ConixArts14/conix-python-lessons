# Day 135 - Activity 1: Task Sorting and Ordering Interface

class TaskSorter:
    def sort(self, tasks):
        raise NotImplementedError("Subclasses must implement the sort method.")

class AlphabeticalSorter(TaskSorter):
    def __init__(self, ascending=True):
        self.ascending = ascending

    def sort(self, tasks):
        # Sorts tasks alphabetically based on their title or content attribute
        def get_task_text(task):
            if hasattr(task, 'title'):
                return str(task.title)
            if hasattr(task, 'content'):
                return str(task.content)
            return ""

        return sorted(tasks, key=get_task_text, reverse=not self.ascending)

if __name__ == "__main__":
    print("🚀 Initializing Day 136 Activity 1 Program...")
    
    from Day_134_Python_Developer_Mastery import ChecklistTask, TextTask
    
    tasks = [
        TextTask("Zebra project review"),
        ChecklistTask("Alpha testing setup", is_completed=False),
        TextTask("Beta release notes preparation")
    ]
    
    sorter = AlphabeticalSorter(ascending=True)
    sorted_tasks = sorter.sort(tasks)
    
    print("\n--- Sorting Tasks Alphabetically ---")
    for task in sorted_tasks:
        print(f"Sorted: {task.render()}")

# Day 136 - Activity 2: Priority and Completion Sorting

class TaskSorter:
    def sort(self, tasks):
        raise NotImplementedError("Subclasses must implement the sort method.")

class AlphabeticalSorter(TaskSorter):
    def __init__(self, ascending=True):
        self.ascending = ascending

    def sort(self, tasks):
        def get_task_text(task):
            if hasattr(task, 'title'):
                return str(task.title)
            if hasattr(task, 'content'):
                return str(task.content)
            return ""

        return sorted(tasks, key=get_task_text, reverse=not self.ascending)

class CompletionSorter(TaskSorter):
    def __init__(self, completed_first=True):
        self.completed_first = completed_first

    def sort(self, tasks):
        # Sorts tasks so completed or uncompleted items come first
        def get_completion_status(task):
            if hasattr(task, 'is_completed'):
                return task.is_completed
            return False # Default uncompleted if attribute is missing

        # Sorts by completion status (False comes before True by default)
        return sorted(tasks, key=get_completion_status, reverse=self.completed_first)

if __name__ == "__main__":
    print("🚀 Initializing Day 136 Activity 2 Program...")
    
    from Day_134_Python_Developer_Mastery import ChecklistTask, TextTask
    
    tasks = [
        TextTask("Zebra project review"),
        ChecklistTask("Alpha testing setup", is_completed=True),
        ChecklistTask("Beta release notes preparation", is_completed=False),
        ChecklistTask("Final deployment check", is_completed=True)
    ]
    
    completion_sorter = CompletionSorter(completed_first=False)
    sorted_tasks = completion_sorter.sort(tasks)
    
    print("\n--- Sorting Tasks by Completion (Incomplete First) ---")
    for task in sorted_tasks:
        print(f"Sorted: {task.render()}")