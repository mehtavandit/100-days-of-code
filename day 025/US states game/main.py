import turtle
import pandas

screen = turtle.Screen()
screen.title("US states game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)
correct_guess = []

data = pandas.read_csv("50_states.csv")
state_list = data["state"].to_list()

while len(correct_guess)<51:
    answer = screen.textinput(title=f"{len(correct_guess)}/50 States correct", prompt="What is the another state?").title()
    if answer == "Exit":
        states_to_learn = [state for state in state_list if state not in correct_guess]
        data_2 = pandas.DataFrame(states_to_learn)
        data_2.to_csv("states_to_learn.csv")
        break


    if answer in state_list:
        if answer not in correct_guess:
            correct_guess.append(answer)
            tur = turtle.Turtle()
            tur.hideturtle()
            tur.penup()
            selected_state = data[data["state"] == answer]
            tur.goto(int(selected_state.x), int(selected_state.y))
            tur.write(answer)


screen.exitonclick()
