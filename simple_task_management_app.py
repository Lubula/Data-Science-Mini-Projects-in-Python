# Developing a simple console-based task management application that allows users to add, view, update, and delete tasks. Tasks will be stored in a text file.

import os
import datetime

# Function to load tasks from a file
def load_tasks():
    tasks = []

    # Check if the tasks file exists
    if os.path.exists("tasks.txt"):
        # Open the tasks file in read mode
        with open("tasks.txt", "r") as file:
            # Read each line in the file
            for line in file:
                # Split the line into a list using commas as separators
                task = line.strip().split(",")
                # Append the task to the tasks list
                tasks.append(task)
    
    return tasks

# Function to save tasks to a file
def save_tasks(tasks):
    # Open the tasks file in write mode
    with open("tasks.txt", "w") as file:
        # Iterate through each task in the tasks list
        for task in tasks:
            # Write the task as a comma-separated string to the file
            file.write(",".join(task) + "\n")

# Function to display the menu
def display_menu():
    # Print the menu options
    print("1. Add a task")
    print("2. View tasks")
    print("3. Update a task")
    print("4. Delete a task")
    print("5. Exit")

# Function to add a new task
def add_task(tasks):
    # Get user input for task details
    title = input("Enter task title: ")
    description = input("Enter task description: ")
    due_date = input("Enter due date (YYYY-MM-DD): ")

    # Validate the date format
    try:
        datetime.datetime.strptime(due_date, "%Y-%m-%d")
    except ValueError:
        print("Invalid date format. Please use YYYY-MM-DD.")
        return

    # Append the new task to the tasks list
    tasks.append([title, description, due_date])
    # Save the updated tasks to the file
    save_tasks(tasks)
    print("Task added successfully!")

# Function to view all tasks
def view_tasks(tasks):
    # Check if there are no tasks
    if not tasks:
        print("No tasks available.")
    else:
        # Iterate through each task and display its details
        for i, task in enumerate(tasks):
            print(f"{i + 1}. Title: {task[0]}, Description: {task[1]}, Due Date: {task[2]}")

# Function to update a task
def update_task(tasks):
    # Display the current tasks
    view_tasks(tasks)
    # Get user input for the task to update
    task_id = input("Enter the task number to update: ")

    try:
        # Convert the task_id to an integer
        task_id = int(task_id)
        # Check if the task_id is within the valid range
        if 1 <= task_id <= len(tasks):
            # Get user input for the updated task details
            title = input("Enter updated task title: ")
            description = input("Enter updated task description: ")
            due_date = input("Enter updated due date (YYYY-MM-DD): ")

            # Validate the date format
            try:
                datetime.datetime.strptime(due_date, "%Y-%m-%d")
            except ValueError:
                print("Invalid date format. Please use YYYY-MM-DD.")
                return

            # Update the task in the tasks list
            tasks[task_id - 1] = [title, description, due_date]
            # Save the updated tasks to the file
            save_tasks(tasks)
            print("Task updated successfully!")
        else:
            print("Invalid task number.")
    except ValueError:
        print("Invalid input. Please enter a valid task number.")

# Function to delete a task
def delete_task(tasks):
    # Display the current tasks
    view_tasks(tasks)
    # Get user input for the task to delete
    task_id = input("Enter the task number to delete: ")

    try:
        # Convert the task_id to an integer
        task_id = int(task_id)
        # Check if the task_id is within the valid range
        if 1 <= task_id <= len(tasks):
            # Delete the task from the tasks list
            del tasks[task_id - 1]
            # Save the updated tasks to the file
            save_tasks(tasks)
            print("Task deleted successfully!")
        else:
            print("Invalid task number.")
    except ValueError:
        print("Invalid input. Please enter a valid task number.")

# Main function
def main():
    # Load existing tasks from the file
    tasks = load_tasks()

    while True:
        # Display the menu
        display_menu()
        # Get user input for the menu choice
        choice = input("Enter your choice: ")

        # Perform the corresponding action based on the user's choice
        if choice == "1":
            add_task(tasks)
        elif choice == "2":
            view_tasks(tasks)
        elif choice == "3":
            update_task(tasks)
        elif choice == "4":
            delete_task(tasks)
        elif choice == "5":
            print("Exiting the task manager.")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 5.")

if __name__ == "__main__":
    # Run the main function when the script is executed
    main()

