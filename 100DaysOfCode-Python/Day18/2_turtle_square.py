from turtle import Turtle, Screen

turtle = Turtle()

for _ in range(0, 4):
    # move forward by 100
    turtle.forward(100)

    # right turn
    turtle.right(90)

screen = Screen()
screen.exitonclick()