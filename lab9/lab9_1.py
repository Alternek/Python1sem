"""
Создать из матрица D и F матрицу A, а по ней найти средние строк и кол элементов, меньших среднего
Яремчук Иван
ИУ7-16
"""
from ivanpy.foolproof import input_proof, print_wrong
import math

d = input('Введите массив D через пробел: ')
f = input('Введите массив F через пробел: ')
if input_proof(inpt=d, amount_of_numbers=0) and input_proof(inpt=f, amount_of_numbers=0):
    d = [float(i) for i in d.split()]
    f = [float(i) for i in f.split()]
    # Создание матрицы
    matrix = []
    for i in d:
        matrix.append(list(map(lambda x: math.sin(x + i), f)))
    av = []
    L = []
    # Создание L и av
    for i in range(len(matrix)):
        av_i = list(map(lambda x: max(x, 0), matrix[i]))
        k = sum(list(map(lambda x: int(x != 0), av_i)))
        if k != 0:
            av.append(sum(av_i) / k)
        else:
            av.append(0)
        if k != 0:
            L.append(sum(list(map(lambda x: int(x < sum(av_i) / k), matrix[i]))))
        else:
            L.append(0)
    # Вывод
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            print('{:^7.3g}'.format(matrix[i][j]), end=' ')
        print('| {:^7.3g}'.format(av[i]), end=' ')
        print('| {:^7.3g}'.format(L[i]))
else:
    print_wrong()
