__author__ = 'Ruslanas'
"""
A little bit of school math and operator overloading.
"""


class Matrix():
    def __init__(self, matrix):
        self.matrix = matrix
        self.rows = len(matrix)
        self.columns = len(matrix[0])

    def __add__(self, scalar):
        output = []
        for i in range(self.rows):
            row_output = []
            for j in range(self.columns):
                row_output.append(self.matrix[i][j] + scalar)
            output.append(row_output)

        return output

    def __mul__(self, operand):
        if isinstance(operand, int):
            output = []
            for i in range(self.rows):
                row_output = []
                for j in range(self.columns):
                    row_output.append(self.matrix[i][j] * operand)
                output.append(row_output)

            return output
        else:
            return self.product(operand.matrix)

    def product(self, v2):
        v1 = self.matrix
        n = len(v1)
        m = len(v2[0])
        p = len(v2)
        v3 = []

        for i in range(n):
            out_row = []
            for j in range(m):
                s = 0
                for k in range(p):
                    try:
                        s += v1[i][k] * v2[k][j]
                    except IndexError as e:
                        print(e)
                out_row.append(s)

            v3.append(out_row)

        return v3


if __name__ == '__main__':
    a = Matrix([
        [1, 2, 3],
        [6, 5, 4]])
    b = Matrix([[1, 3],
                [3, 4],
                [5, 6]])

    print(a * b)
    print(a + 4)
    print(a * 3)