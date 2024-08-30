import tkinter as tk
from tkinter import messagebox, StringVar
from PIL import Image, ImageTk
import random
import string
import sqlite3

import twotoggle


class CustomTkinter:
    def __init__(self, master):
        self.master = master

        self.master.geometry("1260x800")
        self.master.title("Employee Details")


        self.background_image = Image.open("bgnew.png")
        self.background_photo = ImageTk.PhotoImage(self.background_image)

        self.background_label = tk.Label(self.master, image=self.background_photo)
        self.background_label.place(x=0, y=0, relwidth=1, relheight=1)
        self.master.configure(background='red')

        self.heading_label = tk.Label(self.master, text="Welcome to Employees Vault", bg='#B29F9F', font=("Helvetica", 18, "bold"))
        self.heading_label.pack()

        self.add_employee_label = tk.Label(self.master, text="ADD Employee", bg='#B29F9F', font=("Helvetica", 30, "bold"))
        self.add_employee_label.pack(ipadx=0, ipady=10, padx=0, pady=10, anchor='nw')

        self.employee_detail_label = tk.Label(self.master, text="Employee Detail", bg='#B29F9F', font=("Helvetica", 20, "bold"))
        self.employee_detail_label.place(x=70, y=150)

        self.work_place_detail_label = tk.Label(self.master, text="Work Place Detail", bg='#B29F9F', font=("Helvetica", 20, "bold"))
        self.work_place_detail_label.place(x=850, y=150)

        self.personal_detail_label = tk.Label(self.master, text="Personal Detail", bg='#B29F9F', font=("Helvetica", 20, "bold"))
        self.personal_detail_label.place(x=550, y=150)

        self.other_detail_label = tk.Label(self.master, text="OTHER Detail", bg='#B29F9F', font=("Helvetica", 20, "bold"))
        self.other_detail_label.place(x=550, y=400)

        self.other_detail_label = tk.Label(self.master, text="POINT'S FOR RANKING", bg='#B29F9F', font=("Helvetica", 20, "bold"))
        self.other_detail_label.place(x=920, y=400)

        self.enter_button = tk.Button(self.master, text="ENTER", font=("Helvetica", 10, "bold"), command=self.save_to_database, width=20, height=1, bg="purple", fg="white")
        self.enter_button.place(x=500, y=665)

        self.back_button = tk.Button(self.master, text="Back", font=("Helvetica", 10, "bold"), command=self.acer_win, width=20, height=1, bg="red", fg="white")
        self.back_button.place(x=70, y=665)

        self.name_label = tk.Label(self.master, text="Name:", bg="#B29F9F", font=("Arial", 14, "bold"))
        self.name_label.place(x=70, y=220)
        self.name_entry = tk.Entry(self.master, width=35, font=('Arial', 12, 'bold'))
        self.name_entry.place(x=135, y=225)

        self.email_label = tk.Label(self.master, text="Email:", bg="#B29F9F", font=("Helvetica", 15, "bold"))
        self.email_label.place(x=70, y=270)
        self.email_entry = tk.Entry(self.master, width=35, font=('Arial', 12, 'bold'))
        self.email_entry.place(x=135, y=275)

        self.mobile_label = tk.Label(self.master, text="Mobile:", bg="#B29F9F", font=("Helvetica", 15, "bold"))
        self.mobile_label.place(x=70, y=320)
        self.mobile_entry = tk.Entry(self.master, width=35, font=('Arial', 12, 'bold'))
        self.mobile_entry.place(x=135, y=325)

        self.empid_label = tk.Label(self.master, text="EMPLOYEE_ID:", bg="#B29F9F", font=("Helvetica", 15, "bold"))
        self.empid_label.place(x=70, y=400)
        self.emp_id_var = StringVar()
        self.empid_entry = tk.Entry(self.master, textvariable=self.emp_id_var, width=20, font=('Arial', 12))
        self.empid_entry.place(x=70, y=480)

        self.generate_button = tk.Button(self.master, text="Generate Employee ID", command=self.generate_id, width=20, bg="black", fg="white")
        self.generate_button.place(x=150, y=480)

        self.dob_label = tk.Label(self.master, text="D.O.B:", bg="#B29F9F", font=("Helvetica", 15, "bold"))
        self.dob_label.place(x=500, y=220)
        self.dob_entry = tk.Entry(self.master, width=35, font=('Arial', 12, 'bold'))
        self.dob_entry.place(x=580, y=225)

        self.gender_label = tk.Label(self.master, text="Gender:", bg="#B29F9F", font=("Helvetica", 15, "bold"))
        self.gender_label.place(x=500, y=270)
        self.gender_entry = tk.Entry(self.master, width=35, font=('Arial', 12, 'bold'))
        self.gender_entry.place(x=580, y=275)

        self.address_label = tk.Label(self.master, text="Address:", bg="#B29F9F", font=("Helvetica", 15, "bold"))
        self.address_label.place(x=500, y=320)
        self.address_entry = tk.Entry(self.master, width=30, font=('Arial', 12, 'bold'))
        self.address_entry.place(x=600, y=325)

        self.role_label = tk.Label(self.master, text="Role:", bg="#B29F9F", font=("Helvetica", 15, "bold"))
        self.role_label.place(x=820, y=220)
        self.role_entry = tk.Entry(self.master, width=30, font=('Arial', 12, 'bold'))
        self.role_entry.place(x=880, y=225)

        self.post_label = tk.Label(self.master, text="Post:", bg="#B29F9F", font=("Helvetica", 15, "bold"))
        self.post_label.place(x=820, y=270)
        self.post_entry = tk.Entry(self.master, width=30, font=('Arial', 12, 'bold'))
        self.post_entry.place(x=880, y=270)

        self.dept_label = tk.Label(self.master, text="Department:", bg="#B29F9F", font=("Helvetica", 15, "bold"))
        self.dept_label.place(x=820, y=320)
        self.dept_entry = tk.Entry(self.master, width=30, font=('Arial', 12, 'bold'))
        self.dept_entry.place(x=950, y=325)

        self.joining_label = tk.Label(self.master, text="Joining Date:", bg="#B29F9F", font=("Helvetica", 15, "bold"))
        self.joining_label.place(x=550, y=480)
        self.joining_entry = tk.Entry(self.master, width=30, font=('Arial', 12, 'bold'))
        self.joining_entry.place(x=699, y=485)

        self.salary_label = tk.Label(self.master, text="Salary:", bg="#B29F9F", font=("Helvetica", 15, "bold"))
        self.salary_label.place(x=550, y=540)
        self.salary_entry = tk.Entry(self.master, width=30, font=('Arial', 12, 'bold'))
        self.salary_entry.place(x=699, y=545)

        placeholder_text = "0"
        self.WorkEthic_label = tk.Label(self.master, text="1.Work Ethic:", bg="#B29F9F", font=("Helvetica", 15, "bold"))
        self.WorkEthic_label.place(x=920, y=480)
        self.WorkEthic_entry = tk.Entry(self.master, width=10, font=('Arial', 12, 'bold'))
        self.WorkEthic_entry.insert(0, placeholder_text)
        self.WorkEthic_entry.place(x=1100, y=485)

        self.SoftSkills_label = tk.Label(self.master, text="2.Soft Skills:", bg="#B29F9F", font=("Helvetica", 15, "bold"))
        self.SoftSkills_label.place(x=920, y=540)
        self.SoftSkills_entry = tk.Entry(self.master, width=10, font=('Arial', 12, 'bold'))
        self.SoftSkills_entry.insert(0, placeholder_text)
        self.SoftSkills_entry.place(x=1100, y=545)

        self.AttendanceandPunctuality_label = tk.Label(self.master, text="3.Punctuality:", bg="#B29F9F", font=("Helvetica", 15, "bold"))
        self.AttendanceandPunctuality_label.place(x=920, y=600)
        self.AttendanceandPunctuality_entry = tk.Entry(self.master, width=10, font=('Arial', 12, 'bold'))
        self.AttendanceandPunctuality_entry.insert(0, placeholder_text)
        self.AttendanceandPunctuality_entry.place(x=1100, y=605)

        self.EthicalBehavior_label = tk.Label(self.master, text="4.Ethical Behavior:", bg="#B29F9F", font=("Helvetica", 15, "bold"))
        self.EthicalBehavior_label.place(x=920, y=660)

        self.EthicalBehavior_entry = tk.Entry(self.master, width=10, font=('Arial', 12, 'bold'))
        self.EthicalBehavior_entry.insert(0, placeholder_text)
        self.EthicalBehavior_entry.place(x=1120, y=665)

        self.ClientSatisfaction_label = tk.Label(self.master, text="5.Client Satisfaction:", bg="#B29F9F", font=("Helvetica", 15, "bold"))
        self.ClientSatisfaction_label.place(x=920, y=720)

