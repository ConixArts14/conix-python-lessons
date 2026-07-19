import json

tasks = []

def save_tasks():
    with open("tasks.json", "w") as file:
        json.dump(tasks, file)

def load_tasks():
    global tasks
    try:
        with open("tasks.json", "r") as file:
            tasks = json.load(file)
    except FileNotFoundError:
        tasks = []

def add_task(task):
    tasks.append(task)
    save_tasks()
    return f"Task '{task}' added!"

def view_tasks():
    return tasks

def remove_task(task):
    if task in tasks:
        tasks.remove(task)
        save_tasks()
        return f"Task '{task}' removed!"
    return "Task not found."

# Demo run
load_tasks()
print(add_task("Finish Day 54 lesson"))
print(view_tasks())
