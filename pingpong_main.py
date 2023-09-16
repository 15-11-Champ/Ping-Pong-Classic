import turtle
from turtle import *
import random

ballNum = random.randint(1, 4)
print(ballNum)

screen = turtle.Screen()
screen.title("Ping Pong!")
screen.bgcolor("Black")
screen.setup(width=800, height=600)
screen.tracer(0)

# Score
score_a = 0
score_b = 0
score = turtle.Turtle()
score.color("White")
score.penup()
score.hideturtle()
score.goto(0, 250)
score.write("0 : 0", True, align="center", font=("Arial", 18, "normal"))

# paddle A
paddle_a = turtle.Turtle()
paddle_a.shape("square")
paddle_a.color("white")
paddle_a.shapesize(stretch_wid=5, stretch_len=1)
paddle_a.penup()
paddle_a.goto(-350, 0)

# paddle B
paddle_b = turtle.Turtle()
paddle_b.shape("square")
paddle_b.color("white")
paddle_b.shapesize(stretch_wid=5, stretch_len=1)
paddle_b.penup()
paddle_b.goto(350, 0)

# Ball
ball = turtle.Turtle()
ball.shape("square")
ball.color("white")
ball.penup()
ball.goto(0, 0)
ball.dx, ball.dy = 0, 0


def paddle_a_up():
    a_y = paddle_a.ycor()
    a_y += 23
    if a_y >= 250:
        a_y = 250
    paddle_a.sety(a_y)


def paddle_a_down():
    a_y = paddle_a.ycor()
    a_y -= 23
    if a_y <= -250:
        a_y = -250
    paddle_a.sety(a_y)


def paddle_b_up():
    b_y = paddle_b.ycor()
    b_y += 23
    if b_y >= 250:
        b_y = 250
    paddle_b.sety(b_y)


def paddle_b_down():
    b_y = paddle_b.ycor()
    b_y -= 23
    if b_y <= -250:
        b_y = -250
    paddle_b.sety(b_y)

collision = False


if ballNum == 1:
    ball.dx = 3
    ball.dy = 2
elif ballNum == 2:
    ball.dx = -3
    ball.dy = 2
elif ballNum == 3:
    ball.dx = -3
    ball.dy = -2
elif ballNum == 4:
    ball.dx = 3
    ball.dy = -2

# Key Binds
screen.listen()
screen.onkeypress(paddle_a_up, "w")
screen.onkeypress(paddle_a_down, "s")
screen.onkeypress(paddle_b_up, "Up")
screen.onkeypress(paddle_b_down, "Down")

a_x, a_y = paddle_a.xcor(), paddle_a.ycor()
b_x, b_y = paddle_b.xcor(), paddle_b.ycor()

while True:
    screen.update()

    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)

    if ball.ycor() > 290:
        ball.dy *= -1

    if ball.ycor() < -280:
        ball.dy *= -1

    if ball.xcor() > 380:
        ball.goto(0, 0)
        ball.dx *= -1
        score_a += 1
        score.clear()
        score.goto(0, 250)
        score.write(f"{score_a} : {score_b}", align="center", font=("Arial", 18, "normal"))
        print(f"A = {score_a}")

    if ball.xcor() < -390:
        ball.goto(0, 0)
        ball.dx *= -1
        score_b += 1
        score.clear()
        score.goto(0, 250)
        score.write(f"{score_a} : {score_b}", align="center", font=("Arial", 18, "normal"))
        print(f"B = {score_b}")

    if (-340 > ball.xcor() > -350) and (paddle_a.ycor() + 50 > ball.ycor() > paddle_a.ycor() - 50):
        ball.setx(-340)
        ball.dx *= -1
    if (340 < ball.xcor() < 350) and (paddle_b.ycor() + 50 > ball.ycor() > paddle_b.ycor() - 50):
        ball.setx(340)
        ball.dx *= -1
