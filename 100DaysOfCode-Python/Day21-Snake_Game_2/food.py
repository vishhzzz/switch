# this is going to be a food class which know where to draw a circle and will change its location as soon as snake touches the food.

from turtle import Turtle   #food will be a turtle object.
from random import randint

# we can either create it as attribute or simply inherit from it.

class Food(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.shape('circle')
        self.shapesize(stretch_len=0.5, stretch_wid=0.5) #half the circle
        self.color('blue')
        self.speed('fastest')
        self.random_food()

    def random_food(self):
        # screen is 600 * 600.
        random_x = randint(-280, 280)
        random_y = randint(-280, 280)
        self.goto(random_x, random_y)