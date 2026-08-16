# Turtle works with only 1 image format whixh is .gif

# this project is a U.S. states quiz. 
# Where the U.S. states map is a gif file.

import turtle

state = turtle.Screen()

state.title("U.S. States Quiz")

# lets load the Turtle but this time it is of my shape and we can give any img of our choice just by adding .gif file.
image = "./Day25-CSV_Data_Panda_Library/us_quiz/blank_states_img.gif"
state.addshape(image)

# we need to first register any shape as valid turtle shape with turtle screen.
# then only we can use that as turtle shape thus we need both of the lines.


turtle.shape(image)



# quiz question
answer_state = state.textinput(title="Guess the states", prompt="Whats another state's name")
print(answer_state)

state.exitonclick()
# its alternative 
# turtle.mainloop() #holds the screen after finishing


# # to get the location on screen of mouse click.
# def get_mouse_loc(x, y):
#     print(x, y)
# turtle.onscreenclick(get_mouse_loc)
# turtle.mainloop()

# we dont need this code r.n. becoz we already have location data in csv file.
