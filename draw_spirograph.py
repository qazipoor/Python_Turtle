import turtle as t
from random_RGB import random_rgb

screen = t.Screen()
t.mode("logo")
t.colormode(255)

tim = t.Turtle()
tim.speed("fastest")

heading = 0
gap = 5
rotation = int(360 / gap)

for _ in range(rotation):
    tim.pencolor(random_rgb())
    tim.circle(120)
    heading -= gap
    tim.setheading(heading)



screen.exitonclick()
