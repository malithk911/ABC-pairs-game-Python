from tkinter import*

root=Tk()

'''timelabel = Label(text='time:', width=8, height=2)'''

from datetime import datetime
def count_down(t):
    while t > 0:
        t = t-1
        print(t)
        if t == 0:
            time.sleep(1)
            print("Time's up!")
            count_down(60)

countdown(t)
root.mainloop()