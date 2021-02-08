import random
from tkinter import *
root = Tk()
root.title("ABC Pairs")


class GUI:
    def __init__(self, master):

        self.top_frame = Frame(master)  # Creating frames
        self.top_frame.pack()

        self.bottom_frame = Frame(master)
        self.bottom_frame.pack()

        self.time_label = Label(self.top_frame, width=12, height=3, fg='green')  # Creating labels
        self.instruction_label = Label(self.top_frame, text='Click a tile and try to match it', fg="red", width=25,
                                       height=2)
        self.level_label = Label(self.bottom_frame, text='Level : 1', width=15, height=4)
        self.score_label = Label(self.bottom_frame, text='Score : ', width=15, height=4)

        self.labels()
        self.count_down(60)
        self.draw_tiles()

    def draw_tiles(self):
        self.answer = list('XXXXOOOOIIII')
        random.shuffle(self.answer)

        self.answer = [self.answer[:4],
                       self.answer[4:8],
                       self.answer[8:]]

        for row in range(3):
            for column in range(4):
                self.buttons = Button(self.bottom_frame, text=self.answer[row][column], width=16, height=6, fg='blue',
                                      bg='beige')
                self.buttons.grid(row=row+1, column=column)

    def count_down(self, secs):
        self.time_label['text'] = secs
        if secs > 0:
            self.top_frame.after(1000, self.count_down, secs-1)

    def labels(self):
        self.score_label.grid(row=6, column=0)

        self.level_label.grid(row=7, column=0)

        self.instruction_label.config(font=40)
        self.instruction_label.pack()

        self.time_label.config(font=40)
        self.time_label.pack()


    '''def click_event(self):




    def reset_buttons(self, x1, y1, x2, y2):
        self.buttons[x1][y1].config(text='', state=NORMAL)
        self.buttons[x2][y2].config(text='', state=NORMAL)'''


X = GUI(root)
root.mainloop()
