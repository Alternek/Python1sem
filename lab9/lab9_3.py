"""
Яремчук Иван
ИУ7-16
"""
from ivanpy.foolproof import input_matrix


def transpose(matrix: list[list[int]]) -> list[list[int]]:
    """
    Транспонирует матрицу
    :param matrix: list[list[int]]: матрица для обработки
    :return: list[list[int]]: итоговая матрица
    """
    tr_matrix = [[matrix[j][i] for j in range(len(matrix))] for i in range(len(matrix[0]))]
    return tr_matrix


# Ввод
matrix = input_matrix(square=True)
n = len(matrix)
# Транспонирование
matrix = transpose(matrix)
# Вывод
print('Транспонированная матрица: ')
for i in range(n):
    for j in range(n):
        print('{:^7.3g}'.format(matrix[i][j]), end=' ')
    print()
