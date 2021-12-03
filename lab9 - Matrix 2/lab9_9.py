"""
Яремчук Иван
ИУ7-16
"""
from ivanpy.foolproof import int_proof, input_proof, print_wrong


# Ввод
inpt = input('Введите размерность матрицы (x, y, z) в строчку: ').split()
if len(inpt) != 3 or not (int_proof(inpt[0]) and int_proof(inpt[1]) and int_proof(inpt[2])):
    print_wrong()
x, y, z = [int(i) for i in inpt]
matrix_matrix = [[[0 for q in range(z)] for j in range(y)] for i in range(x)]
for i in range(x):
    for j in range(y):
        for q in range(z):
            input_el = input('Введите элемент с координатами ({}, {}, {}): '.format(i, j, q))
            if input_proof(inpt=input_el, amount_of_numbers=1):
                el = float(input_el)
                matrix_matrix[i][j][q] = el
            else:
                print_wrong()
# Вывод среза
ind = input('Введите номер среза: ')
if input_proof(inpt=ind, left_limit=0, right_limit=y-1, amount_of_numbers=1, type_proof='int'):
    ind = int(ind)
    print('Вывод среза:')
    for i in range(x):
        for q in range(z):
            print('{:^7.3g}'.format(matrix_matrix[i][ind][q]), end=' ')
        print()
else:
    print_wrong()
