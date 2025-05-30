#This is a python program
import json
import os
from datetime import datetime

# FILE TO STORE DATA AND ITS TYPE
DATA_FILE = "todo_data.json"

# Define a Task class
class Task:
    def __init__(self, title, description, due_date, completed=False):
        self.title = title
        self.description = description
        self.due_date = due_date
        self.completed = completed

    def to_dict(self):
        return {
            'title': self.title,
            'description': self.description,
            'due_date': self.due_date,
            'completed': self.completed
        }

    @staticmethod
    def from_dict(data):
        return Task(
            title=data['title'],
            description=data['description'],
            due_date=data['due_date'],
            completed=data.get('completed', False)
        )


# Load tasks from a JSON file
def load_tasks():
    if not os.path.exists(DATA_FILE):
        return []
    with open(DATA_FILE, 'r') as file:
        try:
            data = json.load(file)
            return [Task.from_dict(item) for item in data]
        except json.JSONDecodeError:
            return []

# Save tasks to a JSON file
def save_tasks(tasks):
    with open(DATA_FILE, 'w') as file:
        json.dump([task.to_dict() for task in tasks], file, indent=4)

# Display menu
def print_menu():
    print("\nTo-Do List Manager")
    print("-" * 25)
    print("1. View tasks")
    print("2. Add new task")
    print("3. Mark task as complete")
    print("4. Delete task")
    print("5. Exit")

# View all tasks
def view_tasks(tasks):
    if not tasks:
        print("No tasks found.")
        return
    print("\nYour Tasks:")
    for i, task in enumerate(tasks, 1):
        status = "✓" if task.completed else "✗"
        print(f"{i}. [{status}] {task.title} (Due: {task.due_date})")
        print(f"   {task.description}")

# Add a new task
def add_task(tasks):
    title = input("Enter task title: ")
    description = input("Enter task description: ")
    due_date = input("Enter due date (YYYY-MM-DD): ")
    try:
        # Validate date
        datetime.strptime(due_date, "%Y-%m-%d")
    except ValueError:
        print("Invalid date format.")
        return
    task = Task(title, description, due_date)
    tasks.append(task)
    save_tasks(tasks)
    print("Task added successfully!")

# Mark a task as completed
def mark_task_complete(tasks):
    view_tasks(tasks)
    try:
        choice = int(input("Enter the task number to mark as complete: ")) - 1
        if 0 <= choice < len(tasks):
            tasks[choice].completed = True
            save_tasks(tasks)
            print("Task marked as complete.")
        else:
            print("Invalid task number.")
    except ValueError:
        print("Please enter a valid number.")

# Delete a task
def delete_task(tasks):
    view_tasks(tasks)
    try:
        choice = int(input("Enter the task number to delete: ")) - 1
        if 0 <= choice < len(tasks):
            del tasks[choice]
            save_tasks(tasks)
            print("Task deleted.")
        else:
            print("Invalid task number.")
    except ValueError:
        print("Please enter a valid number.")

# Main loop
def main():
    tasks = load_tasks()
    while True:
        print_menu()
        choice = input("Select an option given below: ")
        if choice == '1':
            view_tasks(tasks)
        elif choice == '2':
            add_task(tasks)
        elif choice == '3':
            mark_task_complete(tasks)
        elif choice == '4':
            delete_task(tasks)
        elif choice == '5':
            print("Thank you Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

# Run the program
if __name__ == "__main__":
    main()

