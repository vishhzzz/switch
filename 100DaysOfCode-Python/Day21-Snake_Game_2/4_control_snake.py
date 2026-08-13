# There should be 3 classes 
# 1. Snake
# 2. Food
# 3. Scoreboad

from turtle import Screen
from snake import Snake
import time
import food
import scoreboard

screen = Screen()

# setting up screen
screen.setup(width=600, height=600)
screen.bgcolor('black')
screen.title("Snake Arena")
screen.tracer(0) #turn off the tracer. Nothing will be drawn until update is called.

snake = Snake()
food = food.Food()
score = scoreboard.Scoreboad()

# key-events - in order to control snake.
screen.listen()

screen.onkey(snake.move_up, 'Up')
screen.onkey(snake.move_down, 'Down')
screen.onkey(snake.move_left, 'Left')
screen.onkey(snake.move_right, 'Right')

is_game_on = True
while is_game_on:
    screen.update()
    time.sleep(0.1)

    snake.move()
    # collission with food.
    # we can compare this via distance method which tells that how much distance is in btw the 2.
    if snake.snake_body[0].distance(food) < 15: #as snake is 20*20 and food is 10*10
        food.random_food()
        # also increase the score as snake eats food.
        score.score += 1
        snake.grow_snake()
        score.display_score()

    # detecting collision with wall
    if -300 >= snake.snake_body[0].xcor() or snake.snake_body[0].xcor() >= 300 or -300 >= snake.snake_body[0].ycor() or snake.snake_body[0].ycor() >= 300:
        print("Game Over !!!")
        is_game_on = False
        score.game_over()

    # detecting collision with tail
    # we can detect this if snake head collide with snake body
    for snake_segment in snake.snake_body:
        # of all snake segments here, we have snake head too
        # so we need to pass
        if snake_segment == snake.snake_body[0]:
            pass
        elif snake.snake_body[0].distance(snake_segment) < 10:
            is_game_on = False
            score.game_over()

# hold the screen, till user does click on screen.
screen.exitonclick()