import tkinter as tk
from tkinter import messagebox, ttk
import json
import os

USER_FILE = "users_db.json"

class LoginWindow:
    def __init__(self, root, on_success):
        self.root = root
        self.on_success = on_success
        self.root.withdraw() 
        self.users = self.load_users()
        
        self.login_popup = tk.Toplevel(self.root)
        self.login_popup.title("The Time Organizer - Access Portal")
        self.login_popup.state('zoomed') 
        self.login_popup.configure(bg="#1a1a2e")
        
        self.main_frame = tk.Frame(self.login_popup, bg="#1a1a2e")
        self.main_frame.place(relx=0.5, rely=0.5, anchor="center")

        self.card = tk.Frame(self.main_frame, bg="#ffffff", padx=40, pady=40, highlightbackground="#3d5afe", highlightthickness=2)
        self.card.pack()

        tk.Label(self.card, text="🔑 SYSTEM LOGIN", font=("Helvetica", 18, "bold"), fg="#1a1a2e", bg="white").pack(pady=(0, 20))
        
        tk.Label(self.card, text="👤 SELECT ACCOUNT", font=("Arial", 8, "bold"), fg="#3d5afe", bg="white").pack(anchor="w")
        self.user_list = ttk.Combobox(self.card, values=list(self.users.keys()), font=("Arial", 11), state="readonly", width=28)
        self.user_list.pack(pady=(5, 15), ipady=5)
        
        if not self.users:
            self.user_list.set("No accounts found. Register below.")
        else:
            self.user_list.set("--- Choose an account ---")

        tk.Label(self.card, text="🆕 NEW USERNAME", font=("Arial", 8, "bold"), fg="#2d3436", bg="white").pack(anchor="w")
        self.user_entry = tk.Entry(self.card, font=("Arial", 12), width=30, bd=0, bg="#f1f2f6")
        self.user_entry.pack(pady=(5, 15), ipady=8)
        
        tk.Label(self.card, text="🔒 PASSWORD", font=("Arial", 8, "bold"), fg="#2d3436", bg="white").pack(anchor="w")
        self.pass_entry = tk.Entry(self.card, font=("Arial", 12), width=30, bd=0, bg="#f1f2f6", show="*")
        self.pass_entry.pack(pady=(5, 25), ipady=8)
        
        btn_frame = tk.Frame(self.card, bg="white")
        btn_frame.pack(fill="x")

        tk.Button(btn_frame, text="LOG IN", command=self.check_login, bg="#3d5afe", fg="white", font=("Arial", 10, "bold"), width=12, bd=0, cursor="hand2", pady=10).pack(side="left", expand=True, padx=5)
        tk.Button(btn_frame, text="REGISTER", command=self.register_user, bg="#f1f2f6", fg="#3d5afe", font=("Arial", 10, "bold"), width=12, bd=0, cursor="hand2", pady=10).pack(side="left", expand=True, padx=5)

        tk.Button(self.card, text="⚠️ RESET DATABASE", command=self.factory_reset, bg="white", fg="#e74c3c", font=("Arial", 7, "bold"), bd=0, cursor="hand2").pack(pady=(20, 0))

        self.login_popup.protocol("WM_DELETE_WINDOW", self.root.destroy)

    def load_users(self):
        if os.path.exists(USER_FILE):
            try:
                with open(USER_FILE, "r") as f:
                    data = json.load(f)
                    return data if data else {}
            except: pass
        return {} 

    def save_users(self):
        with open(USER_FILE, "w") as f:
            json.dump(self.users, f, indent=4)
        self.user_list['values'] = list(self.users.keys())

    def check_login(self):
        selected_user = self.user_list.get()
        typed_user = self.user_entry.get().lower().strip()
        user = typed_user if typed_user else selected_user
        pas = self.pass_entry.get()

        if user in self.users and self.users[user] == pas:
            self.login_popup.destroy()
            self.root.deiconify() 
            self.root.state('zoomed')
            self.on_success(user) 
        else:
            messagebox.showerror("Access Denied", "Invalid username or password.")

    def register_user(self):
        user = self.user_entry.get().lower().strip()
        pas = self.pass_entry.get().strip()
        if not user or not pas:
            messagebox.showwarning("Incomplete", "Fill in the fields.")
            return
        if user in self.users:
            messagebox.showerror("Error", "Username taken!")
        else:
            self.users[user] = pas
            self.save_users()
            messagebox.showinfo("Success", f"Welcome, {user}!")
            self.user_entry.delete(0, tk.END)
            self.user_list.set("--- Choose an account ---")

    def factory_reset(self):
        if messagebox.askyesno("Confirm Reset", "Delete all accounts?"):
            if os.path.exists(USER_FILE): os.remove(USER_FILE)
            self.users = {}
            self.user_list['values'] = []
            self.user_list.set("No accounts found.")
            messagebox.showinfo("Reset", "System database wiped.")

