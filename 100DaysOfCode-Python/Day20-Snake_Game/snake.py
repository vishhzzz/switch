from turtle import Turtle

POSITIONS = [(0,0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 20
DIRECTIONS = [0, 90, 180, 270]

# snake class
class Snake:
    def __init__(self):
        self.snake_body = []
        # Create a snake body
        self.create_snake()

    def create_snake(self):
        for position in POSITIONS:
            timmy_the_turtle = Turtle(shape='square')
            timmy_the_turtle.color('white')
            timmy_the_turtle.penup()
            timmy_the_turtle.goto(position)
            self.snake_body.append(timmy_the_turtle)

    def move(self):
        for seg in range(len(self.snake_body)-1, 0, -1):
            # know the co-ord of 2nd last snake body.
            x = self.snake_body[seg-1].xcor()
            y = self.snake_body[seg-1].ycor()

            # get hold of last part of snake body
            # and move it to 2nd last co-ords
            self.snake_body[seg].goto(x, y)
        # # move head
        self.snake_body[0].forward(MOVE_DISTANCE)

    # snake - move up
    def move_up(self):
        '''move snake up'''
        if self.snake_body[0].heading() == 270:
            return

        # set direction
        self.snake_body[0].setheading(90)
        
        self.move()

    
    # snake - move down
    def move_down(self):
        '''move snake down'''
        if self.snake_body[0].heading() == 90:
            return

        # set direction
        self.snake_body[0].setheading(270)

        self.move()
    
    # snake - move left
    def move_left(self):
        '''move snake left'''
        if self.snake_body[0].heading() == 0:
            return

        # set direction
        self.snake_body[0].setheading(180)

        self.move()
    
    # snake - move right
    def move_right(self):
        '''move snake right'''
        if self.snake_body[0].heading() == 180:
            return

        # set direction
        self.snake_body[0].setheading(0)

        self.move()

