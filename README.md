# Simple Student Time Management Program

# We will store tasks in a list
tasks = []

# Function to add a task
def add_task():
    name = input("Enter task name: ")  # ask for the task name
    due = input("Enter due date (YYYY-MM-DD): ")  # ask for the due date
    hours = float(input("Enter estimated hours: "))  # ask for estimated hours
    priority = input("Enter priority (High/Medium/Low): ")  # ask for priority

    # store task as a dictionary
    task = {
        "name": name,
        "due": due,
        "hours": hours,
        "priority": priority,
        "completed": False  # default is not completed
    }
    tasks.append(task)  # add task to the list
    print("Task added successfully!\n")

# Function to show all tasks
def list_tasks():
    if not tasks:  # if list is empty
        print("No tasks found.\n")
    else:
        for i, task in enumerate(tasks, start=1):  # loop through tasks
            status = "Done" if task["completed"] else "Pending"  # check if done
            print(f"{i}. {task['name']} - Due: {task['due']} - {task['hours']} hrs - {task['priority']} - {status}")
        print()

# Function to mark a task as complete
def mark_complete():
    list_tasks()  # show tasks first
    if tasks:  # only continue if there are tasks
        choice = int(input("Enter task number to mark complete: "))  # choose task
        if 1 <= choice <= len(tasks):  # check if choice is valid
            tasks[choice - 1]["completed"] = True  # update status
            print("Task marked as completed!\n")
        else:
            print("Invalid task number.\n")

# Function to show total hours for unfinished tasks
def total_hours():
    total = sum(task["hours"] for task in tasks if not task["completed"])  # add hours
    print(f"Total estimated hours left: {total}\n")

# Main program loop
def main():
    while True:  # keep running until user exits
        print("==== Student Time Management ====")
        print("1. Add task")
        print("2. List tasks")
        print("3. Mark task complete")
        print("4. Show total hours")
        print("5. Exit")

        choice = input("Choose an option (1-5): ")  # ask for menu option

        if choice == "1":
            add_task()
        elif choice == "2":
            list_tasks()
        elif choice == "3":
            mark_complete()
        elif choice == "4":
            total_hours()
        elif choice == "5":
            print("Goodbye! Manage your time well!")  # exit message
            break
        else:
            print("Invalid choice. Please try again.\n")

# Run the program
main()

✦ Features of the Python Program ✦

Add New Tasks

Lets the user enter the task name, due date, estimated hours, and priority.

Each task is stored in a list for easy tracking.

View All Tasks

Displays a numbered list of all tasks with their details (name, due date, hours, priority).

Shows the status of each task as either Pending or Done.

Mark Tasks as Completed

The user can select a task number to mark it as finished.

Helps the student see which tasks are already done and which are left.

Calculate Total Hours Remaining

Adds up the estimated hours for all tasks that are not completed yet.

Gives students an idea of how much study/work time is still needed.

Simple Menu System

The program runs in a loop with a clear menu (1–5 options).

Easy to use: students just type the number for what they want to do.

Exit Option

Allows the user to quit the program safely when finished.

# camia_EllemaVermug\

# Project Title: Simple Task Manager

## Project Description:
This is a simple Python program that helps students or users manage their tasks effectively.
It allows adding new tasks, viewing task details, marking tasks as completed, and calculating the total study/work hours remaining.

## Features
-Add New Tasks -> Enter Task Name, Due Date, Estimated Hours, Priority
-View All Tasks -> Display a numbered list with details & status (Pending/Done)
-Mark Tasks as Completed -> Select a task number to mark as Done
-Calculate Total Hours Remaining -> Sum of hours from all incomplete tasks
-Simple Menu System -> Menu-driven program with options (1–5) for easy navigation
-Exit Option -> Quit the program safely when finished

## How to Run the Program

1. Make sure you have Python installed.
2. Download the file: task_manager.py
3. Open a terminal or command prompt.
4. Run the program by pressing F5 or clicking Run.
5. Follow the on-screen menu to add, view, complete, or calculate tasks.

## Example Output:
 Task Manager
1. Add New Task
2. View All Tasks
3. Mark Task as Completed
4. Calculate Total Hours Remaining
5. Exit
Choose an option: 1

Enter task name: Math Homework
Enter due date: 2025-09-30
Enter estimated hours: 3
Enter priority (High/Medium/Low): High

Task added successfully!

Choose an option: 2
1. Math Homework 
   Due: 2025-09-30 
   Hours: 3  
   Priority: High 
   Status: Pending

## Contributors:

Student 1: Name of Member 1 → (Task adding & validation)
Student 2: Name of Member 2 → (Task viewing & completion logic)
Student 3: Name of Member 3 → (Hours calculation & testing)

