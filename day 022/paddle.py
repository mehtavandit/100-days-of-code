from turtle import Turtle


class Paddel(Turtle):

    def __init__(self, position):
        super().__init__()
        self.shape("square")
        self.color("white")
        self.penup()
        self.speed("fastest")
        self.turtlesize(stretch_wid=5, stretch_len=1)
        self.setpos(position[0], position[1])

    def move_up(self):
        y_cor = self.ycor() + 25
        self.goto(self.xcor(), y_cor)

    def move_down(self):
        y_cor = self.ycor() - 25
        self.goto(self.xcor(), y_cor)
