# There should be 3 classes 
# 1. Snake
# 2. Food
# 3. Scoreboad

from turtle import Screen
from snake import Snake
import time

screen = Screen()

# setting up screen
screen.setup(width=600, height=600)
screen.bgcolor('black')
screen.title("Snake Arena")
screen.tracer(0) #turn off the tracer. Nothing will be drawn until update is called.

snake = Snake()

is_game_on = True
while is_game_on:
    screen.update()
    time.sleep(0.1)

    snake.move()

# hold the screen, till user does click on screen.
screen.exitonclick()