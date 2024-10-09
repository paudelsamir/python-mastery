import turtle as turtle_module
from colorlist_in_RGB import color
import random

DOT_SIZE = 20
GRID_SIZE = 10
GAP_SIZE = 15

def draw_hirst_painting(toe, dot_size, grid_size, gap_size, colors):
    toe.speed("fastest")  

    for y in range(-grid_size // 2, grid_size // 2):
        for x in range(-grid_size // 2, grid_size // 2):
            random_color = random.choice(colors)
            turtle_color = "#{:02x}{:02x}{:02x}".format(random_color[0], random_color[1], random_color[2])
            
            toe.penup()
            toe.goto(x * (dot_size + gap_size), y * (dot_size + gap_size))
            toe.dot(dot_size, turtle_color)

toe = turtle_module.Turtle()

draw_hirst_painting(toe, DOT_SIZE, GRID_SIZE, GAP_SIZE, color)

screen = turtle_module.Screen()
screen.exitonclick()
