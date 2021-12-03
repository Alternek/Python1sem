"""
Яремчук Иван
ИУ7-16
"""
from ivanpy.foolproof import input_matrix, input_array
from ivanpy.matrixpy import print_matrix


# Ввод
D = input_matrix()
I_arr = input_array(type_proof='int', left_limit=0, right_limit=len(D) - 1)
R = []
# Создание R и average
for i in I_arr:
    R.append(max(D[i]))
average = sum(R) / len(R)
# Вывод
print('Матрица D:')
print_matrix(D)
print('-'*40)
print('Массив I:')
print(*I_arr)
print('-'*40)
print('Среднее значение:')
print(format(average, '.5g'))
