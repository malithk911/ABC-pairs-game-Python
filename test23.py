from tkinter import *
import random
root = Tk()
root.title("ABC Pairs Game")
root.geometry('500x600')


class ABCPairs:
    def __init__(self, master):

        self.top_frame = Frame(master)  # Creating frames
        self.top_frame.pack()

        self.middle_frame = Frame(master)
        self.middle_frame.pack()

        self.bottom_frame = Frame(master)
        self.bottom_frame.pack()

        self.buttons = [[Button(self.middle_frame, width=15, height=7, bg='light blue',
                                command=lambda row=row, column=column: self.click_event(row, column))
                         for column in range(4)] for row in range(3)]

        for row in range(3):  # Creating buttons
            for column in range(4):
                self.buttons[row][column].grid(row=row + 1, column=column)  # Packing buttons to grid

        self.first_click = None
        self.draw_tiles()

        self.time_label = Label(self.top_frame, width=12, height=3, fg='red')  # Creating labels
        self.instruction_label = Label(self.top_frame, text='Click a tile and try to match it', fg="black", width=25,
                                       height=2)
        self.level_label = Label(self.bottom_frame, text='Level : 1', width=15, height=2)
        self.score_label = Label(self.bottom_frame, text='Score : ', width=15, height=2)

        self.labels()
        self.count_down(60)  # Start countdown from 60 seconds

    def draw_tiles(self):
        self.answer = list('XXXXOOOOIIII')
        random.shuffle(self.answer)   # Randomly shuffling answers

        self.answer = [self.answer[0:4],   # Slicing list
                       self.answer[4:8],
                       self.answer[8:12]]

        for m in range(len(self.answer)):  # Print answer grid layout
            print(self.answer[m])

    def count_down(self, secs):
        self.time_label['text'] = secs  # Text of time label set to secs variable
        if secs > 0:
            self.top_frame.after(1000, self.count_down, secs-1)

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
        score_1 = 0
        score_2 = 0
        self.buttons[row][column].config(text=self.answer[row][column])  # Assign a letter to a button
        self.buttons[row][column].config(state=DISABLED)  # Disable button when clicked

        if self.first_click is None:
            self.first_click = (row, column)
        else:
            r, c = self.first_click

            if self.answer[row][column] == self.answer[r][c]:
                print('Match!')
                self.positive_scoring(score_1)  # Calling scoring function
                self.first_click = None

            else:
                self.middle_frame.after(800, self.reset_buttons, row, column, r, c)
                print("No match! You suck!")
                self.negative_scoring(score_2)  # Calling scoring function
                self.first_click = None

    def reset_buttons(self, row_a, column_a, row_b, column_b):
        self.buttons[row_a][column_a].config(text='', state=NORMAL)
        self.buttons[row_b][column_b].config(text='', state=NORMAL)

    @staticmethod
    def positive_scoring(score_1):
        '''score_1 = score_1'''
        score_1 += 20
        print("score:", score_1)

    @staticmethod
    def negative_scoring(score_2):
        '''score_2 = score_2'''
        score_2 -= 5
        print("score:", score_2)


X = ABCPairs(root)
root.mainloop()
