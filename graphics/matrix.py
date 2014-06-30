__author__ = 'Ruslanas'
"""
A little bit of school math and operator overloading.
"""


class Matrix():
    def __repr__(self):
        output = []
        for i in range(self.rows):
            output.append("[" + ",".join(map(lambda x: str(x), self.matrix[i])) + "]")

        return 'graphics.matrix.Matrix([' + ",".join(output) + '])'

    def __call__(self, n, m):
        return self.matrix[n - 1][m - 1]

    def __getitem__(self, n):
        return self.matrix[n]

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

    def __str__(self):
        return self.matrix.__str__()

    def __mul__(self, operand):
        if isinstance(operand, (int, float)):
            output = []
            for i in range(self.rows):
                row_output = []
                for j in range(self.columns):
                    row_output.append(self.matrix[i][j] * operand)
                output.append(row_output)

            return output
        elif isinstance(operand, self.__class__):
            return self.product(operand.matrix)
        else:
            raise TypeError('Unsupported operand type')

    @staticmethod
    def transpose(matrix):
        t = []
        for j in range(matrix.columns):
            row = []
            for i in range(matrix.rows):
                row.append(matrix.matrix[i][j])
            t.append(row)
        return Matrix(t)

    def transpose(self):
        t = []
        for j in range(self.columns):
            row = []
            for i in range(self.rows):
                row.append(self.matrix[i][j])
            t.append(row)
        self.__init__(t)
        return self

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
                    s += v1[i][k] * v2[k][j]
                out_row.append(s)

            v3.append(out_row)

        return Matrix(v3)


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
    print(a.transpose())
    print(a * a.transpose())
    print(Matrix.transpose(b))
    print(a(1,1))
    try:
        print(a * 'string')
    except TypeError as e:
        print(e)