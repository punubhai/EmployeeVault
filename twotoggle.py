from tkinter import *
from PIL import ImageTk, Image
import new_employee
import pratice3
import edit

import main

class App2:
    def __init__(self, master):

        self.master = master
        self.master.geometry('1500x1000')
        self.master.configure(bg='#262626')
        self.master.title('EMPLOYEE VAULT')

        self.toggle_background = ImageTk.PhotoImage(Image.open("TWO.jpg").resize((self.master.winfo_screenwidth(), self.master.winfo_screenheight())))

        self.l1 = Label(self.master, text='', fg='white', bg='#262626', image=self.toggle_background)
        self.l1.config(font=('Comic Sans MS', 90))
        self.l1.pack(expand=True)

        self.img1 = ImageTk.PhotoImage(Image.open("open.png"))

        self.create_toggle_button()

    def create_toggle_button(self):
        self.toggle_button = Button(self.master, image=self.img1,
                               command=self.toggle_win,
                               border=0,
                               bg='#262626',
                               activebackground='#262626',
                               foreground ="#D9F1FF"
                                    )
        self.toggle_button.place(x=5, y=10)

    def toggle_win(self):
        self.f1 = Frame(self.master, width=300, height=1000, bg='#640D14')
        self.f1.place(x=0, y=0)

        self.create_buttons()

        # Close button
        self.img2 = ImageTk.PhotoImage(Image.open("close.png"))
        Button(self.f1,
               image=self.img2,
               border=0,
               command=self.dele,
               bg='#12c4c0',
               activebackground='#12c4c0'
               ).place(x=5, y=10)

    def create_buttons(self):
        buttons_info = [
            (0, 80, ' E D I T', '#0f9d9a', '#640D14', self.acer_win),
            (0, 117, 'N E W ENTRY', '#0f9d9a', '#640D14', self.detail),
            (0, 720, 'B A C K', '#0f9d9a', '#DC4116', self.back)

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

    def acer_win(self):
        self.master.destroy()
        root = Tk()
        edit.CustomTkinter(root)
        root.mainloop()

    def detail(self):
        self.master.destroy()
        root = Tk()
        new_employee.CustomTkinter(root)
        root.mainloop()

    def back(self):
        self.master.destroy()  # Destroy current window
        new_root = Tk()  # Create a new Tkinter window
        main.App(new_root)  # Initialize the next page
        new_root.mainloop()

    def run(self):
        self.master.mainloop()

if __name__ == "__main__":
    root = Tk()
    app = App2(root)  # Pass root as the master argument
    app.run()
