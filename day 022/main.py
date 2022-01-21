from turtle import Turtle, Screen
import time
from paddel import Paddel
from ball import Ball
from score import Score

screen = Screen()
screen.setup(height=600, width=800)
screen.bgcolor("black")
screen.title("PONG- The Arcade Game")
screen.tracer(0)

r_paddle = Paddel((350, 0))
l_paddle = Paddel((-350, 0))
ball = Ball()
score = Score()

screen.listen()
screen.onkey(r_paddle.move_up, "Up")
screen.onkey(r_paddle.move_down, "Down")
screen.onkey(l_paddle.move_up, "w")
screen.onkey(l_paddle.move_down, "s")

game_status = True
while game_status:
    time.sleep(ball.pace)
    screen.update()
    ball.move()

    if ball.ycor() > 280 or ball.ycor() < -280:  # Detecting collision with the ball
        ball.bounce_y()  # bounce when ball touches top or bottom

    if ball.distance(r_paddle) < 50 and ball.xcor() > 325 or ball.distance(l_paddle) < 50 and ball.xcor() < -325:  # Collision of ball with paddel
        ball.bounce_x()

    if ball.xcor() > 400:  # when ball misses the right paddle
        ball.goto(0, 0)
        ball.pace = 0.1
        ball.bounce_x()
        score.l_point()

    if ball.xcor() < -400:  # when ball misses the left paddel
        ball.goto(0, 0)
        ball.pace = 0.1
        ball.bounce_x()
        score.r_point()

screen.exitonclick()
