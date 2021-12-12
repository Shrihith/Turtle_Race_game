import turtle
import random


# create window
wn = turtle.Screen()
wn.title("Turtle_Race")
wn.bgcolor("blue")

#turtle
turtle.color('white')
turtle.speed(0)
turtle.penup()
turtle.goto(-140,140)

for i in range(15):
	turtle.write(i)
	turtle.right(90)
	turtle.forward(10)
	turtle.pendown()
	turtle.forward(350)
	turtle.penup()
	turtle.backward(360)
	turtle.left(90)
	turtle.forward(20)

# players 1 to 5
player1 = turtle.Turtle()
player1.color("red")
player1.shape("turtle")
player1.shapesize(2)
#player1.speed(0)
player1.penup()
player1.goto(-170,100)
player1.pendown()\

player2 = turtle.Turtle()
player2.color("green")
player2.shape("turtle")
player2.shapesize(2)
#player2.speed(0)
player2.penup()
player2.goto(-170,40)
player2.pendown()

player3 = turtle.Turtle()
player3.color("yellow")
player3.shape("turtle")
player3.shapesize(2)
#player3.speed(0)
player3.penup()
player3.goto(-170,-20)
player3.pendown()

player4 = turtle.Turtle()
player4.color("black")
player4.shape("turtle")
player4.shapesize(2)
#player4.speed(0)
player4.penup()
player4.goto(-170,-80)
player4.pendown()

player5 = turtle.Turtle()
player5.color("brown")
player5.shape("turtle")
player5.shapesize(2)
#player5.speed(0)
player5.penup()
player5.goto(-170,-140)
player5.pendown()

# move around
for i in range(100):
	player1.forward(random.randint(1,5))
	player2.forward(random.randint(1,5))
	player3.forward(random.randint(1,5))
	player4.forward(random.randint(1,5))
	player5.forward(random.randint(1,5))

while True:
    wn.update()