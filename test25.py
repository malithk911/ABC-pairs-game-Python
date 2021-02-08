from tkinter import *
import random
root = Tk()
root.title("ABC PAIRS GAME")
root.geometry('600x600')
score = 0


class ABCPairs:
    def __init__(self, master):

        self.top_frame = Frame(master)  # Creating frames
        self.top_frame.grid()

        self.middle_frame = Frame(master)
        self.middle_frame.grid()

        self.bottom_frame = Frame(master)
        self.bottom_frame.grid()

        self.buttons = [[Button(self.middle_frame, width=15, height=7, bg='light blue',
                                command=lambda row=row, column=column: self.click_event(row, column))
                         for column in range(4)] for row in range(3)]

        for row in range(3):  # Creating buttons
            for column in range(4):
                self.buttons[row][column].grid(row=row + 1, column=column)  # Packing buttons to grid

        self.first_click = None
        self.draw_tiles()

        self.time_label = Label(self.top_frame, width=8, height=3, fg='red')  # Creating labels
        self.instruction_label = Label(self.top_frame, text='Click a tile and try to match it', fg="black", width=45,
                                       height=5)
        self.level_label = Label(self.bottom_frame, font=6, text='Level : 1', width=15, height=2)
        self.score_label = Label(self.bottom_frame, font=6, width=15, height=2)

        self.labels()
        self.count_down(60)  # Start countdown from 60 seconds

    def draw_tiles(self):
        img1 = PhotoImage(file="fox-face_1f98a.png")
        img2 = PhotoImage(file="tiger-face_1f42f.png")
        img3 = PhotoImage(file="hamster-face_1f439.png")

        self.answer = [img1, img1, img1, img1, img2, img2, img2, img2, img3, img3, img3, img3]
        random.shuffle(self.answer)   # Randomly shuffling answers

        self.answer = [self.answer[0:4],   # Slicing list
                       self.answer[4:8],
                       self.answer[8:12]]

        for m in range(len(self.answer)):  # Print answer grid layout
            print(self.answer[m])

    def count_down(self, sec):
        self.time_label['text'] = sec  # Text of time label set to secs variable
        if sec > 0:
            self.top_frame.after(1000, self.count_down, sec-1)

    def labels(self):
        self.score_label.grid(row=6, column=0)

        self.level_label.grid(row=7, column=0)
        self.level_label.config(font=10)

        self.instruction_label.config(font=40)
        self.instruction_label.grid(row=0, column=3)

        self.time_label.config(font=40)
        self.time_label.grid(row=0, column=12)

    def click_event(self, row, column):
        self.buttons[row][column].config(image=self.answer[row][column])  # Assign a letter to a button
        self.buttons[row][column].config(state=DISABLED)  # Disable button when clicked

        if self.first_click is None:
            self.first_click = (row, column)
        else:
            r, c = self.first_click

            if self.answer[row][column] == self.answer[r][c]:
                print('Match!')
                self.positive_scoring()
                self.score_label.config(text="Score: " + str(score))
                self.first_click = None

            else:
                self.middle_frame.after(800, self.reset_buttons, row, column, r, c)
                print("No match! You suck!")
                self.negative_scoring()
                self.score_label.config(text="Score:" + str(score))
                self.first_click = None

    def reset_buttons(self, row_a, column_a, row_b, column_b):
        self.buttons[row_a][column_a].config(image='', state=NORMAL)
        self.buttons[row_b][column_b].config(image='', state=NORMAL)

    def positive_scoring(self):
        global score
        score = score+20
        print("score:", score)

    def negative_scoring(self):
        global score
        score = score-5
        print("score:", score)


X = ABCPairs(root)
root.mainloop()
