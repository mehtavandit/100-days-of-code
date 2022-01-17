from turtle import Turtle, Screen

screen = Screen()
screen.setup(width = 600, height = 600)
screen.bgcolor("black")
screen.title("The snake game")
starting_pos = [(0, 0), (-20, 0), (-40, 0)]

# tur_1 = Turtle(shape="square")
# tur_1.color("white")
# tur_1.penup()
# tur_2 = Turtle(shape="square")
# tur_2.color("green")
# tur_2.penup()
# tur_2.goto(-20, 0)
# tur_3 = Turtle(shape="square")
# tur_3.color("blue")
# tur_3.goto(-40,0)
# tur_3.penup()

for pos in starting_pos:
    tur = Turtle(shape="square")
    tur.color("white")
    tur.goto(pos)
