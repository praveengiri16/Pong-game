import time
from turtle import Screen
from pong_block import CreateBlock
from pong_ball import CreateBall
from pong_scoreboard import ScoreBoard
game_on = True

s = Screen()
s.setup(width=800, height=600)
s.bgcolor("black")
s.tracer(0)

r_block = CreateBlock(370, 0)
l_block = CreateBlock(-370, 0)
r_score = ScoreBoard()
l_score = ScoreBoard()
r_score.r_update()
l_score.l_update()

s.listen()
s.onkey(fun=r_block.move_up, key="Up")
s.onkey(fun=r_block.move_down, key="Down")
s.onkey(fun=l_block.move_up, key="w")
s.onkey(fun=l_block.move_down, key="s")

ball = CreateBall()


while game_on:
    s.update()
    ball.move_ball()
    time.sleep(0.05)

    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.change_y()
    if ball.distance(r_block) < 50 and ball.xcor() > 340:
        ball.change_x()
    if ball.distance(l_block) < 40 and ball.xcor() < -350:
        ball.change_x()
    if ball.xcor() > 400:
        ball = CreateBall()
        l_score.l_count()
        l_score.l_update()
        ball.change_direction()
    if ball.xcor() < -400:
        ball = CreateBall()
        r_score.r_count()
        r_score.r_update()


s.exitonclick()
