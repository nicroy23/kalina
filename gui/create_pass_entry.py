from actions.store import Store
from actions.file import File
import tkinter as tk
import actions.all_entries as AE


class PassPopUp:
    def __init__(self, main_window):
        self.main_window = main_window
        self.create_elements()
        self.open()

    def create_elements(self):
        self.window = tk.Tk()
        self.window.geometry("300x250")
        self.window.title("Kalina - New entry")

        main_frame = tk.Frame(self.window, height=300, width=300)

        app_name_label = tk.Label(
            main_frame, text="Name of the app: ")
        self.app_name_entry = tk.Entry(main_frame)

        app_username_label = tk.Label(main_frame, text="Username: ")
        self.app_username_entry = tk.Entry(main_frame)

        pass_label = tk.Label(main_frame, text="Password: ")
        self.pass_entry = tk.Entry(main_frame)

        btn_frame = tk.Frame(main_frame, width=300)
        create_btn = tk.Button(btn_frame, text="Create",
                               bg="green", command=self.create)

        main_frame.pack()
        app_name_label.grid(pady=5)
        self.app_name_entry.grid(pady=5)
        app_username_label.grid(pady=5)
        self.app_username_entry.grid(pady=5)
        pass_label.grid(pady=5)
        self.pass_entry.grid(pady=5)
        btn_frame.grid()
        create_btn.grid(pady=10)

    def open(self):
        self.window.mainloop()

    def create(self):
        app_name = self.app_name_entry.get()
        username = self.app_username_entry.get()
        pass_entry = self.pass_entry.get()

        if app_name != "" and username != "" and pass_entry != "":
            #entries = File.get_entry_obj()
            #entries.add_to_list(app_name, username, pass_entry)
            entry = {
                "name": app_name,
                "username": username,
                "password": pass_entry
            }
            Store.passwords.append(entry)
            File.save()
            self.main_window.add_app_entry()
            self.window.destroy()
