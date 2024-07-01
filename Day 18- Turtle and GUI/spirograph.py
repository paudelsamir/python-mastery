import turtle
import random

t = turtle.Turtle()
t.speed(0)
turtle.colormode(255)

for _ in range(100):
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    t.pencolor(r, g, b)
    
    t.circle(100)
    t.left(10)

turtle.done()