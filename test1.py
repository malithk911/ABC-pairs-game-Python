import random
from tkinter import *
root = Tk()

score = 0
tile_num1 = 0
tile_num2 = 0

#Creating answers for tiles
answer = list('AAAABBBBCCCC')

random.shuffle(answer)

#Creating answers for each row by slicing list
answer = [answer[:4],
          answer[4:8],
          answer[8:]]
print(answer)

# printing the sliced list
for everyitem in answer:
    print(everyitem)


'''button_1 = Button(width=8, height=4)
button_1.grid(row=0, column=0)

button_2 = Button(width=8, height=4)
button_2.grid(row=0, column=1)

button_3 = Button(width=8, height=4)
button_3.grid(row=0, column=2)

button_4 = Button(width=8, height=4)
button_4.grid(row=0, column=3)'''


'''button_5 = Button(width=8, height=4)
button_5.grid(row=1, column=0)

button_6 = Button(width=8, height=4)
button_6.grid(row=1, column=1)

button_7 = Button(width=8, height=4)
button_7.grid(row=1, column=2)

button_8 = Button(width=8, height=4)
button_8.grid(row=1, column=3)'''


'''for columnrange1 in range(4):
    button_x = Button(text='', width=8, height=4 )
    first_row = button_x.grid(row=0, column=columnrange1)

for columnrange2 in range(4):
    button_y = Button(text='', width=8, height=4)
    button_y.grid(row=1, column=columnrange2)
    
for columnrange3 in range(4):
    button_z = Button(text='', width=8, height=4)
    button_z.grid(row=2, column=columnrange3)'''


for row in range(3):
    for column in range(4):
        button_x = Button(text=answer[row][column], width=8, height=4)
        button_x.grid(row=row+1, column=column)

'''button_9 = Button(width=8, height=4)
button_9.grid(row=2, column=0)

button_10 = Button(width=8, height=4)
button_10.grid(row=2, column=1)

button_11 = Button(width=8, height=4)
button_11.grid(row=2, column=2)

button_12 = Button(width=8, height=4)
button_12.grid(row=2, column=3)'''




root.mainloop()


