import time
from turtle import Screen

from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("PONG")

screen.tracer(0)
is_game_on = True
r_paddle = Paddle((350, 0))
l_paddle = Paddle((-350, 0))
ball = Ball()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(r_paddle.move_up, "Up")
screen.onkey(r_paddle.move_down, "Down")
screen.onkey(l_paddle.move_up, "w")
screen.onkey(l_paddle.move_down, "s")

speed = 0.1

while is_game_on:
    time.sleep(speed)
    screen.update()

    ball.move()
    if ball.ycor() > 250 or ball.ycor() < -250:
        ball.wall_bounce()
        speed *= 0.9

    if (ball.xcor() > 320 and ball.distance(r_paddle) < 50) or (ball.xcor() < -320 and ball.distance(l_paddle) < 50):
        ball.paddle_bounce()
        speed *= 0.9

    if ball.xcor() < -400:
        ball.ball_reset()
        speed = 0.1
        ball.move()
        scoreboard.r_point()
        scoreboard.write_score()

    if ball.xcor() > 400:
        ball.ball_reset()
        speed = 0.1
        ball.move()
        scoreboard.l_point()
        scoreboard.write_score()

screen.exitonclick()
