from turtle import Turtle


class Score(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        self.color("white")
        self.penup()
        self.goto(0, 265)
        self.write(f"Score: {self.score}", align="center", font=("Arial", 15, "normal"))
        self.hideturtle()

    def score_count(self):
        self.score += 1
        self.clear()
        self.write(f"Score: {self.score}", align="center", font=("Arial", 15, "normal"))

    def game_over(self):
        self.clear()
        self.goto(0, 0)
        self.write(f"GAME OVER: \n SCORE : {self.score}", align="center", font=("Arial", 15, "normal"))
