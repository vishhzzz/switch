from turtle import Turtle, Screen
import random
turtle = Turtle()
screen = Screen()

turtle.shape('turtle')

turtle.speed('fast')
screen.colormode(255)

def random_color():
    return (
        # generating a random color
        random.randint(0, 255),
        random.randint(0, 255),
        random.randint(0, 255)
    )

for _ in range(36):
    turtle.pencolor(random_color())
    turtle.circle(50)
    turtle.left(10)


screen.exitonclick()