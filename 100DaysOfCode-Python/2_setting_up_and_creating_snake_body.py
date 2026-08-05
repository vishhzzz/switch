from turtle import Screen, Turtle

screen = Screen()

# setting up screen
screen.setup(width=600, height=600)
screen.bgcolor('black')
screen.title("Snake Arena")


# Create a snake body
pos = 0
for _ in range(3):
    tim = Turtle(shape='square')
    tim.color('white')
    tim.penup()
    tim.goto(0+pos,0)
    pos -= 20










# hold the screen, till user does click on screen.
screen.exitonclick()