# Set a placeholder text as a hint
        placeholder_text = "0"
        self.ClientSatisfaction_entry = tk.Entry(self.master, width=10, font=('Arial', 12, 'bold'))
        self.ClientSatisfaction_entry.insert(0, placeholder_text)  # Insert placeholder text
        self.ClientSatisfaction_entry.place(x=1120, y=725)

        self.conn = sqlite3.connect('employees.db')
        self.create_table()




    def generate_id(self):
        designation = self.dept_entry.get() # Change this to fetch designation from the input
        if not designation:
            messagebox.showerror("Error", "Please enter a designation first.")
            return

        first_letter = designation[0].lower()
        random_part = ''.join(random.choices(string.digits, k=5))
        employee_id = first_letter + random_part
        self.emp_id_var.set(employee_id)

    def create_table(self):
        cursor = self.conn.cursor()
        cursor.execute('''CREATE TABLE IF NOT EXISTS employees
                          (id INTEGER PRIMARY KEY, name TEXT, email TEXT, mobile TEXT, employee_id TEXT,
                          dob TEXT, gender TEXT, address TEXT, role TEXT, post TEXT, department TEXT,
                          joining_date TEXT, salary TEXT, work_ethic TEXT, soft_skills TEXT,
                          attendance_punctuality TEXT, ethical_behavior TEXT, client_satisfaction TEXT)''')
        self.conn.commit()
    def save_to_database(self):
        # Retrieve data from entry fields
        name = self.name_entry.get()
        email = self.email_entry.get()
        mobile = self.mobile_entry.get()
        employee_id = self.emp_id_var.get()
        dob = self.dob_entry.get()
        gender = self.gender_entry.get()
        address = self.address_entry.get()
        role = self.role_entry.get()
        post = self.post_entry.get()
        department = self.dept_entry.get()
        joining_date = self.joining_entry.get()
        salary = self.salary_entry.get()
        work_ethic = self.WorkEthic_entry.get()
        soft_skills = self.SoftSkills_entry.get()
        attendance_punctuality = self.AttendanceandPunctuality_entry.get()
        ethical_behavior = self.EthicalBehavior_entry.get()
        client_satisfaction = self.ClientSatisfaction_entry.get()

        # Check if any field is empty
        if any(not field for field in [name, email, mobile, employee_id, dob, gender, address, role, post, department,
                                       joining_date, salary, work_ethic, soft_skills, attendance_punctuality,
                                       ethical_behavior, client_satisfaction]):
            messagebox.showerror("Error", "Please fill in all fields.")
            return

        # Insert data into the database
        cursor = self.conn.cursor()
        cursor.execute('''INSERT INTO employees 
                          (name, email, mobile, employee_id, dob, gender, address, role, post, department, 
                          joining_date, salary, work_ethic, soft_skills, attendance_punctuality, ethical_behavior, client_satisfaction) 
                          VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)''',
                       (name, email, mobile, employee_id, dob, gender, address, role, post, department,
                        joining_date, salary, work_ethic, soft_skills, attendance_punctuality, ethical_behavior, client_satisfaction))
        self.conn.commit()
        messagebox.showinfo("Success", "Employee details saved successfully.")

        # Clear text fields
        # Clear text fields
        self.emp_id_var.set("")
        self.name_entry.delete(0, 'end')
        self.email_entry.delete(0, 'end')
        self.mobile_entry.delete(0, 'end')
        self.dob_entry.delete(0, 'end')
        self.gender_entry.delete(0, 'end')
        self.address_entry.delete(0, 'end')
        self.role_entry.delete(0, 'end')
        self.post_entry.delete(0, 'end')
        self.dept_entry.delete(0, 'end')
        self.joining_entry.delete(0, 'end')
        self.salary_entry.delete(0, 'end')
        self.WorkEthic_entry.delete(0, 'end')
        self.SoftSkills_entry.delete(0, 'end')
        self.AttendanceandPunctuality_entry.delete(0, 'end')
        self.EthicalBehavior_entry.delete(0, 'end')
        self.ClientSatisfaction_entry.delete(0, 'end')






        # Repeat this for all entry fields



    def acer_win(self):
     self.master.destroy()

    # Create a new Tkinter window
     new_root = tk.Tk()

    # Assuming twotoggle is imported and App2 is defined in it,
    # create an instance of App2 and start the event loop
     twotoggle.App2(new_root)

    # Start the Tkinter event loop
     new_root.mainloop()
    def __del__(self):
        self.conn.close()

    def run(self):
        self.master.mainloop()

if __name__ == "__main__":
    root = tk.Tk()  # Creating the root window
    app = CustomTkinter(root)  # Passing the root window as master
    app.run()


