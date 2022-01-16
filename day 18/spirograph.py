import turtle as t
import random

tur = t.Turtle()
t.colormode(255)


def random_color():
    r = random.randint(0,255)
    g = random.randint(0,255)
    b = random.randint(0,255)
    color = (r, g, b)
    return color


tur.speed("fastest")
def draw_spirograph(size):
    for i in range(int(360/size)):
        tur.color(random_color())
        tur.circle(100)
        current_heading = tur.heading()
        tur.setheading(current_heading+size )
        print(i)


draw_spirograph(10)


screen = t.Screen()
screen.exitonclick()

