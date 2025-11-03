from random import randint

def random_rgb():
    r = randint(0, 255)
    g = randint(0, 255)
    b = randint(0, 255)

    random_color = (r, g, b)

    return random_color