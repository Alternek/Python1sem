"""
Яремчук Иван
ИУ7-16
"""
from ivanpy.foolproof import print_wrong, input_matrix


# Ввод
A = input_matrix()
B = input_matrix()
if len(A) != len(B) or len(A[0]) != len(B[0]):
    print_wrong()
# Создание C
C = []
for i in range(len(A)):
    adds = []
    for j in range(len(A[0])):
        adds.append(A[i][j] * B[i][j])
    C.append(adds)
# Создание V
V = []
for j in range(len(A[0])):
    s = 0
    for i in range(len(A)):
        s += C[i][j]
    V.append(s)
# Вывод
print('Массив V:')
for i in V:
    print(format(i, '.5g'), end=' ')
