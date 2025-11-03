from turtle import Turtle, Screen

tim = Turtle()
tim.shape("turtle")

shapes = [
    {"shape": "triangle", "sides": 3, "color": "DeepSkyBlue2"},
    {"shape": "square", "sides": 4, "color": "gold1"},
    {"shape": "pentagon", "sides": 5, "color": "IndianRed1"},
    {"shape": "hexagon", "sides": 6, "color": "green4"},
    {"shape": "heptagon", "sides": 7, "color": "LightSalmon4"},
    {"shape": "octagon", "sides": 8, "color": "HotPink"},
    {"shape": "nonagon", "sides": 9, "color": "navy"},
    {"shape": "decagon", "sides": 10, "color": "VioletRed"},
]

for i in range(len(shapes)):
    angel = 360 / shapes[i]["sides"]
    sides = shapes[i]["sides"]
    color = shapes[i]["color"]

    for _ in range(sides):
        tim.color(color)
        tim.forward(100)
        tim.right(angel)


screen = Screen()
screen.exitonclick()
