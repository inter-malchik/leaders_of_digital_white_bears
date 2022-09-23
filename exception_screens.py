import tkinter
from tkinter import messagebox


def throw_error_window(error_message: str, window_name: str = "App error"):
    root = tkinter.Tk()
    root.withdraw()
    messagebox.showerror(window_name, error_message)
    root.destroy()


def throw_info_window(info_message: str, window_name: str = "App error"):
    root = tkinter.Tk()
    root.withdraw()
    messagebox.showinfo(window_name, info_message)
    root.destroy()


def throw_warning_window(warning_message: str, window_name: str = "App error"):
    root = tkinter.Tk()
    root.withdraw()
    messagebox.showwarning(window_name, warning_message)
    root.destroy()
