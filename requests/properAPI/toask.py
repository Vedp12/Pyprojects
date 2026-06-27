import datetime
import csv

tasks = []

while True:
    print("\n===== TO-DO APP =====")
    print("1. Add Task")
    print("2. Delete Task")
    print("3. View Tasks")
    print("4. Save Tasks to CSV")
    print("5. Read Tasks from CSV")
    print("6. Exit")

    try:
        user = int(input("Enter choice: "))
    except ValueError:
        print("Please enter a valid number!")
        continue

    match user:

        # Add Task
        case 1:
            task = input("Enter task: ")
            tasks.append(task)
            print("Task added successfully!")

        # Delete Task
        case 2:
            if not tasks:
                print("No tasks available.")
                continue

            for i, task in enumerate(tasks):
                print(f"{i}: {task}")

            try:
                delete_index = int(input("Enter task number to delete: "))
                removed = tasks.pop(delete_index)
                print(f"Deleted: {removed}")
            except (ValueError, IndexError):
                print("Invalid task number!")

        # View Tasks
        case 3:
            if not tasks:
                print("No tasks available.")
            else:
                print("\nCurrent Tasks:")
                for i, task in enumerate(tasks):
                    print(f"{i+1}: {task}")

        # Save Tasks
        case 4:
            with open("tasks.csv", "w", newline="") as file:
                writer = csv.writer(file)

                headers = ["No", "Task", "Time"]
                writer.writerow(headers)

                for i, task in enumerate(tasks):
                    current_time = datetime.datetime.now()
                    writer.writerow([i, task, current_time])

            print("Tasks saved to tasks.csv")

        # Read Tasks
        case 5:
            try:
                with open("tasks.csv", "r") as file:
                    reader = csv.reader(file)

                    print("\n===== SAVED TASKS =====")
                    for row in reader:
                        print(row)

            except FileNotFoundError:
                print("tasks.csv not found!")

        # Exit
        case 6:
            print("Goodbye!")
            break

        # Invalid Option
        case _:
            print("Invalid choice!")