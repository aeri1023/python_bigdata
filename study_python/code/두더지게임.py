import turtle
import random
t= turtle.Pen()
t.shape("turtle")
t.shapesize(5,5)
t.up()

def show(x,y):
    x=random.randint(-300,300)
    y=random.randint(-300,300)
    t.goto(x,y)
    print("잡았다")
t.onclick(show)
