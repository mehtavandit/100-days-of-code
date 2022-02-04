<h1 align="center">
    100 Days of Code: Day 23
  <br>
</h1>

## Objective
- The aim of this game is to make sure that turtle crosses the path without colliding with any cars.

##main.py
- Create a 600*600 pixel screen.
- The collision between the automobile and the turtle is detected.
- The turtle returns to the starting line as soon as it crosses the finish line, and the next level begins.

## player.py
- A turtle is generated and placed at position (0,-280) with its head set to 90 degrees.
- Functions up() and down() are defined that cause the turtle to move forward and downward when the up and down arrows are pressed, respectively.
- The function is_at_finish_line() determines if the turtle has reached the finish line and returns true when it has, otherwise false.

## car_manager.py
- Function create_car() generate different amount of cars at every second and place them at random locations along the y-axis (x-axis being constant).
- The car's speed is set at 5 units during level 1, however as the level progresses, function increase_speed() raises the car's speed by 2.5 units.
- A function named move_car() enables all of the cars to move at a definite pace from right to left.


## scoreboard.py
- A scoreboard which trackes the number of levels passed is intialized and kept at postition (-280,260). 
- When the turtle passes a level, the function level up() increases the score by one, and the function update score() updates the score.
- Whenever the turtle collides with the car, the function game over() prints "GAME OVER" in the middle of the screen.
