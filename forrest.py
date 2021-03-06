__author__ = 'Ruslanas'

from tkinter import *
import random
import math

geometry = []


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


class Fruit():
    def __init__(self, shape=1, color='red', size=3):
        self.shape = shape
        self.color = color
        self.size = size

    def draw(self, start):
        # stem
        geometry.append(canvas.create_line(start.x, start.y, start.x, start.y + 5))
        tl = Point(start.x - self.size, start.y + self.size)
        br = Point(start.x + self.size, start.y + 5 + self.size * 2)
        if self.shape == 1:
            geometry.append(canvas.create_oval(tl.x, tl.y, br.x, br.y, fill=self.color))


class Species():
    def __init__(self, length=100, angle=60, width=1, color='black', fruit=Fruit()):
        self.length = length
        self.width = width
        self.angle = angle
        self.color = color
        self.fruit = fruit

    def branch(self, start, levels=7, width=1, start_angle=0, trunk=False, length=100):
        var = 0.8
        if levels > 0:

            end = Point(start.x, start.y - random.randint(int(var * length), length))
            if trunk:
                angle = 0
            else:
                angle = start_angle + random.randint(-self.angle, self.angle)
            end.rotate(start, angle)

            width /= 1 + 1 / levels

            geometry.append(canvas.create_line(start.x, start.y, end.x, end.y, width=width, fill=self.color))
            length *= 0.618  # golder ratio

            for i in range(random.randint(2, 3)):
                levels = random.randint(levels - 2, levels - 1)
                self.branch(end, levels=levels, start_angle=angle, length=int(length), width=width)

        else:
            self.fruit.draw(start)


def seed(location, species, generations, spread):
    var = 0.8  # branch length variability
    generation_branch_length = species.length
    spread_var = 0.8

    for i in range(1, generations):

        species.branch(location, trunk=True, width=4, levels=generations - i,
                       length=random.randint(int(var * generation_branch_length), int(generation_branch_length)))

        # drop seed both directions
        location.x += random.randint(int(-spread), int(spread))

        # younger trees
        generation_branch_length *= 0.618
        spread *= spread_var


def save():
    canvas.postscript(file='forest.eps')


def clear():
    for line in geometry:
        canvas.delete(line)
    del geometry[:]


def generate():
    for i in range(1, 20):
        x = random.randint(100, 700)
        base_length = random.randint(150, 250)
        angle = random.randint(10,80)
        spread = random.randint(100, 400)

        value = 80 * 1/i
        color = '#%02x%02x%02x' % (20, 20, value)

        apple = Fruit(color='green')
        random_tree = Species(length=base_length, angle=angle, color=color, fruit=apple)

        # plant
        seed(Point(x, h), random_tree, generations=10, spread=spread)


if __name__ == '__main__':
    root = Tk()
    root.title('Forrest generator')

    w = 800
    h = 600

    toolbar = Frame(root)
    toolbar.pack(fill=X)

    generate_button = Button(toolbar, text='Generate', command=generate)
    generate_button.pack(side=LEFT)
    clear_button = Button(toolbar, text='Clear', command=clear)
    clear_button.pack(side=LEFT)
    save_button = Button(toolbar, text='Save', command=save)
    save_button.pack(side=RIGHT)

    canvas = Canvas(root, width=w, height=h)
    canvas.config(background='#C4DAF6')
    canvas.pack()

    sun_position = Point(70, 50)
    canvas.create_oval(sun_position.x, sun_position.y, sun_position.x + 100, sun_position.y + 100, fill='white', outline='white')

    mainloop()