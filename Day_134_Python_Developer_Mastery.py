# Day 134 - Activity 1: Polymorphism Fundamentals & Base Interface
# Author: Conix

class TaskComponent:
    def render(self):
        raise NotImplementedError("Subclasses must implement this abstract method.")

class TextTask(TaskComponent):
    def __init__(self, content):
        self.content = content

    def render(self):
        return f"📝 Text Task: {self.content}"

if __name__ == "__main__":
    print("🚀 Initializing Day 134 Activity 1 Program...")
    task = TextTask("Complete Python Developer Mastery lessons")
    print(task.render())

class ChecklistTask(TaskComponent):
    def __init__(self, title, is_completed=False):
        self.title = title
        self.is_completed = is_completed

    def render(self):
        status = "☑" if self.is_completed else "☐"
        return f"{status} Checklist: {self.title}"

if __name__ == "__main__":
    print("🚀 Initializing Day 134 Activity 2 Program...")
    
    # Create a list of different task components (Polymorphism)
    tasks = [
        TextTask("Complete Python Developer Mastery lessons"),
        ChecklistTask("Master Polymorphism & Interfaces", is_completed=True),
        ChecklistTask("Build final capstone project", is_completed=False)
    ]
    
    print("\n--- Rendering Polymorphic Tasks ---")
    for task in tasks:
        print(task.render())

class ProjectSection(TaskComponent):
    def __init__(self, title):
        self.title = title
        self.children = []

    def add(self, component):
        self.children.append(component)

    def render(self):
        result = [f"📂 Section: {self.title}"]
        for child in self.children:
            # Indent child rendering for clean hierarchy
            child_output = child.render()
            result.append(f"    {child_output}")
        return "\n".join(result)

if __name__ == "__main__":
    print("🚀 Initializing Day 134 Activity 3 Program...")
    
    # Create a structured project section containing mixed task components
    day3_section = ProjectSection("Day 134 Goals")
    day3_section.add(TextTask("Understand Polymorphism & Interfaces"))
    day3_section.add(ChecklistTask("Implement Base Interface", is_completed=True))
    day3_section.add(ChecklistTask("Build Composite Pattern Section", is_completed=True))
    
    print("\n--- Rendering Composite Section ---")
    print(day3_section.render())

# Update TaskComponent to include a dictionary conversion method
class TaskComponent:
    def render(self):
        raise NotImplementedError("Subclasses must implement this abstract method.")
        
    def to_dict(self):
        raise NotImplementedError("Subclasses must implement to_dict().")

class TextTask(TaskComponent):
    def __init__(self, content):
        self.content = content

    def render(self):
        return f"📝 Text Task: {self.content}"

    def to_dict(self):
        return {"type": "TextTask", "content": self.content}

class ChecklistTask(TaskComponent):
    def __init__(self, title, is_completed=False):
        self.title = title
        self.is_completed = is_completed

    def render(self):
        status = "☑" if self.is_completed else "☐"
        return f"{status} Checklist: {self.title}"

    def to_dict(self):
        return {"type": "ChecklistTask", "title": self.title, "is_completed": self.is_completed}

class ProjectSection(TaskComponent):
    def __init__(self, title):
        self.title = title
        self.children = []

    def add(self, component):
        self.children.append(component)

    def render(self):
        result = [f"📂 Section: {self.title}"]
        for child in self.children:
            child_output = child.render()
            result.append(f"    {child_output}")
        return "\n".join(result)

    def to_dict(self):
        return {
            "type": "ProjectSection",
            "title": self.title,
            "children": [child.to_dict() for child in self.children]
        }

    def export_to_json(self, filename="day134_project.json"):
        import json
        with open(filename, "w") as f:
            json.dump(self.to_dict(), f, indent=4)
        print(f"\n[{self.title}] Successfully exported composite structure to {filename}!")

if __name__ == "__main__":
    print("🚀 Initializing Day 134 Activity 4 Program...")
    
    day3_section = ProjectSection("Day 134 Goals")
    day3_section.add(TextTask("Understand Polymorphism & Interfaces"))
    day3_section.add(ChecklistTask("Implement Base Interface", is_completed=True))
    day3_section.add(ChecklistTask("Build Composite Pattern Section", is_completed=True))
    day3_section.add(ChecklistTask("Add Recursive JSON Export", is_completed=True))
    
    print("\n--- Rendering Section ---")
    print(day3_section.render())
    
    # Test JSON Export (Activity 4)
    day3_section.export_to_json()

@staticmethod
    def import_from_json(filename="day134_project.json"):
        import json
        try:
            with open(filename, "r") as f:
                data = json.load(f)
            
            # Helper function to recursively rebuild components
            def _rebuild(item_dict):
                t = item_dict.get("type")
                if t == "TextTask":
                    return TextTask(item_dict["content"])
                elif t == "ChecklistTask":
                    return ChecklistTask(item_dict["title"], item_dict["is_completed"])
                elif t == "ProjectSection":
                    section = ProjectSection(item_dict["title"])
                    for child_dict in item_dict.get("children", []):
                        section.add(_rebuild(child_dict))
                    return section
                return None

            rebuilt_section = _rebuild(data)
            print(f"\n[Loader] Successfully imported and reconstructed structure from {filename}!")
            return rebuilt_section
            
        except FileNotFoundError:
            print(f"\n⚠️ Warning: The file '{filename}' was not found.")
        except json.JSONDecodeError:
            print(f"\n⚠️ Error: Failed to decode JSON from '{filename}'.")
        except Exception as e:
            print(f"\n⚠️ An unexpected error occurred: {e}")
        return None

if __name__ == "__main__":
    print("🚀 Initializing Day 134 Final Master Program...")
    
    # 1. Create original section structure
    day3_section = ProjectSection("Day 134 Goals")
    day3_section.add(TextTask("Understand Polymorphism & Interfaces"))
    day3_section.add(ChecklistTask("Implement Base Interface", is_completed=True))
    day3_section.add(ChecklistTask("Build Composite Pattern Section", is_completed=True))
    day3_section.add(ChecklistTask("Add Recursive JSON Export & Import", is_completed=True))
    
    # 2. Export structure to JSON (Activity 4)
    day3_section.export_to_json()
    
    # 3. Import and reconstruct structure from JSON (Activity 5)
    print("\n--- Rebuilding from JSON File ---")
    restored_section = ProjectSection.import_from_json()
    
    if restored_section:
        print("\n--- Rendering Restored Structure ---")
        print(restored_section.render())