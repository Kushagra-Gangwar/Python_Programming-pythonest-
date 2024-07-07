import os

TODO_FILE = 'todo_list.txt'

def load_tasks():
    """Load tasks from the text file."""
    if not os.path.exists(TODO_FILE):
        return []
    with open(TODO_FILE, 'r') as file:
        tasks = [line.strip() for line in file]
    return tasks

def save_tasks(tasks):
    """Save tasks to the text file."""
    with open(TODO_FILE, 'w') as file:
        for task in tasks:
            file.write(task + '\n')

def list_tasks(tasks):
    """List all tasks."""
    if not tasks:
        print("No tasks in the todo list.")
        return
    for i, task in enumerate(tasks, start=1):
        print(f"{i}. {task}")

def add_task(tasks):
    """Add a task to the list."""
    description = input("Enter task description: ")
    due_date = input("Enter due date (optional, press Enter to skip): ")
    task = description if not due_date else f"{description} (Due: {due_date})"
    tasks.append(task)
    save_tasks(tasks)
    print("Task added successfully.")

def remove_task(tasks):
    """Remove a task from the list."""
    list_tasks(tasks)
    try:
        task_num = int(input("Enter task number to remove: "))
        if 1 <= task_num <= len(tasks):
            removed_task = tasks.pop(task_num - 1)
            save_tasks(tasks)
            print(f"Removed task: {removed_task}")
        else:
            print("Invalid task number.")
    except ValueError:
        print("Invalid input. Please enter a number.")

def main():
    tasks = load_tasks()
    while True:
        print("\nTodo List Application")
        print("1. List tasks")
        print("2. Add task")
        print("3. Remove task")
        print("4. Exit")
        choice = input("Choose an option: ")
        if choice == '1':
            list_tasks(tasks)
        elif choice == '2':
            add_task(tasks)
        elif choice == '3':
            remove_task(tasks)
        elif choice == '4':
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
