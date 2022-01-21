<h1 align="center">
    100 Days of Code: Day 22
  <br>
</h1>

## Objective
- The aim is to hit the ball so that it goes over the net and bounces on the opponent's half of the table in such a way that the opponent cannot reach it or return it correctly.

## main.py
- Initialize the screen of height 600px and width 800px, having background color black
- Checks the collision of the ball with top and bottom of the screen
- Checks collision of the ball with paddle 
- Checks whether the player has missed the ball or not

## paddle.py
- Decides the coordinates of both the paddles
- Keys for left paddle: w to move up, s to move down
- Keys for right paddle: upper arrow to move up, down arrow to move down

## ball.py
- Initialize the ball of radius 20 and sets it to origin
- If the ball hits the top or bottom of the screen, function is defined to make sure that it bounce back along the y-axis
- If the ball hits the paddle, function is defined so that it bounce back along the x-axis

## score.py
- Intialize the score of both the players to 0, and is placed at the top of the screen
- Keeps the track of the score
