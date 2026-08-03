# false commit
from turtle import Turtle, Screen

timmy_the_turtle = Turtle()

# change the shape
timmy_the_turtle.shape('turtle')

# modify color
timmy_the_turtle.color('blue')

# turtle uses TK for changing colors.
# tk ---> tkinter ---> tk interface

# tk is one of the way via which Python can create GUI - Graphical User Interface.

# tk is the module on which turtle relies on under the hood.

# motion
timmy_the_turtle.forward(100) #move forward by 100 units/spaces

timmy_the_turtle.right(90)





# should be at bottom, as it holds the screen and will close it only when i click on screen.
screen = Screen()
screen.exitonclick()