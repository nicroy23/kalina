import tkinter as tk
import gui
import actions.file as file
import actions


class MainWindow:
    def __init__(self, passwords: str):
        self.create_elements()
        self.add_app_entry()

    def create_elements(self):
        self.window = tk.Tk()
        self.window.geometry("600x400")
        self.window.title("Kalina")

        main_frame = tk.Frame(self.window, width=600, height=400)

        title_label = tk.Label(main_frame, text="Home", padx=10, pady=10)
        title_label.config(font=("Roboto", 20))

        self.passwords_frame = tk.Frame(main_frame, width=600)

        add_frame = tk.Frame(main_frame, width=600, bg="blue")
        add_btn = tk.Button(add_frame, text="+",
                            command=self.open_create_entry)

        main_frame.pack()
        title_label.grid(row=0, column=0)
        self.passwords_frame.grid()
        add_frame.grid()
        add_btn.grid()

    def open_window(self):
        self.window.mainloop()

    def open_create_entry(self):
        gui.PassPopUp(self)

    def add_app_entry(self):
        for child in self.passwords_frame.winfo_children():
            child.destroy()

        print(actions.Store.passwords)

        for item in actions.Store.passwords:
            frame = tk.Frame(self.passwords_frame)
            el_name = tk.Label(frame, text=item["name"])
            el_username = tk.Entry(frame)
            el_username.insert(0, item["username"])
            el_username_btn = tk.Button(
                frame, text="Copy", command=lambda: self.copy_to_clip(item["username"]))
            el_pass = tk.Entry(frame, show="*")
            el_pass.insert(0, item["password"])
            el_pass_btn = tk.Button(
                frame, text="Copy", command=lambda: self.copy_to_clip(item["password"]))

            frame.grid()
            el_name.grid(column=0, row=0)
            el_username.grid(column=1, row=0)
            el_username_btn.grid(column=2, row=0)
            el_pass.grid(column=3, row=0)
            el_pass_btn.grid(column=4, row=0)

    def copy_to_clip(self, value):
        self.window.clipboard_clear()
        self.window.clipboard_append(value)
        self.window.update()
