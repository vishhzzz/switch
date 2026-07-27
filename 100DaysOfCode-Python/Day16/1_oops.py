# creating a new object from class ---> <obj_name> = <class_name>()

# We will be now putting graphics to screen

# We'll be using 'turtle graphics' - preloaded with each python.
# a turtle with paintbrush on its back.
# can do certain things

# We are now going to create an object from a blueprint that someone else has already created which resides on a module called 'turtle'.

# CLASS - blueprint for creating a new object.

import turtle

# object creation in Python
# object_name = class_name()
print("1")
timmy = turtle.Turtle()
print(timmy)
# sets its shape to turtle
timmy.shape('turtle')
timmy.color('cyan')
timmy.forward(100)
# turtle.done()

# it also has class called -> Screen : place where turtle will show up.
my_screen = turtle.Screen()
print(my_screen.canvheight)

my_screen.exitonclick()


