from tkinter import *
from tkinter import messagebox
import attendance
import twotoggle
from PIL import ImageTk, Image
import Detail
import praticerank



class App:
    def __init__(self, master):
        self.master = master
        self.master.geometry('1500x1000')
        self.master.configure(bg='#262626')
        self.master.title('EMPLOYEE VAULT')

        self.toggle_background = ImageTk.PhotoImage(Image.open("main_page img.jpg").resize((self.master.winfo_screenwidth(), self.master.winfo_screenheight())))
        self.l1 = Label(self.master, text='', fg='white', bg='#262626', image=self.toggle_background)
        self.l1.config(font=('Comic Sans MS', 90))
        self.l1.pack(expand=True)

        self.img1 = ImageTk.PhotoImage(Image.open("open.png"))
        self.create_toggle_button()

    def create_toggle_button(self):
        self.toggle_button = Button(self.master, image=self.img1,
                                    command=self.toggle_win,
                                    border=0,
                                    bg='#067C7D',
                                    activebackground='#611E22')
        self.toggle_button.place(x=5, y=10)

    def toggle_win(self):
        self.f1 = Frame(self.master, width=300, height=1000, bg='#067C7D')
        self.f1.place(x=0, y=0)
        self.create_buttons()

        # Close button
        self.img2 = ImageTk.PhotoImage(Image.open("close.png"))
        Button(self.f1,
               image=self.img2,
               border=0,
               command=self.dele,
               bg='#067C7D',
               activebackground='#FF81E6').place(x=5, y=10)

    def change_main_frame(self):
        # Call method to create a new frame
        new_frame = self.create_new_main_frame()

        # Configure the main frame content with the new image
        self.l1.config(image=new_frame)
        self.l1.image = new_frame  # Keep a reference to prevent garbage collection

    def create_new_main_frame(self):
    # Create and configure the new frame with the new image
     new_image = ImageTk.PhotoImage(Image.open("loginimg.jpg").resize((self.master.winfo_screenwidth(), self.master.winfo_screenheight())))

    # Create label for username
     username_label = Label(self.l1, text="Username:", font=("Arial", 12, "bold"), bg="#611E22")
     username_label.place(x=1050, y=537)

    # Create text field for username
     self.username_entry = Entry(self.l1, width=25)
     self.username_entry.place(x=1150, y=542)

    # Create label for password
     password_label = Label(self.l1, text="Password:", font=("Arial", 12, "bold"), bg="#611E22")
     password_label.place(x=1050, y=637)

    # Create text field for password
     self.password_entry = Entry(self.l1, width=25, show="*")
     self.password_entry.place(x=1150, y=642)

    # Create button to submit login credentials
     submit_button = Button(self.l1, text="Enter", bg='#6F1712' ,width=20, command=self.validate_login)
     submit_button.place(x=1150, y=700)

     return new_image





    def validate_login(self):
    # Get username and password entered by the user
     username = self.username_entry.get()
     password = self.password_entry.get()

    # Check if username and password are correct
     if username == "ADMIN" and password == "PASSWORD":
        self.master.destroy()  # Destroy current window
        new_root = Tk()  # Create a new Tkinter window
        twotoggle.App2(new_root)  # Initialize the next page
        new_root.mainloop()
     else:
        # If incorrect, display an error message
         messagebox.showerror("Error", "Invalid username or password")
    def create_buttons(self):
        buttons_info = [
            (0, 80, ' A D M I N LOGIN', '#067C7D', '#067C7D', self.change_main_frame),
            (0, 130, 'D E T A I L', '#067C7D', '#067C7D', self.detail),
            (0, 170, 'R A N K', '#067C7D', '#067C7D',self.rank),
            (0, 220, 'A T T E N D A N C E S', '#067C7D', '#067C7D', self.attend),
        ]

        for info in buttons_info:
            self.create_button(*info)

    def create_button(self, x, y, text, bcolor, fcolor, cmd):
        def on_enter(e):
            button['background'] = bcolor
            button['foreground'] = '#262626'

        def on_leave(e):
            button['background'] = fcolor
            button['foreground'] = '#262626'

        button = Button(self.f1, text=text,
                        width=42,
                        height=2,
                        fg='black',
                        font=('Arial', 10, 'bold'),
                        border=0,
                        bg=fcolor,
                        activeforeground='#262626',
                        activebackground=bcolor,
                        command=lambda: cmd())

        button.bind("<Enter>", on_enter)
        button.bind("<Leave>", on_leave)
        button.place(x=x, y=y)

    def dele(self):
        self.f1.destroy()

    def detail(self):
        self.master.destroy()
        root = Tk()
        Detail.CustomTkinter(root)
        root.mainloop()

    def rank(self):
        self.master.destroy()
        root = Tk()
        praticerank.Rank(root)
        root.mainloop()

    def attend(self):
        self.master.destroy()  # Destroy current window
        new_root = Tk()  # Create a new Tkinter window
        attendance.EmployeeDatabaseApp(new_root)  # Initialize the next page
        new_root.mainloop()



    def run(self):
        self.master.mainloop()

if __name__ == "__main__":
    root = Tk()
    app = App(root)
    app.run()
