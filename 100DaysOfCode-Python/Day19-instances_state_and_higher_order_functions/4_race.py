from turtle import Turtle, Screen

screen = Screen()

# choosing game area or simply screen size
screen.setup(width=500, height=400) #width, height

# works similarly as input.
player_choice = screen.textinput(title='Make your bet', prompt='Which turtle will win the race? Enter a color: ')


turtle1 = Turtle(shape='turtle')
turtle1.penup()
# turtle1.shape('turtle')
turtle1.color('red')
# move turtle to starting position i.e., left most corner
turtle1.goto(x= -200, y= -100)

turtle2 = Turtle(shape='turtle')
turtle2.penup()
# turtle2.shape('turtle')
turtle2.color('blue')
turtle2.goto(x= -200, y= -60)

turtle3 = Turtle(shape='turtle')
turtle3.penup()
# turtle3.shape('turtle')
turtle3.color('green')
turtle3.goto(x= -200, y= -20)

turtle4 = Turtle(shape='turtle')
turtle4.penup()
# turtle4.shape('turtle')
turtle4.color('brown')
turtle4.goto(x= -200, y= 20)

turtle5 = Turtle(shape='turtle')
turtle5.penup()
# turtle5.shape('turtle')
turtle5.color('black')
turtle5.goto(x= -200, y= 60)


# will hold the screen, until user clicks.
screen.exitonclick()