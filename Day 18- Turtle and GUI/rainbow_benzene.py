import turtle
import colorsys #module which basically converts the hsv to rgb later in this program

t = turtle.Turtle()
s = turtle.Screen()
s.bgcolor("black")
t.speed(0)
n = 36
h = 0

for i in range(460):
    c = colorsys.hsv_to_rgb(h, 1, 0.8)
    h += 1/n
    t.color(c)
    t.forward(i*2)
    t.left(145)

turtle.done()