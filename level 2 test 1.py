from tkinter import *
import random
from tkinter import messagebox

root = Tk()
root.title("ABC PAIRS")
root.config(bg="black")
root.geometry('600x640')

# count for buttons in first row
count00 = 0
count01 = 0
count02 = 0
count03 = 0
# count for buttons in second row
count10 = 0
count11 = 0
count12 = 0
count13 = 0
# count for buttons in third row
count20 = 0
count21 = 0
count22 = 0
count23 = 0
# score variables
score = 0
score_x = 0
score_o = 0
score_i = 0

bol = True
secs = 60


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
        self.answer = ""
        self.draw_buttons()

        self.time_label = Label(self.top_frame, width=5, height=5, fg='red', bg="black")  # Creating labels
        self.instruction_label = Label(self.top_frame, text='Click a tile and click another to match it', fg="white",
                                       bg="black", width=45, height=5)
        self.level_label = Label(self.bottom_frame, text='Level : 1', width=55, height=3, bg="black", fg="white",
                                 font=20)
        self.score_label = Label(self.bottom_frame, width=55, height=4, bg="black", font=20)

        self.create_labels()
        self.count_down()  # Start countdown from 60 seconds

    def draw_buttons(self):
        self.answer = ['X', 'X', 'X', 'X', 'O', 'O', 'O', 'O', 'I', 'I', 'I', 'I']
        random.shuffle(self.answer)  # Randomly shuffling answers

        self.answer = [self.answer[0:4],  # Slicing list
                       self.answer[4:8],
                       self.answer[8:12]]

        for m in range(len(self.answer)):  # Print answer grid layout
            print(self.answer[m])

    def count_down(self):
        global secs
        global bol
        if bol is True:
            self.time_label.config(text="00 : " + str(secs))  # Text of time label set to secs variable
            if secs > 0:
                secs = secs - 1
                self.top_frame.after(1000, self.count_down)
            if secs == 0:
                self.time_out()

    def create_labels(self):
        self.score_label.grid(row=6, column=0)  # score label

        self.level_label.grid(row=7, column=0)  # level label

        self.instruction_label.config(font=30)  # instruction label
        self.instruction_label.grid(row=0, column=3)

        self.time_label.config(font=30)   # time label
        self.time_label.grid(row=0, column=12)

    def main_game(self, row, column):
        # Assign a letter to a button Disable button when clicked
        self.buttons[row][column].config(text=self.answer[row][column], state=DISABLED)
        print(row, column)

        if self.first_click is None:  # if first clicked tile has no row or column to compare
            self.first_click = [row, column]  # Then assign coordinates to first click
            self.count(row, column)
        else:
            r, c = self.first_click  # r, c = coordinates of the first click

            # Check if the answer of first click is same as answer of second click
            if self.answer[r][c] == self.answer[row][column]:
                print('Match!')

                # Change color of buttons when matched
                self.buttons[row][column].config(bg="light green")
                self.buttons[r][c].config(bg="light green")

                self.positive_scoring()  # Add score when two tiles are matched
                self.score_label.config(fg="white", text="Score : " + str(score))  # Show score on label
                self.first_click = None
                self.matched()  # call function to display message box if all 12 matched
            else:
                self.count(r, c)
                self.middle_frame.after(800, self.hide_buttons, row, column, r, c)  # Hide tiles if not matched
                print("No match!")

                self.negative_scoring(row, column)
                self.score_label.config(fg="white", text="Score : " + str(score))
                self.first_click = None

    def hide_buttons(self, row_a, column_a, row_b, column_b):
        # Reset first button if not matched
        self.buttons[row_a][column_a].config(text='', state=NORMAL)
        # Reset second button if not matched
        self.buttons[row_b][column_b].config(text='', state=NORMAL)

    @staticmethod
    def count(row, column):  # score -5 if not matched
        global score

    # Increment count of the buttons in the first row
        if row == 0 and column == 0:
            global count00
            count00 += 1
            print(count00)
        elif row == 0 and column == 1:
            global count01
            count01 += 1
        elif row == 0 and column == 2:
            global count02
            count02 += 1
        elif row == 0 and column == 3:
            global count03
            count03 += 1

    # Increment count of the buttons in the second row
        if row == 1 and column == 0:
            global count10
            count10 += 1
        elif row == 1 and column == 1:
            global count11
            count11 += 1
        elif row == 1 and column == 2:
            global count12
            count12 += 1
        elif row == 1 and column == 3:
            global count13
            count13 += 1

    # Increment count of the buttons in the third row
        if row == 2 and column == 0:
            global count20
            count20 += 1
        elif row == 2 and column == 1:
            global count21
            count21 += 1
        elif row == 2 and column == 2:
            global count22
            count22 += 1
        elif row == 2 and column == 3:
            global count23
            count23 += 1

    @staticmethod
    def positive_scoring():  # score +20 if matched
        global score
        score = score + 20
        print("score:", score)

    def negative_scoring(self, row, column):
        global score_x
        global score_o
        global score_i
        global score

    # Calculating negative score for first row
        if row == 0 and column == 0:
            if self.answer[row][column] == "X":
                score_x = count00 * (-5)
            if self.answer[row][column] == "O":
                score_o = count00 * (-5)
            if self.answer[row][column] == "I":
                score_i = count00 * (-5)

        elif row == 0 and column == 1:
            if self.answer[row][column] == "X":
                score_x = count01 * (-5)
            if self.answer[row][column] == "O":
                score_o = count01 * (-5)
            if self.answer[row][column] == "I":
                score_i = count01 * (-5)

        elif row == 0 and column == 2:
            if self.answer[row][column] == "X":
                score_x = count02 * (-5)
            if self.answer[row][column] == "O":
                score_o = count02 * (-5)
            if self.answer[row][column] == "I":
                score_i = count02 * (-5)

        elif row == 0 and column == 3:
            if self.answer[row][column] == "X":
                score_x = count03 * (-5)
            if self.answer[row][column] == "O":
                score_o = count03 * (-5)
            if self.answer[row][column] == "I":
                score_i = count03 * (-5)

    # Calculating negative score for second row
        if row == 1 and column == 0:
            if self.answer[row][column] == "X":
                score_x = count10 * (-5)
            if self.answer[row][column] == "O":
                score_o = count10 * (-5)
            if self.answer[row][column] == "I":
                score_i = count10 * (-5)

        elif row == 1 and column == 1:
            if self.answer[row][column] == "X":
                score_x = count11 * (-5)
            if self.answer[row][column] == "O":
                score_o = count11 * (-5)
            if self.answer[row][column] == "I":
                score_i = count11 * (-5)

        elif row == 1 and column == 2:
            if self.answer[row][column] == "X":
                score_x = count12 * (-5)
            if self.answer[row][column] == "O":
                score_o = count12 * (-5)
            if self.answer[row][column] == "I":
                score_i = count12 * (-5)

        elif row == 1 and column == 3:
            if self.answer[row][column] == "X":
                score_x = count13 * (-5)
            if self.answer[row][column] == "O":
                score_o = count13 * (-5)
            if self.answer[row][column] == "I":
                score_i = count13 * (-5)

    # Calculating negative score for third row
        if row == 2 and column == 0:
            if self.answer[row][column] == "X":
                score_x = count20 * (-5)
            if self.answer[row][column] == "O":
                score_o = count20 * (-5)
            if self.answer[row][column] == "I":
                score_i = count20 * (-5)

        elif row == 2 and column == 1:
            if self.answer[row][column] == "X":
                score_x = count21 * (-5)
            if self.answer[row][column] == "O":
                score_o = count21 * (-5)
            if self.answer[row][column] == "I":
                score_i = count21 * (-5)

        elif row == 2 and column == 2:
            if self.answer[row][column] == "X":
                score_x = count22 * (-5)
            if self.answer[row][column] == "O":
                score_o = count22 * (-5)
            if self.answer[row][column] == "I":
                score_i = count22 * (-5)

        elif row == 2 and column == 3:
            if self.answer[row][column] == "X":
                score_x = count23 * (-5)
            if self.answer[row][column] == "O":
                score_o = count23 * (-5)
            if self.answer[row][column] == "I":
                score_i = count23 * (-5)

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

    @staticmethod
    def start_game():
        messagebox.showinfo("ABC PAIRS", "Click a tile then click another to match it! \n "
                                         "Do you want to start game?")

    def end_game(self):
        global secs
        messagebox.showinfo("ABC PAIRS", "You Win! \n Your Score : " + str(score) + " \n"
                                                                                    " Bonus : " + str(secs))
        if messagebox.askyesno("ABC PAIRS", "Do you wish to play again?"):
            self.replay_game()
            print("OK")
        else:
            root.quit()

    @staticmethod
    def time_out():
        messagebox.showinfo("ABC PAIRS", "Out of time! \n You suck!")
        root.quit()

    def replay_game(self):
        global bol
        bol = True
        global secs
        secs = 60

        self.draw_buttons()
        self.reset_all()
        self.count_down()
        self.create_labels()

    def reset_all(self):
        global score
        global score_x
        global score_o
        global score_i

        global count00
        global count01
        global count02
        global count03

        global count10
        global count11
        global count12
        global count13

        global count20
        global count21
        global count22
        global count23

        for row in range(3):
            for column in range(4):
                self.buttons[row][column].config(text='', state=NORMAL)

                score = 0
                score_x = 0
                score_o = 0
                score_i = 0
                # reset count for buttons in first row
                count00 = 0
                count01 = 0
                count02 = 0
                count03 = 0
                # reset count for buttons in second row
                count10 = 0
                count11 = 0
                count12 = 0
                count13 = 0
                # reset count for buttons in third row
                count20 = 0
                count21 = 0
                count22 = 0
                count23 = 0

                print(score)

                self.score_label.config(text="")
                self.buttons[row][column].config(bg="sky blue")


X = ABCPairs(root)
root.mainloop()
