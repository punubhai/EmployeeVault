import tkinter as tk
import sqlite3
import main

class Rank:
    def __init__(self, root):
        self.root = root
        self.root.title("Top Employees")
        self.root.configure(background='#B29F9F')

        self.conn = sqlite3.connect('employees.db')
        self.create_table()

        # Create GUI elements
        self.top_employees_label = tk.Label(root, text="Top Employees", background= '#B29F9F', font=("Helvetica", 30,'bold'))
        self.top_employees_label.pack(pady=10)

        self.back_button = tk.Button(root, text="Back", command=self.detail,background="black",font=("Helvetica", 10,'bold'),foreground='white')
        self.back_button.pack(pady=10, padx=10)

        self.canvas = tk.Canvas(root, width=1000, height=1000, bg="red", highlightthickness=2, highlightbackground="#B29F9F")
        self.canvas.pack()

        self.bg_image = tk.PhotoImage(file="img_4.png")  # Change to your image file path
        self.canvas.create_image(0, 0, anchor=tk.NW, image=self.bg_image)


        self.refresh_button = tk.Button(root, text="Refresh", command=self.display_top_employees)
        self.refresh_button.pack(pady=5)

        self.display_top_employees()

    def create_table(self):
        cursor = self.conn.cursor()
        cursor.execute('''CREATE TABLE IF NOT EXISTS employees
                          (id INTEGER PRIMARY KEY, name TEXT, email TEXT, mobile TEXT, employee_id TEXT,
                          dob TEXT, gender TEXT, address TEXT, role TEXT, post TEXT, department TEXT,
                          joining_date TEXT, salary TEXT, work_ethic TEXT, soft_skills TEXT,
                          attendance_punctuality TEXT, ethical_behavior TEXT, client_satisfaction TEXT)''')
        self.conn.commit()

    def calculate_scores(self):
        cursor = self.conn.cursor()
        cursor.execute('''SELECT name, work_ethic, soft_skills, attendance_punctuality, ethical_behavior, client_satisfaction FROM employees''')
        employees = cursor.fetchall()

        scores = []
        for employee in employees:
            total_score = sum(int(score) for score in employee[1:])
            scores.append((employee[0], total_score))

        scores.sort(key=lambda x: x[1], reverse=True)
        return scores

    def display_top_employees(self):
        self.canvas.delete("text")  # Clear existing text items

        scores = self.calculate_scores()
        top_employee_data = [(name.upper(), score) for name, score in scores if score > 0]  # Capitalize names and filter employees with score > 0

        # Create column headers
        header_x_offsets = [50, 150, 850]  # Adjusted x-coordinates for column headers
        column_headers = ["Rank", "Name", "Score"]
        for i, (header, x_offset) in enumerate(zip(column_headers, header_x_offsets)):
            self.canvas.create_text(x_offset, 30, anchor=tk.W, text=header, font=("Helvetica", 20, "bold"), fill="black", tag="text")

        y_offset = 80  # Initial y-coordinate for text, adjusted for larger text size
        for rank, (name, score) in enumerate(top_employee_data, start=1):
            self.canvas.create_text(header_x_offsets[0], y_offset, anchor=tk.W, text=str(rank), font=("Helvetica", 20 + 30), fill="black", tag="text")  # Increase font size by 40
            self.canvas.create_text(header_x_offsets[1], y_offset, anchor=tk.W, text=name, font=("Helvetica", 20 + 30), fill="black", tag="text")  # Increase font size by 40
            self.canvas.create_text(header_x_offsets[2], y_offset, anchor=tk.W, text=str(score), font=("Helvetica", 20 + 30), fill="black", tag="text")  # Increase font size by 40
            y_offset += 80  # Increment y-coordinate for next text item, adjusted for larger text size


    def detail(self):
        self.root.destroy()
        root = tk.Tk()
        main.App(root)
        root.mainloop()

    def __del__(self):
        self.conn.close()

# Create and run the GUI



