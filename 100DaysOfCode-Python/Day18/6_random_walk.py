from turtle import Turtle, Screen
from random import choice

turtle = Turtle()
screen = Screen()

colours = ["CornflowerBlue", "DarkOrchid", "IndianRed", "DeepSkyBlue", "LightSeaGreen", "wheat", "SlateGray", "SeaGreen", "black"]

turtle.shape('turtle')
turtle.shapesize(2, 2)
turtle.width(10)

# ***************************************************

# directions = ['north', 'south', 'east', 'west']


# while True:
#     dir_to_move = choice(directions)
#     turtle.color(choice(colours))
#     if dir_to_move == 'east':
#         turtle.setheading(0)
#     elif dir_to_move == 'north':
#         turtle.setheading(90)
#     elif dir_to_move == 'west':
#         turtle.setheading(180)
#     else:
#         turtle.setheading(270)

#     turtle.forward(20)


# there is issue in this version of code, there is a lot of if-else in this.

# ****************************************************

# we will store directions in list - i.e., only angles
# or we can store a dir with angles and names in a dictionary

directions = [0, 90, 180, 270]

turtle.speed('fastest')

while True:
    turtle.color(choice(colours))
    turtle.setheading(choice(directions))
    turtle.forward(20)


screen.exitonclick()