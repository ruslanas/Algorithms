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

def branch(start, levels=7, length=100, width=1, start_angle=0):
    if levels > 0:

        var = 0.8
        end = Point(start.x, start.y - random.randint(int(var * length), length))

        angle = start_angle + random.randint(-30, 30)
        end.rotate(start, angle)

        canvas.create_line(start.x, start.y, end.x, end.y, width=width, tags=3)
        length *= 0.618 # golder ratio
        width *= 0.618

        for i in range(random.randint(2,3)):
            branch(end, random.randint(levels - 2, levels - 1), int(length), width, angle)

if __name__ == '__main__':
    root = Tk()

    w = 600
    h = 300

    canvas = Canvas(root, width=w, height=h)
    canvas.pack()

    start = Point(70, h)

    branch_length = 50
    height = 160 # parent height
    var = 0.7
    for i in range(7):
        branch(start, width=3, length=random.randint(int(var * height), int(height)))
        # drop seed
        start.x += random.randint(20, 130)
        # seed generation
        height = 0.8 * height

    mainloop()