from tkinter import *
from tkinter import messagebox
from actions import File

import gui


class LoginWindow:
    def __init__(self):
        self.create_elements()
        self.open_window()

    def create_elements(self):
        self.window = Tk()
        self.window.geometry("400x200")
        self.window.title("Kalina")

        self.main_frame = Frame(self.window, width=400, height=200)

        self.app_name_label = Label(self.main_frame, text="Login")
        self.app_name_label.config(font=("Roboto", 18))

        self.master_pwd_label = Label(
            self.main_frame,
            text="Enter the master password: ", pady=5)
        self.master_pwd_label.config(font=("Roboto", 12))

        self.master_pwd_input = Entry(self.main_frame, show="*")

        self.btn_frame = Frame(self.main_frame, width=400, height=60)
        self.login_btn = Button(
            self.btn_frame, text="Login", bg="green", command=self.try_reading_pass_file)
        self.quit_btn = Button(self.btn_frame, text="Quit",
                               bg="red", command=lambda: exit())

        self.main_frame.pack()
        self.app_name_label.grid(column=1, pady=20)
        self.master_pwd_label.grid(column=1, pady=5)
        self.master_pwd_input.grid(column=1)
        self.btn_frame.grid(column=1, pady=10)
        self.login_btn.grid(row=0, column=1)
        self.quit_btn.grid(row=0, column=0)

    def open_window(self):
        self.window.mainloop()

    def try_reading_pass_file(self):
        pwd = self.master_pwd_input.get()

        read_file = File.read_file(pwd)

        if read_file["validated"]:
            print(read_file)
            gui.MainWindow(read_file["data"])
            self.window.destroy()
        else:
            messagebox.showerror(title="Error", message="Wrong password!")
