import numpy as np

class Matrix:
    def __init__(self, rows, cols, data=[]):
        self.rows = rows
        self.cols = cols
        if len(data) == 0:
            self.data = np.full((rows, cols), 0, dtype=int)
        else:
            self.data = data

    def __str__(self):
        text = ''
        for r in range(len(self.data)):
            text = f'{text} {" ".join(map(str, self.data[r]))}\n'
        return text

    def __repr__(self):
        return f'{self.rows} {self.cols}'

    def __eq__(self, other):
        return self.data == other.data

    def __add__(self, other):
        if np.array(self.data).shape == np.array(other.data).shape:
            row = np.array(self.data).shape[0]
            col = np.array(self.data).shape[1]
            output_data = np.full((row, col), 0, dtype=int)
            for i in range(row):
                for j in range(col):
                    output_data[i][j] = self.data[i][j] + other.data[i][j]
            return Matrix(row, col, output_data)

    def __mul__(self, other):
        if np.array(self.data).shape[1] == np.array(other.data).shape[0]:
            result_matrix = np.full((np.array(self.data).shape[0], np.array(self.data).shape[1]), 0, dtype=int)
            row = np.array(self.data).shape[0]
            col = np.array(self.data).shape[1]
            for i in range(row):
                for j in range(col):
                    result_matrix[i][j] = sum([self.data[i][n] * other.data[n][j] for n in range(col)])
            return Matrix(row, col, result_matrix)

matrix1 = Matrix(2, 3)
matrix1.data = [[1, 2, 3], [4, 5, 6]]

matrix2 = Matrix(2, 3)
matrix2.data = [[7, 8, 9], [10, 11, 12]]


print(matrix1)
print(matrix2)

print(matrix1 == matrix2)

matrix_sum = matrix1 + matrix2
print(matrix_sum)

matrix3 = Matrix(3, 2)
matrix3.data = [[1, 2], [3, 4], [5,6]]

matrix4 = Matrix(2, 2)
matrix4.data = [[7, 8], [9, 10]]

result = matrix3 * matrix4
print(result)