import tkinter as tk
from tkinter import messagebox
import os

class ToDoApp:
    def __init__(self, root):
        self.root = root
        self.root.title("To-Do List App")
        self.root.geometry("400x500")

        # File to store tasks
        self.file_path = "tasks.txt"
        self.tasks = self.load_tasks()  # Load tasks from file

        # Title
        self.title_label = tk.Label(self.root, text="To-Do List", font=("Helvetica", 16, "bold"))
        self.title_label.pack(pady=10)

        # Task Entry Field
        self.task_entry = tk.Entry(self.root, width=30, font=("Helvetica", 12))
        self.task_entry.pack(pady=10)

        # Add Task Button
        self.add_task_btn = tk.Button(self.root, text="Add Task", command=self.add_task, font=("Helvetica", 12))
        self.add_task_btn.pack(pady=5)

        # Create a frame to hold the Listbox and Scrollbar
        listbox_frame = tk.Frame(self.root)
        listbox_frame.pack(pady=10)

        # Add a Scrollbar
        self.scrollbar = tk.Scrollbar(listbox_frame, orient=tk.VERTICAL)

        # Task List Display with Scrollbar
        self.task_listbox = tk.Listbox(listbox_frame, width=40, height=15, font=("Helvetica", 12), selectmode=tk.SINGLE, yscrollcommand=self.scrollbar.set)
        self.task_listbox.pack(side=tk.LEFT)

        # Link the scrollbar to the listbox
        self.scrollbar.config(command=self.task_listbox.yview)
        self.scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

        # Populate the listbox with existing tasks
        self.populate_listbox()

        # Remove Task Button
        self.remove_task_btn = tk.Button(self.root, text="Remove Task", command=self.remove_task, font=("Helvetica", 12))
        self.remove_task_btn.pack(pady=5)

        # Clear All Tasks Button
        self.clear_tasks_btn = tk.Button(self.root, text="Clear All Tasks", command=self.clear_tasks, font=("Helvetica", 12))
        self.clear_tasks_btn.pack(pady=5)

        # Save tasks on close
        self.root.protocol("WM_DELETE_WINDOW", self.on_close)

    def load_tasks(self):
        """Load tasks from the file."""
        if os.path.exists(self.file_path):
            with open(self.file_path, "r") as file:
                return [task.strip() for task in file.readlines()]
        return []

    def save_tasks(self):
        """Save tasks to the file."""
        with open(self.file_path, "w") as file:
            for task in self.tasks:
                file.write(task + "\n")

    def populate_listbox(self):
        """Populate the listbox with tasks."""
        for task in self.tasks:
            self.task_listbox.insert(tk.END, task)

    def add_task(self):
        """Add a task to the list."""
        task = self.task_entry.get().strip()
        if task:
            self.tasks.append(task)
            self.task_listbox.insert(tk.END, task)
            self.task_entry.delete(0, tk.END)
        else:
            messagebox.showwarning("Warning", "Task cannot be empty!")

    def remove_task(self):
        """Remove the selected task."""
        try:
            selected_index = self.task_listbox.curselection()[0]  # Get selected index
            self.task_listbox.delete(selected_index)  # Remove from listbox
            del self.tasks[selected_index]  # Remove from internal list
        except IndexError:
            messagebox.showerror("Error", "No task selected!")

    def clear_tasks(self):
        """Clear all tasks."""
        if messagebox.askyesno("Confirm", "Are you sure you want to clear all tasks?"):
            self.task_listbox.delete(0, tk.END)  # Clear listbox
            self.tasks.clear()  # Clear internal list

    def on_close(self):
        """Save tasks before closing the app."""
        self.save_tasks()
        self.root.destroy()

# Main Program
if __name__ == "__main__":
    root = tk.Tk()
    app = ToDoApp(root)
    root.mainloop()
