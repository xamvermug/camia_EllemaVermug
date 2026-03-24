import tkinter as tk
from tkinter import messagebox, ttk
import json
import os

DATA_FILE = "student_tasks.json"

class TimeManagerGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Student Time Management System")
        self.root.geometry("600x450")
        
        self.tasks = self.load_tasks()

        # --- UI Elements ---
        # Title
        tk.Label(root, text="Task Manager", font=("Arial", 18, "bold")).pack(pady=10)

        # Input Frame
        input_frame = tk.Frame(root)
        input_frame.pack(pady=10)

        tk.Label(input_frame, text="Task:").grid(row=0, column=0)
        self.task_entry = tk.Entry(input_frame)
        self.task_entry.grid(row=0, column=1, padx=5)

        tk.Label(input_frame, text="Hours:").grid(row=0, column=2)
        self.hours_entry = tk.Entry(input_frame, width=5)
        self.hours_entry.grid(row=0, column=3, padx=5)

        tk.Label(input_frame, text="Priority:").grid(row=1, column=0, pady=5)
        self.priority_var = tk.StringVar(value="Medium")
        self.priority_menu = ttk.Combobox(input_frame, textvariable=self.priority_var, values=["High", "Medium", "Low"], width=10)
        self.priority_menu.grid(row=1, column=1, padx=5)

        add_btn = tk.Button(input_frame, text="Add Task", command=self.add_task, bg="#4CAF50", fg="white")
        add_btn.grid(row=1, column=2, columnspan=2, sticky="ew", padx=5)

        # Task List (Treeview)
        self.tree = ttk.Treeview(root, columns=("Task", "Hours", "Priority", "Status"), show='headings')
        self.tree.heading("Task", text="Task Name")
        self.tree.heading("Hours", text="Hrs")
        self.tree.heading("Priority", text="Priority")
        self.tree.heading("Status", text="Status")
        self.tree.column("Hours", width=50)
        self.tree.pack(pady=10, padx=10, fill="both", expand=True)

        # Bottom Buttons
        btn_frame = tk.Frame(root)
        btn_frame.pack(pady=10)

        tk.Button(btn_frame, text="Mark Complete", command=self.mark_complete).pack(side="left", padx=5)
        tk.Button(btn_frame, text="Delete Task", command=self.delete_task, bg="#f44336", fg="white").pack(side="left", padx=5)
        
        self.update_list()

    def load_tasks(self):
        if os.path.exists(DATA_FILE):
            with open(DATA_FILE, "r") as f:
                return json.load(f)
        return []

    def save_tasks(self):
        with open(DATA_FILE, "w") as f:
            json.dump(self.tasks, f, indent=4)

    def add_task(self):
        name = self.task_entry.get()
        hours = self.hours_entry.get()
        if name and hours:
            try:
                self.tasks.append({
                    "name": name,
                    "hours": float(hours),
                    "priority": self.priority_var.get(),
                    "completed": False
                })
                self.save_tasks()
                self.update_list()
                self.task_entry.delete(0, tk.END)
                self.hours_entry.delete(0, tk.END)
            except ValueError:
                messagebox.showerror("Error", "Please enter a valid number for hours.")
        else:
            messagebox.showwarning("Warning", "Fill in all fields!")

    def update_list(self):
        # Clear current list
        for item in self.tree.get_children():
            self.tree.delete(item)
        
        # Sort by priority
        order = {"High": 0, "Medium": 1, "Low": 2}
        sorted_tasks = sorted(self.tasks, key=lambda x: order.get(x['priority'], 1))
        
        for task in sorted_tasks:
            status = "Done" if task["completed"] else "Pending"
            self.tree.insert("", "end", values=(task["name"], task["hours"], task["priority"], status))

    def mark_complete(self):
        selected = self.tree.selection()
        if selected:
            item_text = self.tree.item(selected[0])['values'][0]
            for task in self.tasks:
                if task["name"] == item_text:
                    task["completed"] = True
            self.save_tasks()
            self.update_list()

    def delete_task(self):
        selected = self.tree.selection()
        if selected:
            item_text = self.tree.item(selected[0])['values'][0]
            self.tasks = [t for t in self.tasks if t["name"] != item_text]
            self.save_tasks()
            self.update_list()

if __name__ == "__main__":
    root = tk.Tk()
    app = TimeManagerGUI(root)
    root.mainloop()