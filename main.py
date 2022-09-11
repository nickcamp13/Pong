import time

from paddle import Paddle
from ball import Ball
from turtle import Screen

screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("Pong")
screen.tracer(0)

paddle_l = Paddle(x=-350)
paddle_r = Paddle(x=350)
ball = Ball()

screen.listen()
screen.onkey(paddle_l.move_up, "w")
screen.onkey(paddle_l.move_down, "s")
screen.onkey(paddle_r.move_up, "Up")
screen.onkey(paddle_r.move_down, "Down")

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    ball.move()

    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()

    if (ball.distance(paddle_r) < 25 or ball.distance(paddle_l) < 25) or (
            (ball.distance(paddle_r) < 43 and ball.xcor() > 320) or (
                    ball.distance(paddle_l) < 43 and ball.xcor() < -320)):
        ball.bounce_x()

screen.exitonclick()
