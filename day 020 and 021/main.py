from turtle import Screen
from snake import Snake
from food import Food
from score import Score
import time

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("The snake game")
screen.tracer(0)

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

snake = Snake()
food = Food()
score = Score()
screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

game_status = True

while game_status:
    screen.update()
    time.sleep(0.1)
    snake.move()

    if snake.head.distance(food) < 15:  # Collision with food
        food.refresh()
        snake.extend()
        score.score_count()

    if snake.head.xcor() > 300 or snake.head.xcor() < -300 or snake.head.ycor() > 300 or snake.head.ycor() < -300: # Detect collision with wall
        #print("wall")
        game_status = False
        score.game_over()

    for part in snake.segments:
        if part == snake.head:
            pass
        elif snake.head.distance(part) < 10:
            #print("tail")
            game_status = False
            score.game_over()
screen.exitonclick()
