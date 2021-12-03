"""
Яремчук Иван
ИУ7-16
"""
from ivanpy.foolproof import input_matrix


# Ввод
matrix = input_matrix(square=True)
n = len(matrix)
mx = matrix[0][0]
mn = matrix[n - 1][n - 1]
# Нахождение минимумов и максимумов
for i in range(n):
    for j in range(n):
        if i + j < n:
            mx = max(mx, matrix[i][j])
        else:
            mn = min(mn, matrix[i][j])
# Вывод
print('Максимум: {:^5.5g}'.format(mx))
print('Минимум: {:^5.5g}'.format(mn))
