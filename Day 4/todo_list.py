## Practice Project: To-Do List Application

#Build a simple command-line to-do list manager.

def display_menu():
    """Display the main menu"""
    print("\n" + "=" * 50)
    print("           TO-DO LIST MANAGER")
    print("=" * 50)
    print("1. View all tasks")
    print("2. Add new task")
    print("3. Mark task as complete")
    print("4. Remove task")
    print("5. Search tasks")
    print("6. Sort tasks")
    print("7. Clear all tasks")
    print("8. Exit")
    print("=" * 50)

def view_tasks(tasks):
    """Display all tasks"""
    if not tasks:
        print("\n📋 No tasks found! Your to-do list is empty.")
        return
    
    print("\n" + "-" * 50)
    print("YOUR TASKS:")
    print("-" * 50)
    for i, task in enumerate(tasks, 1):
        status = "✓" if task[1] else "○"
        print(f"{i}. [{status}] {task[0]}")
    print("-" * 50)
    print(f"Total tasks: {len(tasks)} | Completed: {sum(1 for t in tasks if t[1])}")

def add_task(tasks):
    """Add a new task"""
    task_name = input("\nEnter task description: ").strip()
    if task_name:
        tasks.append([task_name, False])  # [task, completed_status]
        print(f"✓ Task '{task_name}' added successfully!")
    else:
        print("✗ Task cannot be empty!")

def complete_task(tasks):
    """Mark a task as complete"""
    if not tasks:
        print("\n✗ No tasks to complete!")
        return
    
    view_tasks(tasks)
    try:
        index = int(input("\nEnter task number to mark as complete: ")) - 1
        if 0 <= index < len(tasks):
            tasks[index][1] = True
            print(f"✓ Task '{tasks[index][0]}' marked as complete!")
        else:
            print("✗ Invalid task number!")
    except ValueError:
        print("✗ Please enter a valid number!")

def remove_task(tasks):
    """Remove a task"""
    if not tasks:
        print("\n✗ No tasks to remove!")
        return
    
    view_tasks(tasks)
    try:
        index = int(input("\nEnter task number to remove: ")) - 1
        if 0 <= index < len(tasks):
            removed = tasks.pop(index)
            print(f"✓ Task '{removed[0]}' removed successfully!")
        else:
            print("✗ Invalid task number!")
    except ValueError:
        print("✗ Please enter a valid number!")

def search_tasks(tasks):
    """Search for tasks"""
    if not tasks:
        print("\n✗ No tasks to search!")
        return
    
    keyword = input("\nEnter search keyword: ").strip().lower()
    found = [(i+1, task) for i, task in enumerate(tasks) 
             if keyword in task[0].lower()]
    
    if found:
        print("\n" + "-" * 50)
        print(f"SEARCH RESULTS FOR '{keyword}':")
        print("-" * 50)
        for num, task in found:
            status = "✓" if task[1] else "○"
            print(f"{num}. [{status}] {task[0]}")
        print("-" * 50)
    else:
        print(f"\n✗ No tasks found containing '{keyword}'")

def sort_tasks(tasks):
    """Sort tasks"""
    if not tasks:
        print("\n✗ No tasks to sort!")
        return
    
    print("\nSort by:")
    print("1. Alphabetical (A-Z)")
    print("2. Alphabetical (Z-A)")
    print("3. Completed first")
    print("4. Incomplete first")
    
    choice = input("Enter choice (1-4): ")
    
    if choice == '1':
        tasks.sort(key=lambda x: x[0].lower())
        print("✓ Tasks sorted alphabetically (A-Z)")
    elif choice == '2':
        tasks.sort(key=lambda x: x[0].lower(), reverse=True)
        print("✓ Tasks sorted alphabetically (Z-A)")
    elif choice == '3':
        tasks.sort(key=lambda x: x[1], reverse=True)
        print("✓ Tasks sorted (completed first)")
    elif choice == '4':
        tasks.sort(key=lambda x: x[1])
        print("✓ Tasks sorted (incomplete first)")
    else:
        print("✗ Invalid choice!")

def main():
    """Main program"""
    # Initialize task list
    # Each task is a list: [description, completed_status]
    tasks = []
    
    print("Welcome to To-Do List Manager!")
    
    while True:
        display_menu()
        choice = input("\nEnter your choice (1-8): ")
        
        if choice == '1':
            view_tasks(tasks)
        elif choice == '2':
            add_task(tasks)
        elif choice == '3':
            complete_task(tasks)
        elif choice == '4':
            remove_task(tasks)
        elif choice == '5':
            search_tasks(tasks)
        elif choice == '6':
            sort_tasks(tasks)
        elif choice == '7':
            confirm = input("\n⚠️  Clear all tasks? (yes/no): ")
            if confirm.lower() == 'yes':
                tasks.clear()
                print("✓ All tasks cleared!")
            else:
                print("✗ Operation cancelled")
        elif choice == '8':
            print("\n👋 Thank you for using To-Do List Manager!")
            print("Stay productive! 🚀")
            break
        else:
            print("\n✗ Invalid choice! Please try again.")

# Run the program
if __name__ == "__main__":
    main()
