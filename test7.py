# import modules
import random
from tkinter import *
root = Tk()

# Frames
topframe = Frame(root)
topframe.pack()
bottomframe = Frame(root)
bottomframe.pack()

# Creating answers for tiles
answer = list('XXXXOOOOIIII')

random.shuffle(answer)

# slicing list
answer = [answer[:4],
          answer[4:8],
          answer[8:]]
print(answer)


# printing each sliced list in new line
def create_tiles():
    for every_item in answer:
        print(every_item)

        # printing letter from answer list to each button
        for row in range(3):
            for column in range(4):
                button_x = Button(bottomframe, text=answer[row][column],
                                  width=15, height=6, fg='blue', bg='beige')
                button_x.grid(row=row+1, column=column)


create_tiles()

# creating labels
score_label = Label(bottomframe, text='Score', width=15, height=4)
score_label.grid(row=6, column=0)

level_label = Label(bottomframe, text='Level', width=15, height=4)
level_label.grid(row=7, column=0)

instruction_label = Label(topframe, text='Click a tile and try to match it', fg="red", width=25, height=2)
instruction_label.config(font=40)
instruction_label.pack()


# Countdown function
def countdown(secs):
    time_label['text'] = secs
    if secs > 0:
        topframe.after(1000, countdown, secs-1)  # Call countdown every second


# Creating the time label
time_label = Label(topframe, width=12, height=3, fg='green')
time_label.config(font=40)
time_label.pack()

countdown(60)
root.mainloop()
