from tkinter import *
import random

root = Tk()
root.title("ABC Pairs")
root.geometry('500x600')


class GUI:
    def __init__(self, master):

        self.first_click = None

        self.top_frame = Frame(master)  # Creating frames
        self.top_frame.pack()

        self.middle_frame = Frame(master)
        self.middle_frame.pack()

        self.bottom_frame = Frame(master)
        self.bottom_frame.pack()

        self.time_label = Label(self.top_frame, width=12, height=3, fg='green')  # Creating labels
        self.instruction_label = Label(self.top_frame, text='Click a tile and try to match it', fg="red", width=25,
                                       height=2)
        self.level_label = Label(self.bottom_frame, text='Level : 1', width=15, height=2)
        self.score_label = Label(self.bottom_frame, text='Score : ', width=15, height=2)

        self.labels()
        self.count_down(60)
        self.draw_tiles()

    def draw_tiles(self):
        self.answer = list('XXXXOOOOIIII')
        random.shuffle(self.answer)

        self.answer = [self.answer[:4],
                       self.answer[4:8],
                       self.answer[8:12]]

        for m in range(len(self.answer)):  # Print grid
            print(self.answer[m])

        self.buttons = [[Button(self.middle_frame, width=15, height=7, bg='beige',
                                command=lambda row=row, column=column: self.click_event(row, column)
                                ) for column in range(4)] for row in range(3)]

        for row in range(3):
            for column in range(4):
                self.buttons[row][column].grid(row=row + 1, column=column)

    def count_down(self, secs):
        self.time_label['text'] = secs
        if secs > 0:
            self.top_frame.after(1000, self.count_down, secs - 1)

    def labels(self):
        self.score_label.grid(row=6, column=0)
        self.score_label.config(font=10)

        self.level_label.grid(row=7, column=0)
        self.level_label.config(font=10)

        self.instruction_label.config(font=40)
        self.instruction_label.pack()

        self.time_label.config(font=40)
        self.time_label.pack()

    def click_event(self, row, column):
        self.buttons[row][column].config(text=self.answer[row][column])
        self.buttons[row][column].config(state=DISABLED)
        self.first_click = row, column
        x, y = self.first_click
        if self.answer[row][column] == self.first_click[x][y]:
            print('match!')
        else:
            print('no match!')


X = GUI(root)
root.mainloop()
