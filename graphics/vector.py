__author__ = 'Ruslanas'

from graphics.matrix import Matrix
from math import sin, cos, pi


class Vec3():
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

    def rotate_x(self, angle):
        angle = angle * pi / 180
        vector_matrix = Matrix([[self.x, self.y, self.z]])
        vector_matrix.transpose()
        rotation_matrix = Matrix([
            [1, 0, 0],
            [0, cos(angle), -sin(angle)],
            [0, sin(angle), cos(angle)]
        ])
        vec = rotation_matrix * vector_matrix
        self.x = vec(1,1)
        self.y = vec(2,1)
        self.z = vec(3,1)
        return self


if __name__ == '__main__':
    v = Vec3(0, 1, 0)
    print(v.rotate_x(45))