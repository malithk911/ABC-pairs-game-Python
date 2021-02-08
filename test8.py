import random
from tkinter import *

root = Tk()


# printing each sliced list in new line
class GUI:
    def __init__(self, master):

        self.topframe = Frame(master)
        self.topframe.pack()

        self.bottomframe = Frame(master)
        self.bottomframe.pack()

        self.time_label = Label(self.topframe, width=12, height=3, fg='green')
        self.instruction_label = Label(self.topframe, text='Click a tile and try to match it', fg="red", width=25,
                                       height=2)
        self.level_label = Label(self.bottomframe, text='Level : 1', width=15, height=4)
        self.score_label = Label(self.bottomframe, text='Score : ', width=15, height=4)

        self.labels()
        self.countdown(60)

        answer = list('XXXXOOOOIIII')
        random.shuffle(answer)

        # slicing list
        answer = [answer[:4],
                  answer[4:8],
                  answer[8:]]

        for row in range(3):
            for column in range(4):
                self.button_x = Button(self.bottomframe, text=answer[row][column],
                                       width=16, height=6, fg='blue', bg='beige')
                self.button_x.grid(row=row + 1, column=column)

    def countdown(self, secs):
        self.time_label['text'] = secs
        if secs > 0:
            self.topframe.after(1000, self.countdown, secs-1)

    def labels(self):
        self.score_label.grid(row=6, column=0)

        self.level_label.grid(row=7, column=0)

        self.instruction_label.config(font=40)
        self.instruction_label.pack()

        self.time_label.config(font=40)
        self.time_label.pack()


X = GUI(root)
root.mainloop()
