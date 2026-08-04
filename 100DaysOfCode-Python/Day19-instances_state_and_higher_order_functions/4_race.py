from turtle import Turtle, Screen
from random import randint, choice

screen = Screen()

# choosing game area or simply screen size
screen.setup(width=500, height=400) #width, height

is_game_on = False

# works similarly as input.
player_choice = screen.textinput(title='Make your bet', prompt='Which turtle will win the race? Enter a color: ')

if player_choice:
    is_game_on = True

def turtle_move():
    global is_game_on
    while is_game_on:
        for turtle in list_of_turtle:
            if turtle.xcor() > 230:
                is_game_on = False
                if player_choice == turtle.pencolor():
                    # screen.textinput(title='Game Ends !!!', prompt="Winner....")
                    # turtle.write("Win")
                    print("You Won !!!")
                else:
                    # screen.textinput(title='Game Ends !!!', prompt='You loosee....')
                    # turtle.write("Loose")
                    print(f"You loose !!!\nWinning Turtle is {turtle.pencolor()}")
                break
            turtle.forward(randint(0, 10))

color_of_turtle = ['red', 'blue', 'black', 'green', 'brown']
y_dist = 0
list_of_turtle = []
for ele in range(5):
    turtle = Turtle(shape='turtle')
    turtle.penup()
    turtle.color(color_of_turtle[ele])
    turtle.goto(x=-230, y=-100+y_dist)
    y_dist += 40
    list_of_turtle.append(turtle)


turtle_move()


# turtle1 = Turtle(shape='turtle')
# turtle1.penup()
# # turtle1.shape('turtle')
# turtle1.color('red')
# # move turtle to starting position i.e., left most corner
# turtle1.goto(x= -200, y= -100)

# turtle2 = Turtle(shape='turtle')
# turtle2.penup()
# # turtle2.shape('turtle')
# turtle2.color('blue')
# turtle2.goto(x= -200, y= -60)

# turtle3 = Turtle(shape='turtle')
# turtle3.penup()
# # turtle3.shape('turtle')
# turtle3.color('green')
# turtle3.goto(x= -200, y= -20)

# turtle4 = Turtle(shape='turtle')
# turtle4.penup()
# # turtle4.shape('turtle')
# turtle4.color('brown')
# turtle4.goto(x= -200, y= 20)

# turtle5 = Turtle(shape='turtle')
# turtle5.penup()
# # turtle5.shape('turtle')
# turtle5.color('black')
# turtle5.goto(x= -200, y= 60)


# will hold the screen, until user clicks.
screen.exitonclick()