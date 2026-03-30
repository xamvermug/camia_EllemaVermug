import tkinter as tk
from tkinter import messagebox, ttk
import json
import os

DATA_FILE = "student_tasks.json"

class TimeManagerGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Student Time Management System v2.0")
        self.root.geometry("650x500")
        self.root.configure(bg="#f0f0f0") # Light grey background for a cleaner look
        
        self.tasks = self.load_tasks()

        # --- UI Elements ---
        # Header
        header_frame = tk.Frame(root, bg="#2c3e50")
        header_frame.pack(fill="x")
        tk.Label(header_frame, text="THE TIME ORGANIZER", font=("Helvetica", 16, "bold"), fg="white", bg="#2c3e50", pady=10).pack()

        # Input Frame
        input_frame = tk.LabelFrame(root, text=" Add New Task ", padx=10, pady=10)
        input_frame.pack(pady=10, padx=20, fill="x")

        tk.Label(input_frame, text="Task Name:").grid(row=0, column=0, sticky="w")
        self.task_entry = tk.Entry(input_frame, width=30)
        self.task_entry.grid(row=0, column=1, padx=5, pady=5)

        tk.Label(input_frame, text="Est. Hours:").grid(row=0, column=2, sticky="w")
        self.hours_entry = tk.Entry(input_frame, width=10)
        self.hours_entry.grid(row=0, column=3, padx=5, pady=5)

        tk.Label(input_frame, text="Priority Level:").grid(row=1, column=0, sticky="w")
        self.priority_var = tk.StringVar(value="Medium")
        self.priority_menu = ttk.Combobox(input_frame, textvariable=self.priority_var, values=["High", "Medium", "Low"], state="readonly", width=12)
        self.priority_menu.grid(row=1, column=1, padx=5, pady=5, sticky="w")

        # Buttons with colors
        add_btn = tk.Button(input_frame, text="+ Add to List", command=self.add_task, bg="#27ae60", fg="white", font=("Arial", 9, "bold"), width=15)
        add_btn.grid(row=1, column=2, columnspan=2, padx=5, pady=5, sticky="e")

        # Task List (Treeview)
        self.tree = ttk.Treeview(root, columns=("Task", "Hours", "Priority", "Status"), show='headings')
        self.tree.heading("Task", text="TASK DESCRIPTION")
        self.tree.heading("Hours", text="HRS")
        self.tree.heading("Priority", text="PRIORITY")
        self.tree.heading("Status", text="STATUS")
        
        # Column formatting
        self.tree.column("Hours", width=60, anchor="center")
        self.tree.column("Priority", width=100, anchor="center")
        self.tree.column("Status", width=100, anchor="center")
        self.tree.pack(pady=10, padx=20, fill="both", expand=True)

        # Control Buttons Frame
        btn_frame = tk.Frame(root)
        btn_frame.pack(pady=10)

        tk.Button(btn_frame, text="✔ Mark as Done", command=self.mark_complete, bg="#2980b9", fg="white", width=15).pack(side="left", padx=10)
        tk.Button(btn_frame, text="🗑 Delete Selected", command=self.delete_task, bg="#c0392b", fg="white", width=15).pack(side="left", padx=10)
        tk.Button(btn_frame, text="⚠ Clear All", command=self.clear_all_tasks, bg="#7f8c8d", fg="white", width=15).pack(side="left", padx=10)
        
        self.update_list()

    def load_tasks(self):
        try:
            if os.path.exists(DATA_FILE):
                with open(DATA_FILE, "r") as f:
                    return json.load(f)
        except Exception as e:
            print(f"Error loading file: {e}")
        return []

    def save_tasks(self):
        with open(DATA_FILE, "w") as f:
            json.dump(self.tasks, f, indent=4)

    def add_task(self):
        name = self.task_entry.get().strip()
        hours = self.hours_entry.get().strip()
        
        # WEEK 7 UPGRADE: Strict Input Validation
        if not name or not hours:
            messagebox.showwarning("Incomplete Data", "Please fill in both the Task Name and Hours.")
            return
            
        try:
            val_hours = float(hours)
            if val_hours <= 0:
                raise ValueError
                
            self.tasks.append({
                "name": name,
                "hours": val_hours,
                "priority": self.priority_var.get(),
                "completed": False
            })
            self.save_tasks()
            self.update_list()
            
            # Reset fields
            self.task_entry.delete(0, tk.END)
            self.hours_entry.delete(0, tk.END)
            self.priority_var.set("Medium")
            
        except ValueError:
            messagebox.showerror("Input Error", "Please enter a positive number for 'Hours'.")

    def update_list(self):
        for item in self.tree.get_children():
            self.tree.delete(item)
        
        # Sorting Logic
        order = {"High": 0, "Medium": 1, "Low": 2}
        sorted_tasks = sorted(self.tasks, key=lambda x: (x['completed'], order.get(x['priority'], 1)))
        
        for task in sorted_tasks:
            status = "✅ Done" if task["completed"] else "⏳ Pending"
            self.tree.insert("", "end", values=(task["name"], f"{task['hours']}h", task["priority"], status))

    def mark_complete(self):
        selected = self.tree.selection()
        if not selected:
            messagebox.showinfo("Selection Required", "Please click on a task to mark it as complete.")
            return
            
        item_text = self.tree.item(selected[0])['values'][0]
        for task in self.tasks:
            if task["name"] == item_text:
                task["completed"] = True
                break
        
        self.save_tasks()
        self.update_list()

    def delete_task(self):
        selected = self.tree.selection()
        if not selected:
            messagebox.showinfo("Selection Required", "Select a task to delete.")
            return
            
        item_text = self.tree.item(selected[0])['values'][0]
        self.tasks = [t for t in self.tasks if t["name"] != item_text]
        self.save_tasks()
        self.update_list()

    def clear_all_tasks(self):
        if messagebox.askyesno("Confirm", "Are you sure you want to delete EVERY task?"):
            self.tasks = []
            self.save_tasks()
            self.update_list()

if __name__ == "__main__":
    root = tk.Tk()
    app = TimeManagerGUI(root)
    root.mainloop()