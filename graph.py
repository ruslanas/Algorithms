__author__ = 'Ruslanas'

from graphics.vector import Vec3
from tkinter import *

root = Tk()

canvas = Canvas(root, width=100, height=100)
canvas.pack()

vec = Vec3(0, 50, 0)
origin = Vec3(50, 50, 0)

for i in range(12):
    canvas.create_line(origin.x, origin.y, (origin + vec).x, (origin + vec).y)
    vec.rotate_z(30)

mainloop()
