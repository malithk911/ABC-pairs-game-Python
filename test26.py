from tkinter import *
import random

root = Tk()
root.title("ABC PAIRS GAME")
root.config(bg="lavender")
root.geometry('600x640')

score = 0


class ABCPairs:
    def __init__(self, master):

        self.top_frame = Frame(master)  # Creating frames
        self.top_frame.grid()

        self.middle_frame = Frame(master)
        self.middle_frame.grid()

        self.bottom_frame = Frame(master)
        self.bottom_frame.grid()

        self.buttons = [[Button(self.middle_frame, width=15, height=7, bg='sky blue',
                                command=lambda row=row, column=column: self.click_event(row, column))
                        for column in range(4)] for row in range(3)]

        for row in range(3):  # Creating buttons
            for column in range(4):
                self.buttons[row][column].grid(row=row + 1, column=column)  # Packing buttons to grid

        self.first_click = None
        self.draw_buttons()

        self.time_label = Label(self.top_frame, width=5, height=5, fg='red', bg="lavender")  # Creating labels
        self.instruction_label = Label(self.top_frame, text='Click a tile and click another to match it', fg="black",
                                       bg="lavender", width=45, height=5)
        self.level_label = Label(self.bottom_frame, text='Level : 1', width=55, height=3, bg="lavender", font=20)
        self.score_label = Label(self.bottom_frame, width=55, height=4, bg="lavender", font=20)

        self.create_labels()
        self.count_down(60)  # Start countdown from 60 seconds

    def draw_buttons(self):
        self.answer = ['X', 'X', 'X', 'X', 'O', 'O', 'O', 'O', 'I', 'I', 'I', 'I']
        random.shuffle(self.answer)   # Randomly shuffling answers

        self.answer = [self.answer[0:4],   # Slicing list
                       self.answer[4:8],
                       self.answer[8:12]]

        for m in range(len(self.answer)):  # Print answer grid layout
            print(self.answer[m])

    def count_down(self, secs):
        self.time_label.config(text="00:" + str(secs))  # Text of time label set to secs variable
        if secs > 0:
            self.top_frame.after(1000, self.count_down, secs-1)

    def create_labels(self):
        self.score_label.grid(row=6, column=0)

        self.level_label.grid(row=7, column=0)

        self.instruction_label.config(font=30)
        self.instruction_label.grid(row=0, column=3)

        self.time_label.config(font=30)
        self.time_label.grid(row=0, column=12)

    def click_event(self, row, column):
        self.buttons[row][column].config(text=self.answer[row][column])  # Assign a letter to a button
        self.buttons[row][column].config(state=DISABLED)  # Disable button when clicked

        if self.first_click is None:
            self.first_click = (row, column)
        else:
            r, c = self.first_click

            if self.answer[row][column] == self.answer[r][c]:
                print('Match!')

                self.buttons[row][column].config(bg="light green")  # Change color of buttons when matched
                self.buttons[r][c].config(bg="light green")

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
        self.buttons[row_a][column_a].config(text='', state=NORMAL)
        self.buttons[row_b][column_b].config(text='', state=NORMAL)

    def positive_scoring(self):
        global score
        score = score+20
        print("score:", score)

    def negative_scoring(self):
        global score
        score = score-5
        print("score:", score)


        #write a line to stop the timer when all tiles are matched
        #add message box to display start button, quit and display score.
        #add a message box to show the total score
        #make level 2 - reveal the grid initially for 8 seconds


X = ABCPairs(root)
root.mainloop()
