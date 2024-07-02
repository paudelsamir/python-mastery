from turtle import Turtle, Screen

tim = Turtle()
screen = Screen()


def move_forwards():
    tim.forward(20)
def move_backward():
    tim.backward(20)
def turn_right():
    new_heading = tim.heading() - 20
    tim.setheading(new_heading)
def turn_left():
    new_heading = tim.heading() + 20
    tim.setheading(new_heading)
def clear():
    tim.clear()
    tim.penup()
    tim.home()
    tim.pendown()
       

screen.listen()
screen.onkey(move_forwards, "w")
screen.onkey(move_backward, "s")
screen.onkey(turn_left, "a")
screen.onkey(turn_right, "d")
screen.onkey(clear, "c")
screen.exitonclick()
