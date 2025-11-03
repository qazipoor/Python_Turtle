import random
import turtle as t
from random_RGB import random_rgb

screen = t.Screen()
screen.colormode(255)
tim = t.Turtle()
tim.pensize(10)
tim.speed(0)

direction = [0, 90, 180, 270]

for _ in range(200):
    tim.pencolor(random_rgb())
    tim.setheading(random.choice(direction))
    tim.forward(30)

screen.exitonclick()
