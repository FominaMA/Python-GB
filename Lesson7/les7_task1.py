# 1. Реализовать класс Matrix (матрица).
# Обеспечить перегрузку конструктора класса (метод __init__()), который должен принимать данные (список списков) для формирования матрицы.
#
# Подсказка: матрица — система некоторых математических величин, расположенных в виде прямоугольной схемы.
#
# Примеры матриц вы найдете в методичке.
#
# Следующий шаг — реализовать перегрузку метода __str__() для вывода матрицы в привычном виде.
#
# Далее реализовать перегрузку метода __add__() для реализации операции сложения двух объектов класса Matrix (двух матриц).
# Результатом сложения должна быть новая матрица.
#
# Подсказка: сложение элементов матриц выполнять поэлементно — первый элемент первой строки первой матрицы складываем с
#                                                                   первым элементом первой строки второй матрицы и т.д.
import numpy as np

class Matrix:
    def __init__(self, line, column,matrix):
        self.line = line
        self.column = column
        self.matrix = matrix
        matrix_line = []
        for i in range(self.column):
            for k in range(self.line):
                el = int(input(f"Введите элемент матрицы {i + 1}-{k + 1}: "))
                matrix_line.append(el)
            self.matrix.append(matrix_line)
            matrix_line = []

    def __str__(self):
        matrix_str = ''
        for k in range(self.column):
            matrix_str = matrix_str + ' '.join(map(str, self.matrix[k])) + '\n'
        return matrix_str

    def __add__(self, other):
        if self.column != other.column or self.line != other.line:
            return print("Нельзя складывать матрицы разного размера!")

        else:
            summa_matrix = ''
            for k in range(self.column):
                column_1 = self.matrix[k]
                column_2 = other.matrix[k]
                summa_matrix_line = []
                for i in range(len(column_1)):
                    summa_matrix_line.append(column_1[i] + column_2[i])
                summa_matrix = summa_matrix + ' '.join(map(str, summa_matrix_line)) + '\n'
            return summa_matrix


matrix_1 = Matrix(2, 2, [])
print(matrix_1)

matrix_2 = Matrix(3, 2, [])
print(matrix_2)
print("Сумма матриц равна:")
print(matrix_1 + matrix_2)

# Ей богу, будто заполняем модуль numpy.....