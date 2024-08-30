import smtplib
import tkinter as tk
from email.message import EmailMessage
from tkinter import messagebox, StringVar
from PIL import Image, ImageTk
import main

import sqlite3

import twotoggle


class CustomTkinter:
    def __init__(self, master):
        self.master = master

        # Initialize SQLite database connection and cursor
        self.conn = sqlite3.connect("employees.db")
        self.cursor = self.conn.cursor()

        # Create table if it doesn't exist
        self.cursor.execute('''CREATE TABLE IF NOT EXISTS employees (
                            id INTEGER PRIMARY KEY,
                            name TEXT,
                            email TEXT,
                            mobile TEXT,
                            dob TEXT,
                            gender TEXT,
                            address TEXT,
                            role TEXT,
                            post TEXT,
                            dept TEXT,
                            joining_date TEXT,
                            salary REAL,
                            work_ethic INTEGER,
                            soft_skills INTEGER,
                            attendance_punctuality INTEGER,
                            ethical_behavior INTEGER,
                            client_satisfaction INTEGER
                            )''')
        self.conn.commit()

        self.master.geometry("1260x800")
        self.master.title("Employee Details")

        self.background_image = Image.open("bgnew.png")
        self.background_photo = ImageTk.PhotoImage(self.background_image)

        self.background_label = tk.Label(self.master, image=self.background_photo)
        self.background_label.place(x=0, y=0, relwidth=1, relheight=1)

        self.heading_label = tk.Label(self.master, text="Welcome to Employees Vault", bg='#B29F9F',
                                      font=("Helvetica", 18, "bold"))
        self.heading_label.pack()

        self.add_employee_label = tk.Label(self.master, text="Employee Details", bg='#B29F9F',
                                           font=("Helvetica", 30, "bold"))
        self.add_employee_label.pack(ipadx=0, ipady=10, padx=0, pady=10, anchor='nw')

        self.employee_detail_label = tk.Label(self.master, text="Employee Detail", bg='#B29F9F',
                                              font=("Helvetica", 20, "bold"))
        self.employee_detail_label.place(x=70, y=150)

        self.work_place_detail_label = tk.Label(self.master, text="Work Place Detail", bg='#B29F9F',
                                                font=("Helvetica", 20, "bold"))
        self.work_place_detail_label.place(x=850, y=150)

        self.personal_detail_label = tk.Label(self.master, text="Personal Detail", bg='#B29F9F',
                                              font=("Helvetica", 20, "bold"))
        self.personal_detail_label.place(x=550, y=150)

        self.other_detail_label = tk.Label(self.master, text="OTHER Detail", bg='#B29F9F',
                                           font=("Helvetica", 20, "bold"))
        self.other_detail_label.place(x=550, y=400)

        self.other_detail_label = tk.Label(self.master, text="POINT'S FOR RANKING", bg='#B29F9F',
                                           font=("Helvetica", 20, "bold"))
        self.other_detail_label.place(x=920, y=400)



        self.back_button = tk.Button(self.master, text="Back", font=("Helvetica", 10, "bold"), command=self.back,
                                     width=20, height=1, bg="red", fg="white")
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

        self.generate_button = tk.Button(self.master, text="Generate Employee ID", command=self.get_employee_details,
                                         width=20, bg="black", fg="white")
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

        placeholder_text = ""
        self.WorkEthic_label = tk.Label(self.master, text="1.Work Ethic:", bg="#B29F9F", font=("Helvetica", 15, "bold"))
        self.WorkEthic_label.place(x=920, y=480)
        self.WorkEthic_entry = tk.Entry(self.master, width=10, font=('Arial', 12, 'bold'))
        self.WorkEthic_entry.insert(0, placeholder_text)
        self.WorkEthic_entry.place(x=1100, y=485)

        self.SoftSkills_label = tk.Label(self.master, text="2.Soft Skills:", bg="#B29F9F",
                                         font=("Helvetica", 15, "bold"))
        self.SoftSkills_label.place(x=920, y=540)
        self.SoftSkills_entry = tk.Entry(self.master, width=10, font=('Arial', 12, 'bold'))
        self.SoftSkills_entry.insert(0, placeholder_text)
        self.SoftSkills_entry.place(x=1100, y=545)

        self.AttendanceandPunctuality_label = tk.Label(self.master, text="3.Punctuality:", bg="#B29F9F",
                                                       font=("Helvetica", 15, "bold"))
        self.AttendanceandPunctuality_label.place(x=900, y=600)
        self.AttendanceandPunctuality_entry = tk.Entry(self.master, width=10, font=('Arial', 12, 'bold'))
        self.AttendanceandPunctuality_entry.insert(0, placeholder_text)
        self.AttendanceandPunctuality_entry.place(x=1100, y=605)

        self.EthicalBehavior_label = tk.Label(self.master, text="4.Ethical Behavior:", bg="#B29F9F",
                                              font=("Helvetica", 15, "bold"))
        self.EthicalBehavior_label.place(x=920, y=660)

        self.EthicalBehavior_entry = tk.Entry(self.master, width=10, font=('Arial', 12, 'bold'))
        self.EthicalBehavior_entry.insert(0, placeholder_text)
        self.EthicalBehavior_entry.place(x=1120, y=665)

        self.ClientSatisfaction_label = tk.Label(self.master, text="5.Client Satisfaction:", bg="#B29F9F",
                                                 font=("Helvetica", 15, "bold"))
        self.ClientSatisfaction_label.place(x=920, y=720)

        # Set a placeholder text as a hint
        placeholder_text = ""
        self.ClientSatisfaction_entry = tk.Entry(self.master, width=10, font=('Arial', 12, 'bold'))
        self.ClientSatisfaction_entry.insert(0, placeholder_text)  # Insert placeholder text
        self.ClientSatisfaction_entry.place(x=1120, y=725)

    def get_employee_details(self):
       employee_id = self.empid_entry.get()
       self.cursor.execute("SELECT * FROM employees WHERE employee_id=?", (employee_id,))
       employee_details = self.cursor.fetchone()

       try:
          if employee_details:
            name = employee_details[1]
            email = employee_details[2]
            moblie = employee_details[3]
            dob = employee_details[5]
            gender = employee_details[6]
            address = employee_details[7]
            role = employee_details[8]
            post = employee_details[9]
            dept = employee_details[10]
            join = employee_details[11]
            salary = employee_details[12]
            worketh = employee_details[13]
            softsk = employee_details[14]
            atten = employee_details[15]
            behavio = employee_details[16]
            client = employee_details[17]

            self.name_entry.insert(0, name)
            self.email_entry.insert(0, email)
            self.mobile_entry.insert(0, moblie)
            self.dob_entry.insert(0, dob)
            self.gender_entry.insert(0, gender)
            self.address_entry.insert(0, address)
            self.role_entry.insert(0, role)
            self.post_entry.insert(0, post)
            self.dept_entry.insert(0, dept)
            self.joining_entry.insert(0, join)
            self.salary_entry.insert(0, salary)
            self.WorkEthic_entry.insert(0, worketh)
            self.SoftSkills_entry.insert(0, softsk)
            self.AttendanceandPunctuality_entry.insert(0, atten)
            self.EthicalBehavior_entry.insert(0, behavio)
            self.ClientSatisfaction_entry.insert(0, client)
          else:
            self.details_textarea.delete(1.0, tk.END)
            self.details_textarea.insert(tk.END, "Employee ID not found")
       except Exception as e:
    # Handle any exceptions here, such as database errors or other issues
          print("Error:", e)

    def update_employee_details(self):
        # Get employee ID from entry widget
        employee_id = self.emp_id_var.get()

        # Fetch all details from UI widgets
        name = self.name_entry.get()
        email = self.email_entry.get()
        mobile = self.mobile_entry.get()
        dob = self.dob_entry.get()
        gender = self.gender_entry.get()
        address = self.address_entry.get()
        role = self.role_entry.get()
        post = self.post_entry.get()
        dept = self.dept_entry.get()
        joining_date = self.joining_entry.get()
        salary = self.salary_entry.get()
        work_ethic = self.WorkEthic_entry.get()
        soft_skills = self.SoftSkills_entry.get()
        attendance_punctuality = self.AttendanceandPunctuality_entry.get()
        ethical_behavior = self.EthicalBehavior_entry.get()
        client_satisfaction = self.ClientSatisfaction_entry.get()

        # Update database with new details
        try:
            self.cursor.execute('''UPDATE employees SET 
                            name=?, email=?, mobile=?, dob=?, gender=?, address=?, role=?, post=?, department=?, 
                            joining_date=?, salary=?, work_ethic=?, soft_skills=?, attendance_punctuality=?, 
                            ethical_behavior=?, client_satisfaction=? WHERE id=?''',
                                (name, email, mobile, dob, gender, address, role, post, dept, joining_date, salary,
                                 work_ethic, soft_skills, attendance_punctuality, ethical_behavior, client_satisfaction,
                                 employee_id))
            self.conn.commit()

            # Show message box indicating successful update
            messagebox.showinfo("Success", "Employee details updated successfully!")

            # Send email notification
            msg = EmailMessage()
            msg['Subject'] = 'Employee Details Update'
            msg['From'] = 'againhastar@gmail.com'  # Change to your email address
            msg['To'] = email  # Send email to the updated employee
            msg.set_content(
                f"Dear {name},\n\nYour employee details have been updated successfully.\n\nRanking Point:\nWorkethic:{work_ethic}\nsoft_skills:{soft_skills}\nattendance_punctuality:{attendance_punctuality}\nethical_behavior:{ethical_behavior}\nclient_satisfaction:{client_satisfaction}\nRegards,\n[Punav_shigwan]")

            with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
                smtp.login('againhastar@gmail.com', 'dfjx fvjk rtsk ztqc')  # Replace with your email credentials
                smtp.send_message(msg)

        except Exception as e:
            # Show error message if update fails
            messagebox.showerror("Error", f"Failed to update employee details: {str(e)}")

    def delete_employee(self):
        employee_id = self.empid_entry.get()
        confirmation = messagebox.askyesno("Confirmation",
                                           f"Are you sure you want to delete employee with ID {employee_id}?")

        if confirmation:
            self.cursor.execute("DELETE FROM employees WHERE employee_id=?", (employee_id,))
            self.conn.commit()
            messagebox.showinfo("Success", f"Employee with ID {employee_id} deleted successfully.")
            # You may want to clear the entry fields after deletion
            self.clear_entry_fields()
        else:
            messagebox.showinfo("Deletion Cancelled", "Deletion operation cancelled.")

    def acer_win(self):
     self.master.destroy()

    # Create a new Tkinter window
     new_root = tk.Tk()

    # Assuming twotoggle is imported and App2 is defined in it,
    # create an instance of App2 and start the event loop
     twotoggle.App2(new_root)

    # Start the Tkinter event loop
     new_root.mainloop()


    def back(self):
        self.master.destroy()  # Destroy current window
        new_root = tk.Tk()  # Create a new Tkinter window
        main.App(new_root)  # Initialize the next page
        new_root.mainloop()


    def __del__(self):
      self.conn.close()

    def run(self):
        self.master.mainloop()


if __name__ == "__main__":
    root = tk.Tk()  # Creating the root window
    app = CustomTkinter(root)  # Passing the root window as master
    app.run()
