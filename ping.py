# Import required library
import turtle


# Create screen
sc = turtle.Screen()
sc.title("Pong game")
sc.bgcolor("black")
sc.setup(width=1000, height=600)


# Left paddle
lpad = turtle.Turtle()
lpad.speed(0)
lpad.shape("square")
lpad.color("white")
lpad.shapesize(stretch_wid=6, stretch_len=2)
lpad.penup()
lpad.goto(-400, 0)


# Right paddle
rpad = turtle.Turtle()
rpad.speed(0)
rpad.shape("square")
rpad.color("white")
rpad.shapesize(stretch_wid=6, stretch_len=2)
rpad.penup()
rpad.goto(400, 0)


# Ball of circle shape
ball = turtle.Turtle()
ball.speed(40)
ball.shape("circle")
ball.color("blue")
ball.penup()
ball.goto(0, 0)
ball.dx = 5
ball.dy = -5


# Initialize the score
player1 = 0
player2 = 0


# Displays the score
score = turtle.Turtle()
score.speed(0)
score.color("blue")
score.penup()
score.hideturtle()
score.goto(0, 260)
score.write("player 1 : 0 player 2: 0",
			align="center", font=("Courier", 24, "normal"))


# Functions to move paddle vertically
def paddleaup():
	y = lpad.ycor()
	y += 20
	lpad.sety(y)


def paddleadown():
	y = lpad.ycor()
	y -= 20
	lpad.sety(y)


def paddlebup():
	y = rpad.ycor()
	y += 20
	rpad.sety(y)


def paddlebdown():
	y = rpad.ycor()
	y -= 20
	rpad.sety(y)


# Keyboard bindings
sc.listen()
sc.onkeypress(paddleaup, "e")
sc.onkeypress(paddleadown, "x")
sc.onkeypress(paddlebup, "Up")
sc.onkeypress(paddlebdown, "Down")


while True:
	sc.update()

	ball.setx(ball.xcor()+ball.dx)
	ball.sety(ball.ycor()+ball.dy)

	# Checking borders
	if ball.ycor() > 280:
		ball.sety(280)
		ball.dy *= -1

	if ball.ycor() < -280:
		ball.sety(-280)
		ball.dy *= -1

	if ball.xcor() > 500:
		ball.goto(0, 0)
		ball.dy *= -1
		player1 += 1
		score.clear()
		score.write("Left_player : {} Right_player: {}".format(
					player1, player2), align="center",
					font=("Courier", 24, "normal"))

	if ball.xcor() < -500:
		ball.goto(0, 0)
		ball.dy *= -1
		player2 += 1
		score.clear()
		score.write("Left_player : {} Right_player: {}".format(
								player1, player2), align="center",
								font=("Courier", 24, "normal"))

	# Paddle ball collision
	if (ball.xcor() > 360 and ball.xcor()<370) and (ball.ycor() < rpad.ycor()+40 and ball.ycor() > rpad.ycor()-40):
		ball.setx(360)
		ball.dx*=-1
		
	if (ball.xcor()<-360 and ball.xcor()>-370) and (ball.ycor()<lpad.ycor()+40 and ball.ycor()>lpad.ycor()-40):
		ball.setx(-360)
		ball.dx*=-1
