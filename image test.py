from tkinter import *

root = Tk()
root.title("ABC Pairs Game")
root.geometry('600x600')

img1 = PhotoImage(file="fox-face_1f98a.png")
img2 = PhotoImage(file="fox-face_1f98a.png")
img3 = PhotoImage(file="tiger-face_1f42f.png")
img4 = PhotoImage(file="tiger-face_1f42f.png")
img5 = PhotoImage(file="hamster-face_1f439.png")
img6 = PhotoImage(file="hamster-face_1f439.png")


def buttons():
    print("hahahahahaha")


btn1 = Button(root, image=img1, command=buttons)
btn2 = Button(root, image=img3, comman=buttons)
btn3 = Button(root, image=img5, command=buttons)
btn1.grid(row=0, column=0)
btn2.grid(row=0, column=1)
btn3.grid(row=0, column=2)

root.mainloop()
