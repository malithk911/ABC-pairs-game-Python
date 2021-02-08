#import modules
import random
from tkinter import *
root = Tk()

#Frames
topframe = Frame(root)
topframe.pack()
bottomframe = Frame(root)
bottomframe.pack()

#Creating answers for tiles
answer = list('XXXXOOOOIIII')

random.shuffle(answer)

#slicing list
answer = [answer[:4],
          answer[4:8],
          answer[8:]]
print(answer)

#printing each sliced list in new line
def create_tiles():
    for every_item in answer:
        print(every_item)

        # printing letter from answer list to each button
        for row in range(3):
            for column in range(4):
                button_x = Button(bottomframe, text=answer[row][column],
                                  width=15, height=8)
                button_x.grid(row=row+1, column=column)
create_tiles()

#creating labels
score_label = Label(bottomframe, text='Score', width=15, height=4)
score_label.grid(row=6, column=0)

level_label = Label(bottomframe, text='Level', width=15, height=4)
level_label.grid(row=7, column=0)

instruction_label = Label(topframe, text='Click a tile and try to match it', fg="red", width=25, height=5)
instruction_label.pack()




root.mainloop()
