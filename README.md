## Tracking the Time Management of Students: The Time Organizer


# by Therenz R. Ellema and Xanthus Matthew G. Vermug
In school, students often face challenges in managing their time effectively, especially when handling multiple assignments, projects, and activities. 
Many students forget deadlines or struggle to organize their schedules, which can result in stress and incomplete work. 
To address this problem, We developed a Simple Student Time Management Program. 
This program helps students organize their tasks by allowing them to list what needs to be done, mark completed tasks, and view the estimated time required to finish remaining work.
Unlike traditional methods that rely on memory or writing tasks manually on paper, this program provides a more efficient, organized, and accessible way for students to manage their workload.





# Objectives:
My program aims to achieve the following goals:

• To help students effectively organize and monitor their school tasks and deadlines, ensuring they stay aware of their academic responsibilities and manage their workload efficiently.

• To develop a Python-based task management system that allows students to record tasks, mark them as completed, and calculate the total hours required to finish remaining work, thereby promoting better time management through a simple and intuitive interface.

# Planned inputs and outputs:


Inputs:

The program gathers specific details from the student through an easy-to-use input form:

Task Name: A short description of the assignment (e.g., "Math Worksheet").

Estimated Hours: A numerical value representing how long the task will take.

Priority Level: A selection from a dropdown menu (High, Medium, or Low).

Outputs:

The program processes the inputs to provide the following visual feedback:

Dynamic Task Table: A structured display showing the Name, Hours, Priority, and Status (Pending/Done) for every task.

Remaining Hours Summary: A live calculation shown at the bottom of the window totaling the hours needed for all unfinished work.

Status Indicators: Visual cues (like the "✓ Done" label) that give students a satisfying sense of progress.

System Alerts: Pop-up messages that confirm when a task is saved or warn the user if a field was filled out incorrectly.

# Planned Features:


- Interactive Graphical User Interface (GUI): A clean, window-based application that replaces the command-line interface for better accessibility.

- Smart Task Prioritization: Automatically sorts the task list so that High Priority items stay at the top, helping students focus on urgent work first.

- Persistent Data Storage: Uses JSON file handling to ensure all tasks are saved automatically. Students can close the app and return later without losing their data.

- Real-Time Workload Calculation: A built-in calculator that sums up the estimated hours of all "Pending" tasks to give an immediate view of the remaining workload.

- Input Validation & Error Handling: Includes safety checks to prevent the program from crashing if a student enters invalid information (like typing letters instead of numbers for hours).

- Task Lifecycle Management: Simple buttons to add new tasks, mark existing ones as "Done," or permanently delete completed or irrelevant items..





# Scenario: Monday Morning Planning

It’s 7:30 AM on a Monday, and Therenz just sat down at his desk to start the school week. He has a lot on his plate: a History essay, a Biology lab report, and a Math problem set. Normally, he’d feel a bit scattered trying to remember what’s due when, but today he opens "The Time Organizer."

Logging the Week: Therenz starts by entering his tasks into the GUI. He types in "History Essay," sets the hours to "3," and selects High Priority because it’s a major grade. He then adds his Biology and Math assignments.

Instant Organization: As soon as he hits "Add Task," the program springs into action. Even though he entered the Math homework last, the program automatically bumps the High Priority History essay to the top of the table. He can see at a glance that his total workload for the week is 6 hours.

Staying on Track: By lunch, Therenz has finished his Math problems. Instead of crossing it out with a messy pen on paper, he simply clicks the task in the window and hits "Mark Complete." The status instantly updates to "✓ Done." Looking at the summary at the bottom, he sees his remaining work has dropped to 4 hours.

The Stress-Free Finish: Because the program saved his data to a file, Therenz can close his laptop and head to practice. He doesn't have to worry about forgetting the Biology lab report because the program is holding that information for him, organized and ready for when he returns.


