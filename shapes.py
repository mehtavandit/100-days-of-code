from turtle import Turtle, Screen

tri = Turtle()
tri.color("deeppink")
squ = Turtle()
squ.color("darkgoldenrod1")
pen = Turtle()
pen.color("green")
hex = Turtle()
hex.color("navy")
hep = Turtle()
hep.color("purple")
oct = Turtle()
oct.color("seagreen")
non = Turtle()
non.color("antiquewhite4")
dec = Turtle()



# for i in range(4):
#     timmy.forward(100)
#     timmy.left(90)

# for i in range(15):
#     timmy.forward(10)
#     timmy.penup()
#     timmy.forward(10)
#     timmy.pendown()

for i in range(3):
    tri.forward(100)
    tri.right(120)

for i in range(4):
    squ.forward(100)
    squ.right(90)

for i in range(5):
    pen.forward(100)
    pen.right(72)

for i in range(6):
    hex.forward(100)
    hex.right(60)

for i in range(7):
    hep.forward(100)
    hep.right(51.483)

for i in range(8):
    oct.forward(100)
    oct.right(45)

for i in range(9):
    non.forward(100)
    non.right(40)

for i in range(10):
    dec.forward(100)
    dec.right(36)


screen = Screen()
screen.exitonclick()
