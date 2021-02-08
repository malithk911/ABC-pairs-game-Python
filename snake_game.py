import turtle
import time

delay = 0.1

root = turtle.Screen()
root.title("snake game")
root.bgcolor("red")
root.setup(width=600, height=600)
root.tracer(0)  # turns off animation on screen

# snake head
head = turtle.Turtle()
head.speed(0)  # animation speed of turtle module
head.shape("square")
head.color("black")
head.penup()  # does not draw lines
head.goto(0, 0)
head.direction = "up"


def move():
    if head.direction == "up":
        y = head.ycor()
        head.sety(y + 20)

    if head.direction == "down":
        y = head.ycor()
        head.sety(y+20)

    if head.direction == "left":
        x = head.xcor()
        head.setx(x+20)

    if head.direction == "right":
        x = head.xcor()
        head.setx(x+20)


# main game loop
while True:
    root.update()
    move()
    time.sleep(delay)


root.mainloop()

