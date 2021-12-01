"""
Яремчук Иван
ИУ7-16
"""
from ivanpy.foolproof import print_wrong, input_matrix
from ivanpy.matrixpy import print_matrix


# Ввод
print('Матрица D: ')
D = input_matrix()
print('Матрица Z: ')
Z = input_matrix()
G = []
if len(D) > len(Z):
    print_wrong()
# Создание G
for i in range(len(D)):
    s = sum(Z[i])
    G.append(max(sum(list(map(lambda x: int(x > s), D[i]))), 0))
# Вывод
print('D до преобразования: ')
print_matrix(D)
print('-'*40)
for i in range(len(D)):
    for j in range(len(D[0])):
        D[i][j] *= max(G)
print('D после преобразования: ')
print_matrix(D)
print('-'*40)
print('Массив G:', *G)
