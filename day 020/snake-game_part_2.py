from turtle import Turtle, Screen
import time

screen = Screen()
screen.setup(width = 600, height = 600)
screen.bgcolor("black")
screen.title("The snake game")
screen.tracer(0)
starting_pos = [(0, 0), (-20, 0), (-40, 0)]
segments = []


for pos in starting_pos:
    tur = Turtle(shape="square")
    tur.penup()
    tur.color("white")
    tur.goto(pos)
    segments.append(tur)

game_status = True

while game_status:
    screen.update()
    time.sleep(0.1)

    for segment in range(len(segments)-1, 0, -1):
        new_x = segments[segment-1].xcor()
        new_y = segments[segment - 1].ycor()
        segments[segment].goto(new_x, new_y)

    segments[0].forward(20) #Checking of for loop
    segments[0].left(90)


screen.exitonclick()
