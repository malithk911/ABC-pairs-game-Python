from tkinter import *
root = Tk()
topframe = Frame(root)
topframe.pack()
bottomframe = Frame(root)
bottomframe.pack(side=BOTTOM)
root.geometry("500x500")
import random

#Labels
label_1 = Label(bottomframe, text="Score", width=8, height=2)
label_2 = Label(bottomframe, text="Level", width=8, height=2)
label_1.pack(side=BOTTOM)
label_2.pack(side=BOTTOM)

#Buttons
button_1 = Button(topframe, text="B1", bg="beige", width=4, height=2)
button_2 = Button(topframe, text="B2", bg="beige", width=4, height=2)
button_3 = Button(topframe, text="B3", bg="beige", width=4, height=2)
button_4 = Button(topframe, text="B4", bg="beige", width=4, height=2)
button_5 = Button(topframe, text="B5", bg="beige", width=4, height=2)
button_6 = Button(topframe, text="B6", bg="beige", width=4, height=2)
button_7 = Button(topframe, text="B7", bg="beige", width=4, height=2)
button_8 = Button(topframe, text="B8", bg="beige", width=4, height=2)
button_9 = Button(topframe, text="B9", bg="beige", width=4, height=2)
button_10 = Button(topframe, text="B10", bg="beige", width=4, height=2)
button_11 = Button(topframe, text="B11", bg="beige", width=4, height=2)
button_12 = Button(topframe, text="B12", bg="beige", width=4, height=2)


#Grid Layout
button_1.grid(row=0, column=0)
button_2.grid(row=0, column=1)
button_3.grid(row=0, column=2)
button_4.grid(row=0, column=3)
button_5.grid(row=1, column=0)
button_6.grid(row=1, column=1)
button_7.grid(row=1, column=2)
button_8.grid(row=1, column=3)
button_9.grid(row=2, column=0)
button_10.grid(row=2, column=1)
button_11.grid(row=2, column=2)
button_12.grid(row=2, column=3)


def buttons():
    answers = ['a','a','a','a','b','b','b','b','c','c','c','c']
    random.shuffle(answers)
    print(answers)

x = buttons()
root.mainloop()