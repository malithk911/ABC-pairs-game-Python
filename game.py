from tkinter import*
import time
import random
import numpy as np
import numpy.random


#functions
click = []
def match(num):
    click.append(num)
    print(num)
    print(click)
    if num == 1:
        Button1.config(state="disabled")
        Button1["background"] = "black"
    elif num==2:
        Button2.config(state="disabled")
        Button2["background"] ="black"
    elif num==3:
        Button3.config(state="disabled")
        Button3["background"]="black" 
    elif num==4:
        Button4.config(state="disabled")
        Button4["background"]="black" 
    #second raw
    elif num==5:
        Button5.config(state="disabled")
        Button5["background"]="black" 
    elif num==6:
        Button6.config(state="disabled")
        Button6["background"]="black" 
    elif num==7:
       Button7.config(state="disabled")
       Button7["background"]="black" 
    elif num==8:
        Button8.config(state="disabled")
        Button8["background"]="black" 
    # Third row 
    elif num==9:
        Button9.config(state="disabled")
        Button9["background"]="black" 
    elif num==10:
       Button10.config(state="disabled")
       Button10["background"]="black" 

    elif num==11:
        Button11.config(state="disabled")
        Button11["background"]="black" 
    elif num ==12 :
        Button12.config(state="disabled")
        Button12["background"]="black" 


#setting the game window
window = Tk()
window.title("ABC pair game")

#setting the frame
topFrame = Frame(window)
topFrame.pack()
topDown = Frame(window)
topDown.pack()
topBottom = Frame(window)
topBottom.pack()

# sequence = [i for i in range(12)]
# print(sequence)
# # make choices from the sequence
# for _ in range(5):
# 	selection = choice(sequence)
# 	print(selection)
# arr = [1,2,3,4,5,6,7,8,9,10,11,12]
# random.shuffle(arr)
# print(arr)

col = ["lightblue", "green", "red"]

arr = [7,2,9,3,1,12,4,6,8,11,10,5]
c = arr.copy()
random.shuffle(c)
random.shuffle(arr)
# print(arr)


# for i in arr:
#     j = i %3
#     if j == 0:
#         Button1 = Button(topFrame,  height=5, width=12, bg=col[j], command=lambda:match(i))
#         Button1.pack(side = LEFT)
#     elif j==1:
#         Button2 = Button(topDown,  height=5, width=12, bg=col[j] , command=lambda:match(i))
#         Button2.pack(side = LEFT)
#     else:
#         Button3 = Button(topBottom,  height=5, width=12, bg=col[j], command=lambda:match(i))
#         Button3.pack(side = LEFT)
#     print(i)
for i in arr:
    j = i % 3
    if i == 1:
        Button1 = Button(topFrame,  height=5, width=12, bg=col[j], command=lambda:match(1))
        Button1.pack(side = LEFT)
    elif i == 2:
        Button2 = Button(topFrame,  height=5, width=12, bg=col[j], command=lambda:match(2))
        Button2.pack(side = LEFT)
    elif i == 3:
        Button3 = Button(topFrame,  height=5, width=12, bg=col[j], command=lambda:match(3))
        Button3.pack(side = LEFT)
    elif i == 4:
        Button4 = Button(topFrame,  height=5, width=12, bg=col[j], command=lambda:match(4))
        Button4.pack(side = LEFT)

        #second raw
    elif i == 5:
        Button5 = Button(topDown,  height=5, width=12, bg=col[j] , command=lambda:match(5) )
        Button5.pack(side = LEFT)
    elif i == 6:
        Button6 = Button(topDown,  height=5, width=12, bg=col[j] , command=lambda:match(6) )
        Button6.pack(side = LEFT)
    elif i==7:
        Button7 = Button(topDown,  height=5, width=12, bg=col[j] , command=lambda:match(7) )
        Button7.pack(side = LEFT)
    elif i==8:
        Button8 = Button(topDown,  height=5, width=12, bg=col[j] , command=lambda:match(8) )
        Button8.pack(side = LEFT)

        # Third row 
    elif i==9:
        Button9 = Button(topBottom,  height=5, width=12, bg=col[j], command=lambda:match(9) )
        Button9.pack(side = LEFT)
    elif i==10:
        Button10 = Button(topBottom,  height=5, width=12, bg=col[j], command=lambda:match(10) )
        Button10.pack(side = LEFT)

    elif i==11:
        Button11 = Button(topBottom,  height=5, width=12, bg=col[j], command=lambda:match(11) )
        Button11.pack(side = LEFT)

    elif i==12  :
        Button12 = Button(topBottom,  height=5, width=12, bg=col[j], command=lambda:match(12) )
        Button12.pack(side = LEFT)






window.mainloop()









