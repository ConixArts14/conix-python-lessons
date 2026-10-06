# Day 132 - Activity 1: Object-Oriented Inheritance Fundamentals
# Author: Conix

class Project:
    def __init__(self, name, budget):
        self.name = name
        self.budget = budget

    def get_details(self):
        return f"Project: {self.name} | Budget: ${self.budget:,.2f}"

if __name__ == "__main__":
    print("🚀 Initializing Day 132 Activity 1 Program...")
    base_project = Project("Alpha Infrastructure", 50000)
    print(base_project.get_details())

class SoftwareProject(Project):
    def __init__(self, name, budget, programming_language):
        super().__init__(name, budget)
        self.programming_language = programming_language
        self.milestones = []

    def add_milestone(self, milestone):
        self.milestones.append(milestone)
        print(f"[{self.name}] Added milestone: '{milestone}'")

if __name__ == "__main__":
    print("🚀 Initializing Day 132 Activity 2 Program...")
    
    # Testing Base Class
    base_project = Project("Alpha Infrastructure", 50000)
    print(base_project.get_details())
    
    # Testing Child Class (Activity 2)
    print("\n--- Testing SoftwareProject Subclass ---")
    dev_project = SoftwareProject("Python Developer Mastery", 15000, "Python")
    print(dev_project.get_details())
    dev_project.add_milestone("Master OOP Inheritance")
    dev_project.add_milestone("Implement Polymorphism")

def get_details(self):
        # Activity 3: Overriding the parent class method
        base_info = super().get_details()
        return f"{base_info} | Language: {self.programming_language} | Milestones: {len(self.milestones)}"

if __name__ == "__main__":
    print("🚀 Initializing Day 132 Activity 3 Program...")
    
    # Testing Child Class with Method Overriding (Activity 3)
    dev_project = SoftwareProject("Python Developer Mastery", 15000, "Python")
    dev_project.add_milestone("Master OOP Inheritance")
    dev_project.add_milestone("Implement Method Overriding")
    
    print("\n--- Testing Overridden Method ---")
    print(dev_project.get_details())

def export_project_to_json(self, filename="day132_project.json"):
        # Activity 4: Exporting subclass data to JSON
        import json
        data = {
            "name": self.name,
            "budget": self.budget,
            "programming_language": self.programming_language,
            "milestones": self.milestones
        }
        with open(filename, "w") as f:
            json.dump(data, f, indent=4)
        print(f"\n[{self.name}] Successfully exported project data to {filename}!")

if __name__ == "__main__":
    print("🚀 Initializing Day 132 Activity 4 Program...")
    
    dev_project = SoftwareProject("Python Developer Mastery", 15000, "Python")
    dev_project.add_milestone("Master OOP Inheritance")
    dev_project.add_milestone("Implement Method Overriding")
    dev_project.add_milestone("Add JSON File Persistence")
    
    print("\n--- Testing Overridden Method ---")
    print(dev_project.get_details())
    
    # Testing File Export (Activity 4)
    dev_project.export_project_to_json()

def load_project_from_json(self, filename="day132_project.json"):
        # Activity 5: Robust file loading with error handling
        import json
        try:
            with open(filename, "r") as f:
                data = json.load(f)
                self.name = data.get("name", self.name)
                self.budget = data.get("budget", self.budget)
                self.programming_language = data.get("programming_language", self.programming_language)
                self.milestones = data.get("milestones", [])
            print(f"\n[{self.name}] Successfully loaded project data from {filename}!")
        except FileNotFoundError:
            print(f"\n⚠️ Warning: The file '{filename}' was not found.")
        except json.JSONDecodeError:
            print(f"\n⚠️ Error: Failed to decode JSON from '{filename}'.")
        except Exception as e:
            print(f"\n⚠️ An unexpected error occurred: {e}")

    def generate_capstone_report(self):
        # Activity 5: Final capstone report summary
        print("\n" + "="*50)
        print(f" 📊 DAY 132 CAPSTONE REPORT: {self.name}")
        print("="*50)
        print(f" 💰 Budget: ${self.budget:,.2f}")
        print(f" 💻 Language: {self.programming_language}")
        print(f" 🏆 Milestones Completed ({len(self.milestones)}):")
        for i, m in enumerate(self.milestones, 1):
            print(f"     {i}. {m}")
        print(" Status: Inheritance, Overriding, JSON I/O, & Error Handling Verified!")
        print("="*50)