from tkinter import *
import random


answer = list('AABBCCXXYYZZ')
random.shuffle(answer)
#print(len(answer), answer)

answer = [answer[:4],
          answer[4:8],
          answer[8:]]
print(answer)
for m in range(len(answer)):
    print(answer[m])



'''print(answer[0][0])
print(answer[0][1])
print(answer[0][2])
print(answer[0][3])'''


'''for q in range(4):
    print(answer[0][q])

for w in range(4):
    print(answer[1][w])

for e in range(4):
    print(answer[2][e])'''

for r in range(3):
    for q in range(4):
        print(answer[r][q])





root = Tk()

'''for y in range(4):
    row1 = Button(text='', width=8, height=4)
    row1.grid(row=0, column=y)

for a in range(4):
    row2 = Button(text='', width=8, height=4)
    row2.grid(row=1, column=a)

for b in range(4):
    row3 = Button(text='', width=8, height=4)
    row3.grid(row=2, column=b)'''

for n in range(3):
    for y in range(4):
        row1 = Button(text='', width=8, height=4)
        row1.grid(row=n, column=y)



messagelabel = Label(text="start game")
messagelabel.grid(row=0)
scorelabel = Label(text="Score :")
scorelabel.grid(row=4, column=1)

levellabel = Label(text="Level :")
levellabel.grid(row=5, column=1)


root.mainloop()
