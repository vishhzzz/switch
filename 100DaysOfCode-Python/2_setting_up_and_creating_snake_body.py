# although in python, we can use Keyword Args.
# range function is something where we cant use that as it comes from c. it does not take any keyword args.


from turtle import Screen, Turtle
import time

screen = Screen()

# setting up screen
screen.setup(width=600, height=600)
screen.bgcolor('black')
screen.title("Snake Arena")
screen.tracer(0) #turn off the tracer. Nothing will be drawn until update is called.

positions = [(0,0), (-20, 0), (-40, 0)]
snake_body = []

# Create a snake body
pos = 0
for position in positions:
    tim = Turtle(shape='square')
    tim.color('white')
    tim.penup()
    tim.goto(position)
    snake_body.append(tim)

# screen.update() #now it will draw.


# this is wrong movements
# while is_game_on:
#     screen.update() #it will draw screen when each segment moves
#     time.sleep(0.1)
#     for snake in snake_body:
#         snake.forward(20)

# will try to move like this i.e., last segment move to 2nd last and so on.
is_game_on = True
while is_game_on:
    screen.update()
    time.sleep(0.1)

    for seg in range(len(snake_body)-1, 0, -1):
        x = snake_body[seg-1].xcor()
        y = snake_body[seg-1].ycor()
        snake_body[seg].goto(x, y)
    snake_body[0].forward(20)









# hold the screen, till user does click on screen.
screen.exitonclick()