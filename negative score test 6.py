from tkinter import *
import random
from tkinter import messagebox

root = Tk()
root.title("ABC PAIRS")
root.config(bg="black")
root.geometry('600x640')

# Assign variables
score = 0
count_X = 0
count_O = 0
count_I = 0

score_x = 0
score_o = 0
score_i = 0

bol = True


class ABCPairs:
    def __init__(self, master):

        self.start_game()  # Start game message box

        self.top_frame = Frame(master)  # Creating frames
        self.top_frame.grid()

        self.middle_frame = Frame(master)
        self.middle_frame.grid()

        self.bottom_frame = Frame(master)
        self.bottom_frame.grid()

        self.buttons = [[Button(self.middle_frame, width=15, height=7, bg='sky blue',
                                command=lambda row=row, column=column: self.main_game(row, column))
                         for column in range(4)] for row in range(3)]

        for row in range(3):  # Creating buttons for 3 rows and 4 columns
            for column in range(4):
                self.buttons[row][column].grid(row=row + 1, column=column)  # Packing buttons to grid

        self.first_click = None
        self.draw_buttons()

        self.time_label = Label(self.top_frame, width=5, height=5, fg='red', bg="black")  # Creating labels
        self.instruction_label = Label(self.top_frame, text='Click a tile and click another to match it', fg="white",
                                       bg="black", width=45, height=5)
        self.level_label = Label(self.bottom_frame, text='Level : 1', width=55, height=3, bg="black", fg="white",
                                 font=20)
        self.score_label = Label(self.bottom_frame, width=55, height=4, bg="black", font=20)

        self.create_labels()
        self.count_down(60)  # Start countdown from 60 seconds

    def draw_buttons(self):
        self.answer = ['X', 'X', 'X', 'X', 'O', 'O', 'O', 'O', 'I', 'I', 'I', 'I']
        random.shuffle(self.answer)  # Randomly shuffling answers

        self.answer = [self.answer[0:4],  # Slicing list
                       self.answer[4:8],
                       self.answer[8:12]]

        for m in range(len(self.answer)):  # Print answer grid layout
            print(self.answer[m])

    def count_down(self, secs):
        global bol
        if bol is True:
            self.time_label.config(text="00:" + str(secs))  # Text of time label set to secs variable
            if secs > 0:
                self.top_frame.after(1000, self.count_down, secs - 1)
            if secs == 0:
                self.time_out()

    def create_labels(self):
        self.score_label.grid(row=6, column=0)

        self.level_label.grid(row=7, column=0)

        self.instruction_label.config(font=30)
        self.instruction_label.grid(row=0, column=3)

        self.time_label.config(font=30)
        self.time_label.grid(row=0, column=12)

    def main_game(self, row, column):

        # Assign a letter to a button Disable button when clicked
        self.buttons[row][column].config(text=self.answer[row][column], state=DISABLED)
        self.count(row, column)

        if self.first_click is None:  # if first clicked tile has no row or column to compare
            self.first_click = [row, column]  # Then assign coordinates to first click
        else:
            r, c = self.first_click  # r, c = coordinates of the first click

            # Check if the answer of first click is same as answer of second click
            if self.answer[r][c] == self.answer[row][column]:
                print('Match!')

                self.buttons[row][column].config(bg="light green")  # Change color of buttons when matched
                self.buttons[r][c].config(bg="light green")

                self.positive_scoring()  # Add score when two tiles are matched
                self.score_label.config(fg="white", text="Score: " + str(score))  # Show score on label
                self.first_click = None
                self.matched()  # call function to display message box if all 12 matched
            else:
                self.middle_frame.after(800, self.hide_buttons, row, column, r, c)  # Hide tiles if not matched
                print("No match! You suck!")

                self.negative_scoring()
                self.score_label.config(fg="white", text="Score:" + str(score))
                self.first_click = None

    def hide_buttons(self, row_a, column_a, row_b, column_b):
        self.buttons[row_a][column_a].config(text='', state=NORMAL)  # Reset first button if not matched
        self.buttons[row_b][column_b].config(text='', state=NORMAL)  # Reset second button if not matched

    def positive_scoring(self):  # score +20 if matched
        global score
        score = score + 20
        print("score:", score)

    def count(self, row, column):  # score -5 if not matched
        if self.first_click is not None:
            a, b = self.first_click  # coordinates of the first click
            print("a:", a)
            print("b:", b)
        '''else:
            print("im here")'''

        if self.answer[row][column] == "X":
            global count_X
            count_X += 1
            print("count x : ", count_X)

            if self.first_click is not None:
                a, b = self.first_click
                if self.answer[a][b] == self.answer[row][column] == "X":
                    count_X -= 1
                    print("count x : ", count_X)
                    print("haha1")

        elif self.answer[row][column] == "O":
            global count_O
            count_O += 1
            print("count o : ", count_O)

            if self.first_click is not None:
                a, b = self.first_click
                if self.answer[a][b] == self.answer[row][column] == "O":
                    count_O -= 1
                    print("count o : ", count_O)
                    print("haha2")

        elif self.answer[row][column] == "I":
            global count_I
            count_I += 1
            print("count I : ", count_I)

            if self.first_click is not None:
                a, b = self.first_click
                if self.answer[a][b] == self.answer[row][column] == "I":
                    count_I -= 1
                    print("count I : ", count_I)
                    print("haha3")

    def negative_scoring(self):
        global score_x
        global score_o
        global score_i
        global score

        if count_X == 1:
            score_x = 0
        if count_X > 1:
            score_x = count_X * (-5)
            print("score_x:", score_x)

        if count_O == 1:
            score_o = 0
        if count_O > 1:
            score_o = count_O * (-5)
            print("score_o:", score_o)

        if count_I == 1:
            score_i = 0
        if count_I > 1:
            score_i = count_I * (-5)
            print("score_i:", score_i)

        score = score + score_x + score_o + score_i
        print(score)

    def matched(self):  # check if all 12 tiles are matched and display message box
        global bol
        count = 0
        for row in range(3):
            for column in range(4):
                if self.buttons[row][column]["state"] == DISABLED:
                    count += 1
                    if count == 12:
                        print("You Win!")
                        bol = False
                        self.end_game()

    def start_game(self):
        messagebox.showinfo("ABC PAIRS", "Click a tile then click another to match it! \n "
                                         "Do you want to start game?")

    def end_game(self):
        messagebox.showinfo("ABC PAIRS", "You Win! \n Your Score : ")
        if messagebox.askyesno("ABC PAIRS", "Do you wish to play again?"):
            self.replay_game()
            print("OK")
        else:
            root.quit()

    def time_out(self):
        messagebox.showinfo("ABC PAIRS", "Out of time! \n You suck!")
        root.quit()

    def replay_game(self):
        global bol
        bol = True

        self.draw_buttons()
        self.reset_all()
        self.count_down(60)
        self.create_labels()

    def reset_all(self):
        global score
        global count_X
        global count_O
        global count_I
        global score_x
        global score_o
        global score_i

        for row in range(3):
            for column in range(4):
                self.buttons[row][column].config(text='', state=NORMAL)

                score = 0
                count_X = 0
                count_O = 0
                count_I = 0
                score_x = 0
                score_o = 0
                score_i = 0
                print(score)

                self.score_label.config(text="")
                self.buttons[row][column].config(bg="sky blue")


X = ABCPairs(root)
root.mainloop()