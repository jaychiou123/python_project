import turtle

import pandas

from convert_data import Data
# Screen setup
screen = turtle.Screen()
screen.title("U.S States Game")
screen.addshape("blank_states_img.gif")
turtle.shape("blank_states_img.gif")
# convert csv to useful data
data = Data()
states_list = data.state
# Start main function
guessed_states = []
correct_num = 0
answer = screen.textinput(title=f"Guess the state.",
                          prompt="What's another state's name?").title()
while len(guessed_states) < 50:
    if answer == "Exit":
        df = pandas.DataFrame(states_list)
        df.to_csv("Missing_states.csv")
        break
    if answer in states_list:
        data.set_location(answer)
        correct_num += 1
        guessed_states.append(answer)
        states_list.remove(answer)
    else:
        pass
    answer = screen.textinput(title=f"{correct_num}/50 States Correct.",
                              prompt="What's another state's name?")
