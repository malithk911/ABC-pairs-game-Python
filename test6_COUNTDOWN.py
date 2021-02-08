from tkinter import *
root = Tk()
top_frame = Frame(root)
top_frame.pack()


def countdown(secs):
    time_label['text'] = secs

    if secs > 0:
        top_frame.after(1000, countdown, secs-1)


time_label = Label(top_frame, width=12, height=3, fg='green')
time_label.config(font=40)
time_label.grid(row=2, column=2)

countdown(60)
root.mainloop()
