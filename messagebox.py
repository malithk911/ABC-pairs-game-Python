import tkinter
from tkinter import messagebox

# hide main window
root = tkinter.Tk()
root.withdraw()

# message box display
messagebox.showinfo("ABC PAIRS", "Your score is: ")
messagebox.askyesno("ABC PAIRS", "Do you want to play again?")

