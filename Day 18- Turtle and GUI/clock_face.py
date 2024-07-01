import turtle
import datetime

def draw_clock(h, m, s):
    t.penup()
    t.goto(0, -200)
    t.pendown()
    t.circle(200)
    
    for _ in range(12):
        t.penup()
        t.goto(0, 0)
        t.setheading((_ * 30) - 90)
        t.forward(180)
        t.pendown()
        t.forward(20)
    
    hands = [('red', 80, h * 30), ('blue', 120, m * 6), ('green', 160, s * 6)]
    for color, length, angle in hands:
        t.penup()
        t.goto(0, 0)
        t.color(color)
        t.setheading(angle - 90)
        t.pendown()
        t.forward(length)

t = turtle.Turtle()
t.speed(0)
s = turtle.Screen()
s.bgcolor("lightgray")

now = datetime.datetime.now()
draw_clock(now.hour % 12, now.minute, now.second)

turtle.done()