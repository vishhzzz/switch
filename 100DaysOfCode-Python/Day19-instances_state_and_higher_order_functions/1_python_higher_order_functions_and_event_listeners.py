# EVENT LISTENERS
# these r piece of code which allows to listen the key-stroke or infact any sort of events.

# We have Turtle Event Listeners
# which help specifically in Turtle related GUI things using events.

# So Python itself does not have any kind of event listeners i.e., no built-in event listener system.
# it relies on diff. libraries for the same.
# Diff. lib. provide their own 'event handling apis'.
# basically each lib has their own event handling mechanism.

# listen is an event listener function in turtle which listens for any events 
# listen: it tells the turtle window that from now start focusing on key strokes and for each key what happens is decided via user.

from turtle import Turtle, Screen

tim = Turtle()
screen = Screen()

def move_forward():
    tim.forward(10)

# listening events
screen.listen()

screen.onkey(key='space', fun=move_forward) #When we pass a function as arguement then we dont add brackets to it.
# () triggers functions to happen.

# this holds the screen so that it does not disappear on its own.
screen.exitonclick()


# HIGHER ORDER FUNCTIONS
# these r the functions which can work with other functions.
# Basically here onkey is a 'HIGHER ORDER FUNCTION' as it takes another function as input and work with it.


# HIGHER ORDER FUNCTIONS
# a function is termed as HIGHER ORDER FUNCTION if it satisfies either of 2 conditions:
# 1. takes 1 or more functions as input
# 2. returns a functions