from turtle import Turtle, Screen
import random
turtle = Turtle()
screen = Screen()

turtle.shape('turtle')
turtle.shapesize(2, 2)
turtle.width(10)

directions = [0, 90, 180, 270]

turtle.speed('fastest')
screen.colormode(255)

def random_color():
    return (
        # generating a random color
        random.randint(0, 255),
        random.randint(0, 255),
        random.randint(0, 255)
    )

while True:
    turtle.pencolor(random_color())
    turtle.setheading(random.choice(directions))
    turtle.forward(20)


screen.exitonclick()