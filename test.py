import pgzrun
from random import randint
from pygame import Rect

WIDTH = 300
HEIGHT = 300

def draw():
    screen.clear()  # clears the previoous frame

    r = randint(120, 255)
    g = randint(120, 255)
    b = randint(120, 255)

    width = WIDTH
    height = HEIGHT - 200

    for i in range(20):
        rect = Rect((0, 0), (width, height))
        rect.center = (150, 150)

        screen.draw.rect(rect, (r, g, b))



        width =width- 10
        height =height+ 10
pgzrun.go()       