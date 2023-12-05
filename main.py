from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time

screen = Screen()
screen.bgcolor('black')
screen.setup(width=800, height=600)
screen.title('Pong')
screen.tracer(0)

paddle_L = Paddle(position=(-350, 0))
paddle_R = Paddle(position=(350, 0))
ball = Ball()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(paddle_R.up, 'Up')
screen.onkey(paddle_R.down, 'Down')
screen.onkey(paddle_L.up, 'w')
screen.onkey(paddle_L.down, 's')

game_is_on = True
while game_is_on:
    time.sleep(ball.ball_speed)
    screen.update()
    ball.move()
    #detect collision with up & down walls.
    if ball.ycor() >280 or ball.ycor() <-280:
        ball.bounce_y()
    #detect collision with paddle.
    if ball.distance(paddle_R)<50 and ball.xcor()>320 or ball.distance(paddle_L)<50 and ball.xcor()<-320:
        ball.bounce_x()
        ball.ball_speed *= 0.9
    elif ball.xcor()>380:
        scoreboard.l_scoreplus()
        ball.home()
        ball.ball_speed = 0.1
        ball.bounce_x()
    elif ball.xcor()<-380:
        scoreboard.r_scoreplus()
        ball.home()
        ball.ball_speed = 0.1
        ball.bounce_x()









screen.exitonclick()