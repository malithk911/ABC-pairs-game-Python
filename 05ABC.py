from tkinter import *
import random

root = Tk()

answer = list('AABBCCXXYYZZ')
random.shuffle(answer)

answer = [answer[:4],
          answer[4:8],
          answer[8:]]
print(answer)

class Pairs:
    def __init__(self, parent):
        self.parent = parent
        for m in range(len(answer)):
            print(answer[m])
    for n in range(3):
        for y in range(4):
            row1 = Button(text=(answer[n][y]), width=8, height=4)
            row1.grid(row=n + 1, column=y)

messagelabel = Label(text="Start game")
messagelabel.grid(row=0)

scorelabel = Label(text="Score :")
scorelabel.grid(row=4, column=1)

levellabel = Label(text="Level :")
levellabel.grid(row=5, column=1)

root.mainloop()
