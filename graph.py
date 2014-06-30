__author__ = 'Ruslanas'

from graphics.vector import Vec3
from tkinter import *

root = Tk()

canvas = Canvas(root, width=100, height=100)

vec = Vec3(0, 50, 0)
canvas.pack()
for i in range(9):
    vec.rotate_x(5)
    canvas.create_line(0, 0, vec.y, vec.z)
mainloop()
