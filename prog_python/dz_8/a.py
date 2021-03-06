
from __future__ import annotations
from sys import stdin
from typing import List


class Matrix:
    def __init__(self, arr) -> None:
        if isinstance(arr, Matrix):
            arr = arr.arr
        self.arr = []
        for line in arr:
            self.arr.append(line.copy())

    def copy(self):
        return self.__class__(self.arr)

    def __str__(self) -> str:
        return "\n".join(["\t".join(map(str, line)) for line in self.arr])

    def size(self):
        if not len(self.arr):
            return (0, 0)
        return (len(self.arr), len(self.arr[1]))

    def __add__(self, other: Matrix):
        if self.size() != other.size():
            raise MatrixError(self, other)
        result = self.copy()
        for i in range(len(other.arr)):
            for j in range(len(other.arr[0])):
                result.arr[i][j] += other.arr[i][j]
        return result

    @staticmethod
    def _matrix_mult(mat_1, mat_2):
        result = []
        for row_n in range(len(mat_1)):
            result.append([])
            for column_n in range(len(mat_2[0])):
                _sum = 0
                for n in range(len(mat_2)):
                    _sum += mat_1[row_n][n] * mat_2[n][column_n]
                result[row_n].append(_sum)
        return result

    def __mul__(self, other):
        result = self.copy()
        if isinstance(other, float) or isinstance(other, int):
            for i in range(len(result.arr)):
                for j in range(len(result.arr[0])):
                    result.arr[i][j] *= other
        elif isinstance(other, Matrix):
            if self.size()[1] != other.size()[0]:
                raise MatrixError(self, other)
            result.arr = Matrix._matrix_mult(self.arr, other.arr)

        return result

    __rmul__ = __mul__

    def transpose(self):
        if not len(self.arr):
            return self
        transposed = []
        for i in range(len(self.arr[0])):
            transposed.append([])
            for j in range(len(self.arr)):
                transposed[i].append(self.arr[j][i])
        self.arr = transposed
        return self

    def solve(self, free_coeff: List):
        matrix = self.copy()
        coeff = Matrix([free_coeff]).transpose()
        for i in range(len(matrix.arr)):
            lider_line_num = get_lider_line(matrix.arr, i, i)
            if lider_line_num < 0:
                raise MatrixError(self, Matrix(free_coeff))
            if lider_line_num != i:
                matrix.element_premutation_2(lider_line_num, i)
                coeff.element_premutation_2(lider_line_num, i)
                lider_line_num = i
            lider = matrix.arr[i][i]
            matrix.element_premutation_3(lider_line_num, 1 / lider)
            coeff.element_premutation_3(lider_line_num, 1 / lider)
            for line_num in range(i + 1, len(matrix.arr)):
                if matrix.arr[line_num][i]:
                    lamb = -matrix.arr[line_num][i]
                    matrix.element_premutation_1(
                        line_num, lider_line_num, lamb)
                    coeff.element_premutation_1(line_num, lider_line_num, lamb)
        for i in range(len(matrix.arr) - 1, -1, -1):
            for line_num in range(i - 1, -1, -1):
                if matrix.arr[line_num][i]:
                    lamb = -matrix.arr[line_num][i]
                    matrix.element_premutation_1(line_num, i, lamb)
                    coeff.element_premutation_1(line_num, i, lamb)
        return coeff.transpose().arr[0]

    def element_premutation_2(self, line_1, line_2):
        self.arr[line_1], self.arr[line_2] = self.arr[line_2], self.arr[line_1]

    def element_premutation_1(self, target_line, source_line, lamb):
        for i in range(len(self.arr[0])):
            self.arr[target_line][i] += lamb * self.arr[source_line][i]

    def element_premutation_3(self, target_line, lamb):
        for i in range(len(self.arr[0])):
            self.arr[target_line][i] *= lamb

    @staticmethod
    def transposed(matrix: Matrix):
        m = matrix.copy()
        return m.transpose()

    @classmethod
    def create_id_matrix(cls, size):
        arr = [[0 for _ in range(size)] for __ in range(size)]
        for i in range(size):
            arr[i][i] = 1
        return Matrix(arr)


def get_lider_line(arr, start_line, linder_index):
    for i in range(start_line, len(arr)):
        if arr[start_line][linder_index]:
            return i
    return -1


class MatrixError(BaseException):
    def __init__(self, m_1: Matrix, m_2: Matrix):
        self.matrix1 = m_1
        self.matrix2 = m_2


class SquareMatrix(Matrix):

    def __pow__(self, pow):
        if pow == 0:
            return Matrix.create_id_matrix(len(self.arr))
        if pow == 1:
            return self.copy()
        if pow % 2 == 0:
            return (self * self) ** int(pow / 2)
        else:
            return self * (self ** (pow - 1))


exec(stdin.read())
