from turtle import  Turtle, Screen
import random

screen = Screen()
screen.setup(width=500, height=400)
user_guess = screen.textinput(title="Make you bet", prompt="Which turtle will win the race?")
color = ["red", "orange", "yellow", "green", "blue",  "violet"]
y_pos = [-120, -70, -20, 30, 80, 130]
turtles = []
race_status = False

for i in range(0,6):
    tim = Turtle(shape="turtle")
    tim.penup()
    tim.color(color[i])
    tim.goto(x=-230, y=y_pos[i])
    turtles.append(tim)

# tur_1 = Turtle(shape="turtle")
# tur_1.penup()
# tur_1.color(color[0])
# tur_1.goto(x=-230, y=-120)
#
# tur_2 = Turtle(shape="turtle")
# tur_2.penup()
# tur_2.color(color[1])
# tur_2.goto(x=-230, y=-70)
#
# tur_3 = Turtle(shape="turtle")
# tur_3.penup()
# tur_3.color(color[2])
# tur_3.goto(x=-230, y=-20)
#
# tur_4 = Turtle(shape="turtle")
# tur_4.penup()
# tur_4.color(color[3])
# tur_4.goto(x=-230, y=30)
#
# tur_5 = Turtle(shape="turtle")
# tur_5.penup()
# tur_5.color(color[4])
# tur_5.goto(x=-230, y=80)
#
# tur_6 = Turtle(shape="turtle")
# tur_6.penup()
# tur_6.color(color[5])
# tur_6.goto(x=-230, y=130)

if user_guess:
    race_status = True

while race_status:
    for i in turtles:

        if i.xcor() > 230:
            race_status = False
            win_color = i.pencolor()
            if win_color == user_guess:
                print(f"You won!! {win_color} is the winner")
            else:
                print(f"You lost. {win_color} is the winner")
        dist_for = random.randint(0, 10)
        i.forward(dist_for)


screen.exitonclick()
