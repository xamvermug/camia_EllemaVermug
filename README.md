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


# Sample Input and Output Scenario

Input:
A student enters the following task details into the program:

  •	Task Name: Science Project
  
    o	Due Date: November 10, 2025
    o	Hours Needed: 5
    o	Priority: High

Then the student adds two more tasks:

  •	Task Name: Math Homework
  
    o	Due Date: November 2, 2025
    o	Hours Needed: 2
    o	Priority: Medium

  •	Task Name: English Essay
  
    o	Due Date: November 8, 2025
    o	Hours Needed: 3
    o	Priority: High


Output:
After saving the tasks, the program displays them in an organized list:


  Task Name----------Due Date------Hours Needed----Priority-------Status
  
  Math Homework---Nov 2, 2025----2 hrs--------------Medium------Pending
  
  English Essay-------Nov 8, 2025----3 hrs--------------High----------Pending
  
  Science Project-----Nov 10, 2025---5 hrs-------------High----------Pending
  
Total Remaining Hours: 10 hours





Updated Output (after marking one task as completed):
The student marks “Math Homework” as completed.


   Task Name----------Due Date------Hours Needed----Priority-------Status
  
  Math Homework---Nov 2, 2025----2 hrs--------------Medium------Completed
  
  English Essay-------Nov 8, 2025----3 hrs--------------High----------Pending
  
  Science Project-----Nov 10, 2025---5 hrs-------------High----------Pending
  
Total Remaining Hours: 8 hours