class TimeManagerGUI:
    def __init__(self, root, current_user):
        self.root = root
        self.current_user = current_user
        self.user_data_file = f"{self.current_user}_tasks.json"
        self.root.title(f"The Time Organizer - {self.current_user.title()}")
        self.root.configure(bg="#ffffff")
        
        self.tasks = self.load_tasks()

        # SIDEBAR
        self.sidebar = tk.Frame(root, bg="#2d3436", width=280, padx=25, pady=25)
        self.sidebar.pack(side="left", fill="y")
        self.sidebar.pack_propagate(False)

        tk.Label(self.sidebar, text="📂 NAVIGATOR", font=("Helvetica", 12, "bold"), bg="#2d3436", fg="#dfe6e9").pack(pady=(0, 30), anchor="w")

        tk.Label(self.sidebar, text="📝 TASK DESCRIPTION", font=("Arial", 8, "bold"), bg="#2d3436", fg="#636e72").pack(anchor="w")
        self.task_entry = tk.Entry(self.sidebar, font=("Arial", 11), bg="#3d4446", fg="white", bd=0, insertbackground="white")
        self.task_entry.pack(fill="x", pady=(5, 20), ipady=8)

        tk.Label(self.sidebar, text="⏱️ EST. HOURS", font=("Arial", 8, "bold"), bg="#2d3436", fg="#636e72").pack(anchor="w")
        self.hours_entry = tk.Entry(self.sidebar, font=("Arial", 11), bg="#3d4446", fg="white", bd=0, insertbackground="white")
        self.hours_entry.pack(fill="x", pady=(5, 20), ipady=8)

        tk.Label(self.sidebar, text="📊 PRIORITY LEVEL", font=("Arial", 8, "bold"), bg="#2d3436", fg="#636e72").pack(anchor="w")
        self.priority_var = tk.StringVar(value="Medium")
        self.priority_menu = ttk.Combobox(self.sidebar, textvariable=self.priority_var, values=["High", "Medium", "Low"], state="readonly")
        self.priority_menu.pack(fill="x", pady=(5, 30))

        tk.Button(self.sidebar, text="✚  ADD NEW TASK", command=self.add_task, bg="#3d5afe", fg="white", font=("Arial", 10, "bold"), bd=0, pady=12, cursor="hand2").pack(fill="x")
        
        # Spacer
        tk.Frame(self.sidebar, height=1, bg="#4b5557").pack(fill="x", pady=40)
        
        tk.Button(self.sidebar, text="🚪 LOG OUT", command=self.logout, bg="#2d3436", fg="#ff7675", font=("Arial", 9, "bold"), bd=1, relief="flat", pady=8, cursor="hand2").pack(fill="x")

        # MAIN WORKSPACE
        self.workspace = tk.Frame(root, bg="white", padx=40, pady=30)
        self.workspace.pack(side="right", fill="both", expand=True)

        # TOP BAR WITH SEARCH
        top_bar = tk.Frame(self.workspace, bg="white")
        top_bar.pack(fill="x", pady=(0, 20))

        tk.Label(top_bar, text=f"📋 {self.current_user.upper()}'S DASHBOARD", font=("Helvetica", 18, "bold"), bg="white", fg="#2d3436").pack(side="left")
        
        # SEARCH OBJECT
        search_frame = tk.Frame(top_bar, bg="#f1f2f6", padx=10)
        search_frame.pack(side="right")
        tk.Label(search_frame, text="🔍", bg="#f1f2f6").pack(side="left")
        self.search_var = tk.StringVar()
        self.search_var.trace("w", lambda name, index, mode: self.update_list())
        self.search_entry = tk.Entry(search_frame, textvariable=self.search_var, font=("Arial", 10), bg="#f1f2f6", bd=0, width=20)
        self.search_entry.pack(side="left", ipady=5, padx=5)

        # TABLE
        style = ttk.Style()
        style.theme_use("clam")
        style.configure("Treeview", background="white", fieldbackground="white", rowheight=40, font=("Arial", 10), borderwidth=0)
        style.configure("Treeview.Heading", background="#f1f2f6", font=("Arial", 10, "bold"), borderwidth=0)
        
        # selectmode="extended" allows multi-select
        self.tree = ttk.Treeview(self.workspace, columns=("Task", "Hours", "Priority", "Status"), show='headings', selectmode="extended")
        self.tree.heading("Task", text="TASK NAME")
        self.tree.heading("Hours", text="TIME")
        self.tree.heading("Priority", text="LEVEL")
        self.tree.heading("Status", text="PROGRESS")
        self.tree.column("Hours", width=80, anchor="center")
        self.tree.pack(fill="both", expand=True)

        # ACTION BAR
        action_bar = tk.Frame(self.workspace, bg="white", pady=25)
        action_bar.pack(fill="x")

        tk.Button(action_bar, text="✔️ MARK DONE", command=self.mark_complete, bg="#00b894", fg="white", width=18, bd=0, pady=10, font=("Arial", 9, "bold")).pack(side="left", padx=5)
        tk.Button(action_bar, text="🗑️ DELETE SELECTED", command=self.delete_task, bg="#f1f2f6", fg="#d63031", width=18, bd=0, pady=10, font=("Arial", 9, "bold")).pack(side="left", padx=5)
        
        # TASK COUNTER OBJECT
        self.counter_label = tk.Label(action_bar, text="Tasks: 0", font=("Arial", 9, "bold"), bg="#f1f2f6", fg="#2d3436", padx=15, pady=8)
        self.counter_label.pack(side="right", padx=5)
        
        tk.Button(action_bar, text="🧨 CLEAR ALL", command=self.clear_all_tasks, bg="#f1f2f6", fg="#636e72", width=18, bd=0, pady=10, font=("Arial", 9, "bold")).pack(side="right", padx=5)
        
        self.update_list()

    def load_tasks(self):
        if os.path.exists(self.user_data_file):
            try:
                with open(self.user_data_file, "r") as f:
                    return json.load(f)
            except: return []
        return []

    def save_tasks(self):
        with open(self.user_data_file, "w") as f:
            json.dump(self.tasks, f, indent=4)
        self.update_counter()

    def update_counter(self):
        total = len(self.tasks)
        pending = len([t for t in self.tasks if not t["completed"]])
        self.counter_label.config(text=f"Total: {total} | Pending: {pending}")

    def add_task(self):
        name, hours = self.task_entry.get().strip(), self.hours_entry.get().strip()
        if not name or not hours: return
        try:
            val_hours = float(hours)
            self.tasks.append({"name": name, "hours": val_hours, "priority": self.priority_var.get(), "completed": False})
            self.save_tasks(); self.update_list()
            self.task_entry.delete(0, tk.END); self.hours_entry.delete(0, tk.END)
        except: messagebox.showerror("Error", "Enter numbers for hours.")

    def update_list(self):
        for item in self.tree.get_children(): self.tree.delete(item)
        
        search_term = self.search_var.get().lower()
        order = {"High": 0, "Medium": 1, "Low": 2}
        
        # Filter and Sort
        filtered_tasks = [t for t in self.tasks if search_term in t["name"].lower()]
        sorted_tasks = sorted(filtered_tasks, key=lambda x: (x['completed'], order.get(x['priority'], 1)))
        
        for task in sorted_tasks:
            status = "✅ COMPLETED" if task["completed"] else "⌛ PENDING"
            self.tree.insert("", "end", values=(task["name"], f"{task['hours']}h", task["priority"], status))
        self.update_counter()

    def mark_complete(self):
        selected_items = self.tree.selection()
        if not selected_items: return
        
        for item in selected_items:
            task_name = self.tree.item(item)['values'][0]
            for task in self.tasks:
                if task["name"] == task_name:
                    task["completed"] = True
        
        self.save_tasks(); self.update_list()

    def delete_task(self):
        selected_items = self.tree.selection()
        if not selected_items: return
        
        # Get list of names to delete
        names_to_delete = [self.tree.item(item)['values'][0] for item in selected_items]
        
        if messagebox.askyesno("Confirm", f"Delete {len(names_to_delete)} selected task(s)?"):
            self.tasks = [t for t in self.tasks if t["name"] not in names_to_delete]
            self.save_tasks(); self.update_list()

    def clear_all_tasks(self):
        if messagebox.askyesno("Confirm", "Wipe all tasks?"):
            self.tasks = []; self.save_tasks(); self.update_list()

    def logout(self):
        self.root.destroy()
        main()

def main():
    root = tk.Tk()
    LoginWindow(root, lambda u: TimeManagerGUI(root, u))
    root.mainloop()

if __name__ == "__main__":
    main()