import random
from tkinter import *
root = Tk()

score = 0
tile_num1 = 0
tile_num2 = 0

#Creating answers for tiles
answer = list('AAAABBBBCCCC')

random.shuffle(answer)

#slicing list
answer = [answer[:4],
          answer[4:8],
          answer[8:]]
print(answer)

#printing each sliced list in new line
for everyitem in answer:
    print(everyitem)

#printing letter from answer list to each button
for row in range(3):
    for column in range(4):
        button_x = Button(text=answer[row][column], width=10, height=4)
        button_x.grid(row=row+1, column=column)


#creating labels
score_label = Label(text='Score')
score_label.grid(row=6, column=0)

level_label = Label(text='Level')
level_label.grid(row=7, column=0)

instruction_label = Label(text='Click a tile and try match it', fg="red", width=15)
instruction_label.grid(row=0)

root.mainloop()
