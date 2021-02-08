import time
from tkinter import *
root = Tk()
top_frame = Frame()


def countdown():
    for seconds in range(60, 0, -1):
        print(seconds)
        time.sleep(1)

countdown()

'''countdown()
time_label = Label(top_frame, text="time", height=3, width=8)
time_label.grid(row=0, column=0)'''

print("Game over!")

root.mainloop()





