"""
Яремчук Иван
ИУ7-16
"""
from ivanpy.foolproof import input_matrix
from ivanpy.matrixpy import print_matrix


def rotatematrix(mat: list[list]) -> list[list]:
    """
    Поворачивает матрицу на 90 по часовой
    :param mat: list[list]: матрица
    :return: list[list]: итоговая матрица
    """
    return[list(t) for t in zip(*mat[::-1])]


# Ввод
matrix = input_matrix(square=False)
matrix = rotatematrix(matrix)
# Поворот на 90 по часовой
print_matrix(matrix)
print('-'*40)
# поворот на 90 против часовой
matrix = rotatematrix(matrix)
matrix = rotatematrix(matrix)
matrix = rotatematrix(matrix)
print_matrix(matrix)
