# w -> forward
# s -> backward
# a -> left
# d -> right
# c -> clear

from turtle import Turtle, Screen

tim = Turtle()
screen = Screen()

# start listening to keyboard
screen.listen()

def move_forward():
    tim.forward(10)

def move_backward():
    tim.backward(10)

def move_left():
    tim.left(10)
    tim.forward(10)

def move_right():
    tim.right(10)
    tim.forward(10)

def clear_screen():
    tim.reset()

screen.onkey(fun=move_forward, key='w')
screen.onkey(fun=move_backward, key='s')
screen.onkey(fun=move_left, key='a')
screen.onkey(fun=move_right, key='d')
screen.onkey(fun=clear_screen, key='c')

# hold the screen from disappearing.
screen.exitonclick()