from tkinter import *
import random


answer = list('AABBCCXXYYZZ')

random.shuffle(answer)
print(len(answer), answer)

'''print(str(answer[0]),
      "\n"+str(answer[1]),
      "\n"+str(answer[2]),
      "\n"+str(answer[3]),
      "\n"+str(answer[4]),
      "\n"+str(answer[5]),
      "\n"+str(answer[6]),
      "\n"+str(answer[7]),
      "\n"+str(answer[8]),
      "\n"+str(answer[9]),
      "\n"+str(answer[10]),
      "\n"+str(answer[11]))

for x in range(len(answer)):
    print(answer[x])'''



answer = [answer[:4],
          answer[4:8],
          answer[8:]]

print(str(answer[0]),'\n'+str(answer[1]),'\n'+str(answer[2]))

root = Tk()
'''
button_1 = Button(text="B1", bg="beige", width=4, height=2)
button_1.grid(row=0, column=0)
button_2 = Button(text="B2", bg="beige", width=4, height=2)
button_2.grid(row=0, column=1)
button_3 = Button(text="B3", bg="beige", width=4, height=2)
button_3.grid(row=0, column=2)
button_4 = Button(text="B4", bg="beige", width=4, height=2)
button_4.grid(row=0, column=3)
'''
for y in range(4):
    row1 = Button(text='', width=8, height=4)
    row1.grid(row=0, column=y)

'''
button_5 = Button(text="B5", bg="beige", width=4, height=2)
button_5.grid(row=1, column=0)
button_6 = Button(text="B6", bg="beige", width=4, height=2)
button_6.grid(row=1, column=1)
button_7 = Button(text="B7", bg="beige", width=4, height=2)
button_7.grid(row=1, column=2)
button_8 = Button(text="B8", bg="beige", width=4, height=2)
button_8.grid(row=1, column=3)'''

for a in range(4):
    row2 = Button(text='', width=8, height=4)
    row2.grid(row=1, column=a)



'''button_9 = Button(text="B9", bg="beige", width=4, height=2)
button_9.grid(row=2, column=0)
button_10 = Button(text="B10", bg="beige", width=4, height=2)
button_10.grid(row=2, column=1)
button_11 = Button(text="B11", bg="beige", width=4, height=2)
button_11.grid(row=2, column=2)
button_12 = Button(text="B12", bg="beige", width=4, height=2)
button_12.grid(row=2, column=3)'''

for b in range(4):
    row3 = Button(width=8, height=4)
    row3.grid(row=2, column=b)


scorelabel = Label(text="Score :")
scorelabel.grid(row=4, column=1)

levellabel = Label(text="Level :")
levellabel.grid(row=5, column=1)


root.mainloop()






