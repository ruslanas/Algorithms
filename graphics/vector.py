__author__ = 'Ruslanas'

from graphics.matrix import Matrix
from math import sin, cos, pi, sqrt


class Vec3():
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

    def __abs__(self):
        return self.length()

    def __sub__(self, other):
        return Vec3(self.x - other.x, self.y - other.y, self.z - other.z)

    def __mul__(self, other):
        return Vec3(self.x * other, self.y * other, self.z * other)

    def __xor__(self, other):
        """
        Cross product A x B
        :param other:
        :return:
        """
        return Vec3(self.y * other.z - self.z * other.y, self.z * other.x - self.x * other.z,
                    self.x * other.y - self.y * other.x)

    def __add__(self, other):
        return Vec3(self.x + other.x, self.y + other.y, self.z + other.z)

    def __repr__(self):
        return "graphics.vector.Vec3(%f, %f, %f)" % (self.x, self.y, self.z)

    def rotate_z(self, angle):
        angle = angle * pi / 180
        vector_matrix = Matrix([[self.x, self.y, self.z]])
        vector_matrix.transpose()
        rotation_matrix = Matrix([
            [cos(angle), -sin(angle), 0],
            [sin(angle), cos(angle), 0],
            [0, 0, 1]
        ])
        vec = rotation_matrix * vector_matrix
        self.x = vec(1, 1)
        self.y = vec(2, 1)
        self.z = vec(3, 1)
        return self

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
        self.x = vec(1, 1)
        self.y = vec(2, 1)
        self.z = vec(3, 1)
        return self

    def normalize(self):
        vec = Vec3(self.x, self.y, self.z) * (1 / self.length())
        self.__init__(vec.x, vec.y, vec.z)
        return self

    def length(self):
        return sqrt(self.x * self.x + self.y * self.y + self.z * self.z)


def dot(a, b):
    return a.x * b.x + a.y * b.y + a.z * b.z


if __name__ == '__main__':
    v1 = Vec3(0.0, 1.0, 0.0)
    v2 = Vec3(1.0, 0.0, 0.0)
    print(v1 - v2)
    print(dot(v1, v2))
    print(v1.rotate_x(45))
    print(v1 ^ v2)
    print(Vec3(1, 1, 1).length())
    print(v1 + v2)
    print(abs(v2))
    v3 = Vec3(1, 1, 1)
    v3.normalize()
    print(v3.length())