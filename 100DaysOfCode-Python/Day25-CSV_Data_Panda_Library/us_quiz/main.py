# if i use 1 turtle then whole thing starts moving as we use goto becoz the image itself is turtle, so we need 2 turtles, one for image and one for writing names

# We should have a secret code via which we can exit

import turtle, pandas

turtle_state_name = turtle.Turtle()
turtle_state_name.hideturtle()
turtle_state_name.penup()
state = turtle.Screen()
state.title("U.S. States Quiz")

image = "./Day25-CSV_Data_Panda_Library/us_quiz/blank_states_img.gif"
state.addshape(image)
turtle.shape(image)



# quiz questions

# we need to ask questions till the user entered all correct states.
# no of states
states_data = pandas.read_csv("./Day25-CSV_Data_Panda_Library/us_quiz/50_states.csv")
no_of_correct_states = len(states_data.state.to_list())
# print(states_data.state.to_list())

no_of_correct_guesses = 0
guessed_states = []
while True:
    # get user ans
    answer_state = state.textinput(title=f"Guess the states {no_of_correct_guesses}/50", prompt="Whats another state's name")

    if answer_state == 'exit':
        break

    # if that user input state exists in table or not
    # print(states_data['state'].str.lower() == answer_state.lower())
    # if states_data['state'].str.lower() == answer_state.lower():
    # in series k index ko check krta h thats why .values is imp.
    if answer_state.lower() in states_data['state'].str.lower().values:
        # get co-ordinates of answered data from db
        x_cor = states_data[states_data['state'].str.lower() == answer_state.lower()].x.iloc[0] #we can also use .x.item() to get hold of value
        y_cor = states_data[states_data['state'].str.lower() == answer_state.lower()].y.iloc[0]

        print(x_cor)
        print(y_cor)

        # place a text on screen for correct state
        # turtle.penup()
        turtle_state_name.goto(x=x_cor, y=y_cor)
        turtle_state_name.write(answer_state, align="center", font=("Arial", 16, "normal"))
        guessed_states.append(answer_state.title())

        no_of_correct_guesses += 1

        if no_of_correct_guesses == no_of_correct_states:
            break
    else:
        continue


turtle_state_name.goto(0, 0)
turtle_state_name.write("Game Over", align="center", font=("Arial", 16, "normal"))
print('Game Over')

# we need to generate a csv file which should contain all those names which r missed by user.
total_states = states_data['state'].to_list()
missed_states = []
for state in total_states:
    if state not in guessed_states:
        missed_states.append(state)
# list comprehension
# missed_states = [state for state in total_states if state not in guessed_states]

csv_data = pandas.DataFrame(missed_states)
csv_data.to_csv("./Day25-CSV_Data_Panda_Library/us_quiz/missed_state.csv")




state.exitonclick()

