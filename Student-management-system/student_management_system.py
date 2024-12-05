import tkinter as tk
from tkinter import messagebox, filedialog
from tkinter import ttk
from PIL import Image, ImageTk
import os
import pandas as pd

class StudentManagementSystem:
    def __init__(self, root):
        self.root = root
        self.root.title("Student Management System")
        self.root.geometry("800x600")

        self.excel_file = "student_data.xlsx"  # Excel file to store data
        self.student_data = self.load_student_data()

        # Title
        self.title_label = tk.Label(self.root, text="Student Management System", font=("Helvetica", 20, "bold"))
        self.title_label.pack(pady=10)

        # Student details
        self.student_name_label = tk.Label(self.root, text="Student Name:")
        self.student_name_label.pack(pady=5)
        self.student_name_entry = tk.Entry(self.root, width=30)
        self.student_name_entry.pack(pady=5)
        
        self.parent_name_label = tk.Label(self.root, text="Parent Name:")
        self.parent_name_label.pack(pady=5)
        self.parent_name_entry = tk.Entry(self.root, width=30)
        self.parent_name_entry.pack(pady=5)
        
        self.class_label = tk.Label(self.root, text="Class:")
        self.class_label.pack(pady=5)
        self.class_entry = tk.Entry(self.root, width=30)
        self.class_entry.pack(pady=5)

        self.parent_phone_label = tk.Label(self.root, text="Parent Phone:")
        self.parent_phone_label.pack(pady=5)
        self.parent_phone_entry = tk.Entry(self.root, width=30)
        self.parent_phone_entry.pack(pady=5)

        self.fee_label = tk.Label(self.root, text="Fee Structure:")
        self.fee_label.pack(pady=5)
        self.fee_entry = tk.Entry(self.root, width=30)
        self.fee_entry.pack(pady=5)

        # Upload Photo Button
        self.upload_photo_btn = tk.Button(self.root, text="Upload Student Photo", command=self.upload_photo)
        self.upload_photo_btn.pack(pady=5)

        # Upload Report Card Button
        self.upload_report_card_btn = tk.Button(self.root, text="Upload Report Card (PDF)", command=self.upload_report_card)
        self.upload_report_card_btn.pack(pady=5)

        # Display Photo
        self.student_photo_label = tk.Label(self.root, text="No photo selected")
        self.student_photo_label.pack(pady=5)

        # Display Report Card
        self.report_card_label = tk.Label(self.root, text="No report card uploaded")
        self.report_card_label.pack(pady=5)

        # Buttons for CRUD operations
        self.save_btn = tk.Button(self.root, text="Save Student Data", command=self.save_student_data)
        self.save_btn.pack(pady=20)

        self.view_btn = tk.Button(self.root, text="View All Students", command=self.view_all_students)
        self.view_btn.pack(pady=5)

        self.update_btn = tk.Button(self.root, text="Update Student Data", command=self.update_student_data)
        self.update_btn.pack(pady=5)

        self.delete_btn = tk.Button(self.root, text="Delete Student Data", command=self.delete_student_data)
        self.delete_btn.pack(pady=5)

        self.print_btn = tk.Button(self.root, text="Print Report", command=self.print_report)
        self.print_btn.pack(pady=5)

    def load_student_data(self):
        """Load student data from the Excel file."""
        if os.path.exists(self.excel_file):
            return pd.read_excel(self.excel_file)
        else:
            # If the file doesn't exist, create a new one with the columns
            df = pd.DataFrame(columns=["Student Name", "Parent Name", "Class", "Parent Phone", "Fee Structure", "Photo", "Report Card"])
            df.to_excel(self.excel_file, index=False)
            return df

    def save_student_data(self):
        """Save the entered student data to the Excel file."""
        student_name = self.student_name_entry.get()
        parent_name = self.parent_name_entry.get()
        class_name = self.class_entry.get()
        parent_phone = self.parent_phone_entry.get()
        fee_structure = self.fee_entry.get()

        if student_name and parent_name and class_name and parent_phone and fee_structure:
            new_data = {
                "Student Name": student_name,
                "Parent Name": parent_name,
                "Class": class_name,
                "Parent Phone": parent_phone,
                "Fee Structure": fee_structure,
                "Photo": self.photo_path if hasattr(self, 'photo_path') else None,
                "Report Card": self.report_card_path if hasattr(self, 'report_card_path') else None
            }
            
            # Add the new data to the DataFrame and save it back to Excel
            self.student_data = self.student_data.append(new_data, ignore_index=True)
            self.student_data.to_excel(self.excel_file, index=False)
            messagebox.showinfo("Success", "Student data saved successfully!")
        else:
            messagebox.showwarning("Input Error", "Please fill in all fields.")

    def view_all_students(self):
        """Display all student records in a new window."""
        view_window = tk.Toplevel(self.root)
        view_window.title("All Students")
        view_window.geometry("600x400")

        tree = ttk.Treeview(view_window, columns=("Student Name", "Parent Name", "Class", "Parent Phone", "Fee Structure"), show="headings")
        tree.pack(fill=tk.BOTH, expand=True)

        tree.heading("Student Name", text="Student Name")
        tree.heading("Parent Name", text="Parent Name")
        tree.heading("Class", text="Class")
        tree.heading("Parent Phone", text="Parent Phone")
        tree.heading("Fee Structure", text="Fee Structure")

        # Populate the treeview with student data
        for _, row in self.student_data.iterrows():
            tree.insert("", "end", values=(row["Student Name"], row["Parent Name"], row["Class"], row["Parent Phone"], row["Fee Structure"]))

    def update_student_data(self):
        """Update the selected student data."""
        student_name = self.student_name_entry.get()
        if student_name:
            updated_data = {
                "Student Name": student_name,
                "Parent Name": self.parent_name_entry.get(),
                "Class": self.class_entry.get(),
                "Parent Phone": self.parent_phone_entry.get(),
                "Fee Structure": self.fee_entry.get(),
                "Photo": self.photo_path if hasattr(self, 'photo_path') else None,
                "Report Card": self.report_card_path if hasattr(self, 'report_card_path') else None
            }
            
            # Find the row with the same student name and update it
            self.student_data.loc[self.student_data["Student Name"] == student_name, updated_data.keys()] = updated_data.values()
            self.student_data.to_excel(self.excel_file, index=False)
            messagebox.showinfo("Success", "Student data updated successfully!")
        else:
            messagebox.showwarning("Input Error", "Please provide the student name to update.")

    def delete_student_data(self):
        """Delete the selected student data."""
        student_name = self.student_name_entry.get()
        if student_name:
            # Remove student data from the DataFrame
            self.student_data = self.student_data[self.student_data["Student Name"] != student_name]
            self.student_data.to_excel(self.excel_file, index=False)
            messagebox.showinfo("Success", "Student data deleted successfully!")
        else:
            messagebox.showwarning("Input Error", "Please provide the student name to delete.")

    def upload_photo(self):
        """Upload student photo."""
        file_path = filedialog.askopenfilename(filetypes=[("Image files", "*.png;*.jpg;*.jpeg")])
        if file_path:
            self.photo_path = file_path
            self.student_photo_label.config(text=f"Photo selected: {os.path.basename(file_path)}")

    def upload_report_card(self):
        """Upload student report card."""
        file_path = filedialog.askopenfilename(filetypes=[("PDF files", "*.pdf")])
        if file_path:
            self.report_card_path = file_path
            self.report_card_label.config(text=f"Report card selected: {os.path.basename(file_path)}")

    def print_report(self):
        """Print the student report card."""
        if hasattr(self, 'report_card_path'):
            os.startfile(self.report_card_path, "print")
        else:
            messagebox.showwarning("No Report Card", "Please upload a report card to print.")

# Run the application
if __name__ == "__main__":
    root = tk.Tk()
    app = StudentManagementSystem(root)
    root.mainloop()
