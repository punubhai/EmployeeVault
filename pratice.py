import customtkinter as ctk
import tkinter as tk
from tkinter import messagebox, ttk
import random
import sqlite3
import string
import main_page

DESIGNATION_TITLES = {
    "technician": [("Technical Ninja 1", "30,000"), ("Technical Ninja 2", "60,000"), ("Technical Ninja Senior", "1,00,000")],
    "sale": [("Sales Warrior Omega", "40,000"), ("Sales Mighty", "50,000"), ("Sales Master", "80,000")]
}

class EmployeeGUI:
    def __init__(self, master):
        self.master = master
        self.master.geometry("600x400")
        self.master.title("Employee Database")
        self.master.configure(bg="white")

        # Load the background image
        from PIL import Image, ImageTk

# Load the background image
        self.bg_image = ImageTk.PhotoImage(Image.open("img_2.png").resize((600, 400)))

# Set the background image

        # Set the background image

        # The rest of your code
        self.conn = sqlite3.connect('employee_database.db')
        self.c = self.conn.cursor()

        # Create table if it doesn't exist
        self.c.execute('''CREATE TABLE IF NOT EXISTS employees
                     (name text, mail text, emp_id text, phone text, rank text, designation text, salary text)''')

        self.name_var = ctk.StringVar()
        self.mail_var = ctk.StringVar()
        self.emp_id_var = ctk.StringVar()
        self.phone_var = ctk.StringVar()
        self.rank_var = ctk.StringVar()
        self.designation_var = ctk.StringVar()
        self.salary_var = ctk.StringVar()

        self.create_label_and_entry("Name:", self.name_var, 0)
        self.create_label_and_entry("Mail:", self.mail_var, 1)
        self.create_label_and_entry("Emp-Id:", self.emp_id_var, 2)
        self.create_label_and_entry("Phone-No:", self.phone_var, 3)
        self.create_label_and_entry("Rank:", self.rank_var, 4)
        self.create_label_and_entry("Designation:", self.designation_var, 5)
        self.create_label_and_entry("Salary:", self.salary_var, 6)

        ctk.CTkButton(self.master, text="Enter", command=self.add_employee_to_db, corner_radius=5).grid(row=7, column=0, columnspan=2, pady=10)
        ctk.CTkButton(self.master, text="Generate ID", command=self.generate_id, corner_radius=5).grid(row=2, column=2, padx=10)
        ctk.CTkButton(self.master, text="Get Titles and Salaries", command=self.get_titles_and_salaries, corner_radius=5).grid(row=6, column=2, pady=10)
        ctk.CTkButton(self.master, text="Back", command=self.back_to_main, corner_radius=5).grid(row=7)

    def create_label_and_entry(self, label_text, variable, row):
          tk.Label(self.master, text=label_text).grid(row=row, column=0)
          tk.Entry(self.master, textvariable=variable, width=30).grid(row=row, column=1)

    def add_employee_to_db(self):
        name = self.name_var.get()
        mail = self.mail_var.get()
        emp_id = self.emp_id_var.get()
        phone = self.phone_var.get()
        rank = self.rank_var.get()
        designation = self.designation_var.get()

        if not all([name, mail, emp_id, phone, rank, designation]):
            messagebox.showerror("Error", "All fields are required")
            return

        query = "INSERT INTO employees VALUES (?, ?, ?, ?, ?, ?, ?)"
        salary = self.salary_var.get()
        values = (name, mail, emp_id, phone, rank, designation, salary)

        try:
            self.c.execute(query, values)
            self.conn.commit()
            messagebox.showinfo("Success", "Employee added successfully")
            self.clear_entry_fields()
        except Exception as e:
            messagebox.showerror("Error", f"Failed to add employee: {e}")

    def generate_id(self):
        designation = self.designation_var.get()
        if not designation:
            messagebox.showerror("Error", "Please enter a designation first.")
            return

        first_letter = designation[0].lower()
        random_part = ''.join(random.choices(string.digits, k=5))
        employee_id = first_letter + random_part
        self.emp_id_var.set(employee_id)

        messagebox.showinfo("Success", "Employee ID generated.")

    def get_titles_and_salaries(self):
           designation = self.designation_var.get()
           if not designation:
               messagebox.showerror("Error", "Please enter a designation first.")
           return

           if designation in DESIGNATION_TITLES:
                titles_and_salaries = DESIGNATION_TITLES[designation]
                titles = ', '.join([title[0] for title in titles_and_salaries])
                salaries = ', '.join([title[1] for title in titles_and_salaries])

                self.title_textarea.delete('1.0')
                self.title_textarea.insert( f"Titles: {titles}\nSalaries: {salaries}")
           else:
                messagebox.showerror("Error", "Invalid designation.")

    def back_to_main(self):
        self.master.destroy()
        root = tk.Tk()
        main_page.MainPage(root)
        root.mainloop()

    def clear_entry_fields(self):
        self.name_var.set("")
        self.mail_var.set("")
        self.emp_id_var.set("")
        self.phone_var.set("")
        self.rank_var.set("")
        self.designation_var.set("")
        self.salary_var.set("")


if __name__ == "__main__":
    root = tk.Tk()
    EmployeeGUI(root)
    root.mainloop()
