import time
from turtle import Screen, Turtle
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard


screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)
screen.listen()

player=Player()
car_manager = CarManager()
score = Scoreboard()
screen.onkey(player.up, "Up")
screen.onkey(player.down,"Down")

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()

    car_manager.create_car()
    car_manager.move_cars()

    for car in car_manager.all_cars:  # Detecting collison between cars and turtle
        if car.distance(player)<20:
            game_is_on=False
            score.game_over()

    if player.is_at_finish_line(): # When the level is completed player gets to the starting line
        player.go_to_start()
        car_manager.increase_speed()
        score.level_up()

screen.exitonclick()
