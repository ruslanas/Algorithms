__author__ = 'Ruslanas'

from tkinter import *
import random
import math


class Point():
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def rotate(self, origin, angle):
        dx = self.x - origin.x
        dy = self.y - origin.y
        rad = angle * math.pi / 180
        self.x = dx * math.cos(rad) - dy * math.sin(rad)
        self.y = dx * math.sin(rad) + dy * math.cos(rad)

        self.x += origin.x
        self.y += origin.y


def branch(start, levels=7, length=100, width=1, start_angle=0, trunk=False):
    if levels > 0:

        end = Point(start.x, start.y - random.randint(int(var * length), length))
        if trunk:
            angle = 0
        else:
            angle = start_angle + random.randint(-70, 70)
        end.rotate(start, angle)

        width /= 1 + 1/levels

        canvas.create_line(start.x, start.y, end.x, end.y, width=width, tags=3)
        length *= 0.618  # golder ratio

        for i in range(random.randint(2, 3)):
            branch(end, random.randint(levels - 2, levels - 1), int(length), width, angle)

def seed(start, generations, height, distance):
    dead_zone = 10

    for i in range(1, generations):
        branch(start, trunk=True, width=3, levels=generations - i,
               length=random.randint(int(var * height), int(height)))

        # drop seed both directions

        start.x += random.randint(int(-distance), int(distance))

        # younger trees
        height *= golden_ratio
        distance *= golden_ratio

        if round(dead_zone) <= 0 or round(distance) <= 0:
            break


if __name__ == '__main__':
    root = Tk()
    root.title('Forest')

    w = 800
    h = 500

    canvas = Canvas(root, width=w, height=h)
    canvas.pack()

    # parent

    var = 0.7  # variability

    golden_ratio = 0.8

    # plant
    seed(Point(w/2, h), generations=10, height=160, distance=240)
    seed(Point(w/2 + 150, h), generations=10, height=100, distance=100)

    mainloop()