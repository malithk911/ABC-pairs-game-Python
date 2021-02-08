from tkinter import *
import random

root = Tk()
root.title("ABC PAIRS 2018412")
root.config(bg="#008080")


class ABCPairs:
    def __init__(self, master):
        self.top_frame = Frame(master)
        self.top_frame.grid()
        self.middle_frame = Frame(master)
        self.middle_frame.grid()
        self.bottom_frame = Frame(master)
        self.bottom_frame.grid()

        self.buttons = [[Button(self.middle_frame, width=10, height=5, bg="sky blue", font=40,
                        command=lambda row=row, column=column: self.click(row, column))
                        for column in range(4)] for row in range(3)]

        for row in range(3):
            for column in range(4):
                self.buttons[row][column].grid(row=row+1, column=column)
        self.answer = []
        self.draw_buttons()
        self.first = None

    def draw_buttons(self):
        self.answer = ['A', 'A', 'A', 'A', 'B', 'B', 'B', 'B', 'C', 'C', 'C', 'C']
        random.shuffle(self.answer)
        self.answer = [self.answer[0:4], self.answer[4:8], self.answer[8:12]]

        for i in range(len(self.answer)):
            print(self.answer[i])

    def click(self, row, column):
        self.buttons[row][column].config(text=self.answer[row][column], state=DISABLED)
        if self.first is None:
            self.first = [row, column]
        else:
            if self.answer[row][column] == self.answer[self.first[0]][self.first[1]]:
                self.buttons[row][column].config(bg="light green")
                self.buttons[self.first[0]][self.first[1]].config(bg="light green")
                print("Match!")
                self.first = None
            else:
                self.middle_frame.after(1000, self.reset, row, column)
                self.first = None

    def reset(self, row_a, column_a):
        self.buttons[row_a][column_a].config(text="", state=NORMAL)
        self.buttons[self.first[0]][self.first[1]].config(text="", state=NORMAL)


X = ABCPairs(root)
root.mainloop()
