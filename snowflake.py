import turtle

wn = turtle.Screen()
bob = turtle.Turtle()

bob.color("cyan")
wn.bgcolor("grey")

bob.penup()
bob.forward(90)
bob.left(45)
bob.pendown()

def branch():
    for i in range(3):
        for i in range(3):
            bob.forward(30)
            bob.backward(30)
            bob.right(45)
        bob.left(90)
        bob.backward(30)
        bob.left(45)
    bob.right(90)
    bob.forward(90)

for i in range(8):
    branch()
    bob.left(45)

wn.exitonclick()
