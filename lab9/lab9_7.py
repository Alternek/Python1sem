"""
Яремчук Иван
ИУ7-16
"""
from ivanpy.foolproof import input_matrix
from ivanpy.matrixpy import print_matrix


# Ввод
matrix = input_matrix(type_proof='char')
# Замена символов
for i in range(len(matrix)):
    for j in range(len(matrix[0])):
        if matrix[i][j] in 'AaEeIiOoUuYy':
            matrix[i][j] = '.'
# Вывод
print('Матрица:')
print_matrix(matrix, type_el='char')
