def task():
    # List to store tasks
    tasks = []

    print("WELCOME TO TASK MANAGEMENT APP")

    # Ask the user how many tasks they want to add initially
    while True:
        try:
            total_tasks = int(input("Enter how many tasks you want to add: "))
            if total_tasks <= 0:
                print("Please enter a positive number.")
                continue
            break
        except ValueError:
            print("Invalid input! Enter a number.")

    # Add initial tasks one by one
    for i in range(1, total_tasks + 1):
        while True:
            task_name = input(f"Enter task {i} of {total_tasks}: ").strip()
            if task_name:
                tasks.append(task_name)  # Add task to list
                break
            else:
                print("Task cannot be empty!")

    # Task Manager Menu - similar to JS task manager UI
    while True:
        # Show current tasks
        print("\nToday's tasks:", tasks if tasks else "No tasks available.")

        # Show options to the user
        print("\nOptions:")
        print("1 - Add New Task")
        print("2 - Update Task")
        print("3 - Delete Task")
        print("4 - Delete All Tasks")
        print("5 - Exit")

        operation = input("Enter your choice (1-5): ").strip()

        # Add a new task
        if operation == "1":
            new_task = input("Enter new task: ").strip()
            if new_task:
                tasks.append(new_task)
                print(f"Task '{new_task}' has been successfully added.")
            else:
                print("Task cannot be empty!")

        # Update an existing task
        elif operation == "2":
            old_task = input("Enter the task you want to update: ").strip()
            if old_task in tasks:
                new_task = input("Enter new task: ").strip()
                if new_task:
                    index = tasks.index(old_task)
                    tasks[index] = new_task  # Replace old task with new task
                    print(f"Task updated to '{new_task}'.")
                else:
                    print("Task cannot be empty!")
            else:
                print("Task not found!")

        # Delete a specific task
        elif operation == "3":
            del_task = input("Which task you want to delete: ").strip()
            if del_task in tasks:
                tasks.remove(del_task)  # Remove task from list
                print(f"Task '{del_task}' has been deleted.")
            else:
                print("Task not found!")

        # Delete all tasks at once
        elif operation == "4":
            tasks.clear()  # Clear the entire list
            print("All tasks have been deleted.")

        # Exit the program
        elif operation == "5":
            print("✅ Thanks for using the To-Do App! Closing program...")
            break

        # Handle invalid input
        else:
            print("Invalid choice! Please enter a number from 1 to 5.")


# Call the task manager function
task()
