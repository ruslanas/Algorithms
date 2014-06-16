__author__ = 'Ruslanas'

from tkinter import *
import random

class Point():
    def __init__(self, x, y):
        self.x = x
        self.y = y

def branch(start, levels, length):
    if levels > 0:
        end = Point(start.x + random.randint(-20, 20), start.y - random.randint(int(0.3 * length), length))
        canvas.create_line(start.x, start.y, end.x, end.y)
        length *= 0.8
        for i in range(random.randint(1,3)):
            branch(end, levels - 1, int(length))

if __name__ == '__main__':
    root = Tk()

    w = 600
    h = 300

    canvas = Canvas(root, width=w, height=h)
    canvas.pack()

    start = Point(50, h)

    branch_length = 50

    for i in range(7):
        branch(start, 6, branch_length)
        start.x += random.randint(50, 100)

    mainloop()