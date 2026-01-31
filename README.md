## Tracking the Time Management of Students: The Time Organizer


# by Therenz R. Ellema and Xanthus Matthew G. Vermug
In school, students often face challenges in managing their time effectively, especially when handling multiple assignments, projects, and activities. 
Many students forget deadlines or struggle to organize their schedules, which can result in stress and incomplete work. 
To address this problem, I developed a Simple Student Time Management Program. 
This program helps students organize their tasks by allowing them to list what needs to be done, mark completed tasks, and view the estimated time required to finish remaining work.
Unlike traditional methods that rely on memory or writing tasks manually on paper, this program provides a more efficient, organized, and accessible way for students to manage their workload.





# Objectives:
My program aims to achieve the following goals:

• To help students effectively organize and monitor their school tasks and deadlines, ensuring they stay aware of their academic responsibilities and manage their workload efficiently.
• To develop a Python-based task management system that allows students to record tasks, mark them as completed, and calculate the total hours required to finish remaining work, thereby promoting better time management through a simple and intuitive interface.

# Planned Features:
• Let students input their task name, due date, estimated hours, and priority level (High, Medium, or Low).

• Display all the current tasks, showing which ones are done or still pending.

• Allow students to update the status of a task once it is finished.

• Automatically calculate the total estimated time left for all unfinished tasks.

• Include a simple menu where students can easily add, view, or mark their tasks as complete.

• Provide an option to exit the program once they are done managing their tasks.

# Planned Inputs and Outputs:
The program will first ask students to enter the details of their tasks, such as:
The name, Due date, Number of hours needed, Priority     
(High, Medium, or Low) After that, the program will store these tasks and show them in an organized list.
For every task, it will display whether it is Pending or Done. 
Students can also choose to mark a task as completed once they finish it. 
Additionally, the program will show the total remaining hours of all pending tasks, 
helping students estimate how much time they still need to manage their schoolwork.
Through these simple inputs and outputs, 
The program will make it easier for students to track their responsibilities, manage their schedules, and stay productive every day.





# Scenario: Monday Morning Planning

In this scenario, we will add three tasks in a random order. You will see the program automatically "move" the High Priority task to the top.



1. Adding Tasks (User Input)

Action 1: Select 1 (Add Task)
Name: Math Homework | Due: 2026-02-05 | Hours: 2 | Priority: Medium

Action 2: Select 1 (Add Task)
Name: CS Project | Due: 2026-02-03 | Hours: 5 | Priority: High

Action 3: Select 1 (Add Task)
Name: Read Chapter 1 | Due: 2026-02-10 | Hours: 1 | Priority: Low



2. Viewing the List (Program Output)

When you select 2 (View List), the program will display the tasks sorted by priority:

 ==== Student Time Management ====

Add Task | 2. View (High Prio First) | 3. Mark Done | 4. Exit


Choice: 2


ID | TASK NAME      | DUE DATE   | PRIO   | STATUS

1  | CS Project     | 2026-02-03 | High   | Pending

2  | Math Homework  | 2026-02-05 | Medium | Pending

3  | Read Chapter 1 | 2026-02-10 | Low    | Pending

TOTAL REMAINING HOURS: 8.0



3. Marking a Task Complete

Action: Select 3 (Mark Done)

Input: Enter 1 (To finish the CS Project)

Enter ID number to mark complete: 1
Updated successfully!

TOTAL REMAINING HOURS: 3.0
