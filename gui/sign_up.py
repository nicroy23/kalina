from tkinter import *
from actions import File
from gui import LoginWindow


class SignUpWindow:
    def __init__(self):
        self.create_elements()
        self.open_window()

    def create_elements(self):
        """Create elements function

        This function creates all the elements necessary to the sign up gui window. It stores all of the elements
        in object properties.

        Args:
            none

        Returns:
            nothing
        """

        self.window = Tk()
        self.window.geometry("800x300")
        self.window.title("Kalina")

        self.main_frame = Frame(self.window, width=500, height=300)

        self.page_name_label = Label(self.main_frame, text="Get Started")
        self.page_name_label.config(font=("Roboto", 18))

        self.explain_text = """ Welcome to Kalina, a simple password manager to store all your different
        passwords. Your information is encrypted and therefore cannot be accessed
        by anyone except you. To get started, created a master password by 
        completing both text fields."""
        self.explain_label = Label(self.main_frame, text=self.explain_text)
        self.warning_label = Label(
            self.main_frame, text="***Warning, you cannot change your password after this.***", fg="red")

        self.enter_pwd_frame = Frame(self.main_frame)
        self.enter_pwd_label = Label(
            self.enter_pwd_frame, text="Enter master password: ")
        self.enter_pwd_input = Entry(self.enter_pwd_frame, show="*")

        self.reenter_pwd_frame = Frame(self.main_frame)
        self.reenter_pwd_label = Label(
            self.reenter_pwd_frame, text="Re-enter master password: ")
        self.reenter_pwd_input = Entry(self.reenter_pwd_frame, show="*")

        self.btn_frame = Frame(self.main_frame, height=60, width=500)
        self.create_btn = Button(
            self.btn_frame, text="Create", bg="green", command=self.verify_pwds)
        self.quit_btn = Button(self.btn_frame, text="Quit",
                               bg="red", command=lambda: exit())

        self.main_frame.pack()
        self.page_name_label.grid(pady=5)
        self.explain_label.grid(pady=5)
        self.warning_label.grid(pady=2)
        self.enter_pwd_frame.grid(pady=5)
        self.enter_pwd_label.grid()
        self.enter_pwd_input.grid()
        self.reenter_pwd_frame.grid(pady=5)
        self.btn_frame.grid()
        self.create_btn.grid(row=0, column=1)
        self.quit_btn.grid(row=0, column=0)
        self.reenter_pwd_label.grid()
        self.reenter_pwd_input.grid()

    def open_window(self):
        """Opens the window

        This function opens the sign up window that has been created.

        Args:
            none

        Returns:
            nothing
        """
        self.window.mainloop()

    def verify_pwds(self):
        pass1 = self.enter_pwd_input.get()
        pass2 = self.reenter_pwd_input.get()

        if pass1 != "" and pass2 != "" and pass1 == pass2:
            File.create_file(pass1)
            self.window.destroy()
            LoginWindow()
