from turtle import Turtle, Screen

tim = Turtle()
tim.pensize(5)
screen = Screen()


def move_forward():
    tim.forward(25)

def move_backward():
    tim.backward(25)


def clockwise():
    new_head = tim.heading() - 10
    tim.setheading(new_head)


def anticlock():
    new_head = tim.heading()+10
    tim.setheading(new_head)


def clear_screen():
    tim.clear()
    tim.penup()
    tim.setpos(0,0)
    tim.setheading(0)
    tim.pendown()




screen.listen()  # telling the screen object to start listening
screen.onkey(key="w", fun=move_forward)  # when a function is passed as argument no parantheses are there
screen.onkey(key="s", fun=move_backward)
screen.onkey(key="a", fun=clockwise)
screen.onkey(key="d", fun=anticlock)
screen.onkey(key="c", fun=clear_screen)
screen.exitonclick()
