from tkinter import *
import random
from tkinter import messagebox

root = Tk()
root.title("ABC PAIRS - 2018412")
root.config(bg="#008080")
# root.geometry('1920x1080')

# count for buttons in first row
count00 = (-1)
count01 = (-1)
count02 = (-1)
count03 = (-1)
# count for buttons in second row
count10 = (-1)
count11 = (-1)
count12 = (-1)
count13 = (-1)
# count for buttons in third row
count20 = (-1)
count21 = (-1)
count22 = (-1)
count23 = (-1)
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
        self.buttons = [[Button(self.middle_frame, width=10, height=5, bg='sky blue', font=40, text="",
                        command=lambda row=row, column=column: self.main_game(row, column))
                        for column in range(4)]for row in range(3)]

        for row in range(3):  # Creating buttons for 3 rows and 4 columns
            for column in range(4):
                self.buttons[row][column].grid(row=row + 1, column=column)  # Packing buttons to grid

        self.answer = []
        self.first_click = None
        self.draw_buttons()
        self.time_label = Label(self.top_frame, width=5, height=5, fg='#800000', bg="#008080")  # Creating labels
        self.instruction_label = Label(self.top_frame, text='Click a tile and click another to match it', fg="black",
                                       bg="#008080", width=45, height=5)
        self.level_label = Label(self.bottom_frame, text='Level : 1', width=55, height=3, bg="#008080", fg="black",
                                 font=20)
        self.score_label = Label(self.bottom_frame, width=55, height=2, bg="#008080", font=20)
        self.create_labels()
        self.count_down()  # Start countdown from 60 seconds

    def draw_buttons(self):
        self.answer = ['X', 'X', 'X', 'X', 'O', 'O', 'O', 'O', 'I', 'I', 'I', 'I']
        random.shuffle(self.answer)  # Randomly shuffling answers
        self.answer = [self.answer[0:4],  # Slicing list
                       self.answer[4:8],
                       self.answer[8:12]]
        for a in range(len(self.answer)):
            print(self.answer[a])

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
        self.time_label.config(font=30)  # time label
        self.time_label.grid(row=0, column=12)

    def main_game(self, row, column):
        # Assign a letter to a button Disable button when clicked
        self.buttons[row][column].config(text=self.answer[row][column], state=DISABLED)
        if self.first_click is None:  # if first clicked tile has no row or column to compare
            self.first_click = [row, column]  # Then assign coordinates to first click
            self.count(row, column)  # count button clicks
        else:
            r, c = self.first_click  # r, c = coordinates of the first click
            # Check if the answer of first click is same as answer of second click
            if self.answer[r][c] == self.answer[row][column]:
                # Change color of buttons when matched
                self.buttons[row][column].config(bg="#7CFC00")
                self.buttons[r][c].config(bg="#7CFC00")
                self.positive_scoring()  # Add score when two tiles are matched
                self.score_label.config(fg="black", text="Score : " + str(score))  # Show score on label
                self.first_click = None
                self.matched()  # call function to display message box if all 12 matched
            else:
                self.count(row, column)  # count button clicks
                self.middle_frame.after(800, self.hide_buttons, row, column, r, c)  # Hide tiles if not matched
                self.negative_scoring(r, c)
                self.score_label.config(fg="black", text="Score : " + str(score))
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

    def negative_scoring(self, row, column):
        global score_x
        global score_o
        global score_i
        global score
        # Calculating negative score for first row
        if row == 0 and column == 0:
            if self.answer[row][column] == "X":
                if count00 >= 1:
                    score_x = count00 * (-5)
            if self.answer[row][column] == "O":
                if count00 >= 1:
                    score_o = count00 * (-5)
            if self.answer[row][column] == "I":
                if count00 >= 1:
                    score_i = count00 * (-5)

        elif row == 0 and column == 1:
            if self.answer[row][column] == "X":
                if count01 >= 1:
                    score_x = count01 * (-5)
            if self.answer[row][column] == "O":
                if count01 >= 1:
                    score_o = count01 * (-5)
            if self.answer[row][column] == "I":
                if count01 >= 1:
                    score_i = count01 * (-5)

        elif row == 0 and column == 2:
            if self.answer[row][column] == "X":
                if count02 >= 1:
                    score_x = count02 * (-5)
            if self.answer[row][column] == "O":
                if count02 >= 1:
                    score_o = count02 * (-5)
            if self.answer[row][column] == "I":
                if count02 >= 1:
                    score_i = count02 * (-5)

        elif row == 0 and column == 3:
            if self.answer[row][column] == "X":
                if count03 >= 1:
                    score_x = count03 * (-5)
            if self.answer[row][column] == "O":
                if count03 >= 1:
                    score_o = count03 * (-5)
            if self.answer[row][column] == "I":
                if count03 >= 1:
                    score_i = count03 * (-5)

        # Calculating negative score for second row
        if row == 1 and column == 0:
            if self.answer[row][column] == "X":
                if count10 >= 1:
                    score_x = count10 * (-5)
            if self.answer[row][column] == "O":
                if count10 >= 1:
                    score_o = count10 * (-5)
            if self.answer[row][column] == "I":
                if count10 >= 1:
                    score_i = count10 * (-5)

        elif row == 1 and column == 1:
            if self.answer[row][column] == "X":
                if count11 >= 1:
                    score_x = count11 * (-5)
            if self.answer[row][column] == "O":
                if count11 >= 1:
                    score_o = count11 * (-5)
            if self.answer[row][column] == "I":
                if count11 >= 1:
                    score_i = count11 * (-5)

        elif row == 1 and column == 2:
            if self.answer[row][column] == "X":
                if count12 >= 1:
                    score_x = count12 * (-5)
            if self.answer[row][column] == "O":
                if count12 >= 1:
                    score_o = count12 * (-5)
            if self.answer[row][column] == "I":
                if count12 >= 1:
                    score_i = count12 * (-5)

        elif row == 1 and column == 3:
            if self.answer[row][column] == "X":
                if count13 >= 1:
                    score_x = count13 * (-5)
            if self.answer[row][column] == "O":
                if count13 >= 1:
                    score_o = count13 * (-5)
            if self.answer[row][column] == "I":
                if count13 >= 1:
                    score_i = count13 * (-5)

        # Calculating negative score for third row
        if row == 2 and column == 0:
            if self.answer[row][column] == "X":
                if count20 >= 1:
                    score_x = count20 * (-5)
            if self.answer[row][column] == "O":
                if count20 >= 1:
                    score_o = count20 * (-5)
            if self.answer[row][column] == "I":
                if count20 >= 1:
                    score_i = count20 * (-5)

        elif row == 2 and column == 1:
            if self.answer[row][column] == "X":
                if count21 >= 1:
                    score_x = count21 * (-5)
            if self.answer[row][column] == "O":
                if count21 >= 1:
                    score_o = count21 * (-5)
            if self.answer[row][column] == "I":
                if count21 >= 1:
                    score_i = count21 * (-5)

        elif row == 2 and column == 2:
            if self.answer[row][column] == "X":
                if count22 >= 1:
                    score_x = count22 * (-5)
            if self.answer[row][column] == "O":
                if count22 >= 1:
                    score_o = count22 * (-5)
            if self.answer[row][column] == "I":
                if count22 >= 1:
                    score_i = count22 * (-5)

        elif row == 2 and column == 3:
            if self.answer[row][column] == "X":
                if count23 >= 1:
                    score_x = count23 * (-5)
            if self.answer[row][column] == "O":
                if count23 >= 1:
                    score_o = count23 * (-5)
            if self.answer[row][column] == "I":
                if count23 >= 1:
                    score_i = count23 * (-5)

        score = score + score_x + score_o + score_i

    def matched(self):  # check if all 12 tiles are matched and display message box
        global bol
        count = 0
        for row in range(3):
            for column in range(4):
                if self.buttons[row][column]["state"] == DISABLED:
                    count += 1
                    if count == 12:
                        bol = False
                        self.end_game()

    @staticmethod
    def start_game():
        messagebox.showinfo("ABC PAIRS", "Click a tile then click another to match it! \n "
                                         "You have 60 seconds \n")

    def end_game(self):
        global secs
        messagebox.showinfo("ABC PAIRS", "\n Your Score : " + str(score) + " \n Bonus : " + str(secs))
        if messagebox.askyesno("ABC PAIRS", "Do you want to play level 1 again?"):
            self.replay_level_1()
        else:
            if messagebox.askyesno("ABC PAIRS", "Do you want to play level 2?"):
                messagebox.showinfo("ABC PAIRS", "Grid will be revealed initially for 8 seconds \n"
                                                 "You will have 60 seconds to match 6 pairs and 3 different letters")
                self.level_2()
            else:
                root.quit()

    @staticmethod
    def time_out():
        messagebox.showinfo("ABC PAIRS", "Out of time!")
        root.quit()

    def reset_level_1(self):
        global score, score_x, score_o, score_i
        global count00, count01, count02, count03
        global count10, count11, count12, count13
        global count20, count21, count22, count23

        for row in range(3):
            for column in range(4):
                self.buttons[row][column].config(text='', state=NORMAL)

                score = 0
                score_x = 0
                score_o = 0
                score_i = 0
                # reset count for buttons in first row
                count00 = (-1)
                count01 = (-1)
                count02 = (-1)
                count03 = (-1)
                # reset count for buttons in second row
                count10 = (-1)
                count11 = (-1)
                count12 = (-1)
                count13 = (-1)
                # reset count for buttons in third row
                count20 = (-1)
                count21 = (-1)
                count22 = (-1)
                count23 = (-1)

                self.score_label.config(text="")
                self.buttons[row][column].config(bg="sky blue")

    def replay_level_1(self):
        global bol
        bol = True
        global secs
        secs = 60
        self.draw_buttons()
        self.reset_level_1()
        self.count_down()
        self.create_labels()

# _______________________________________________ LEVEL 2 _____________________________________________________________#

    def level_2(self):
        global bol
        bol = True
        global secs
        secs = 68
        self.draw_buttons()
        self.reset_level_2()
        self.count_down()
        self.create_labels()
        self.preview()
        self.middle_frame.after(8000, self.hide_preview)

    def reset_level_2(self):
        global score, score_x, score_o, score_i
        global count00, count01, count02, count03
        global count10, count11, count12, count13
        global count20, count21, count22, count23

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

                self.score_label.config(text="")
                self.level_label.config(text="Level : 2")
                self.buttons[row][column].config(bg="sky blue")

    def preview(self):
        for row in range(3):
            for column in range(4):
                self.buttons[row][column].config(text=self.answer[row][column], state=DISABLED)

    def hide_preview(self):
        for row in range(3):
            for column in range(4):
                self.buttons[row][column].config(text='', state=NORMAL)


X = ABCPairs(root)
root.mainloop()
