"""
Исследование методов сортировки
Шейкер-сортировка
Яремчук Иван
ИУ7-16Б
"""


from ivanpy.foolproof import int_proof
import random
from time import time


def generate_list(n: int, type_list: str) -> list[int]:
    """
    Генерирует массив
    :param n: длина
    :param type_list: тип массива
    :return: массив
    """
    if type_list == 'sort':
        return list(range(1, n + 1))
    if type_list == 'sort_reverse':
        return list(range(n, 0, -1))
    if type_list == 'unsort':
        lst = list(range(1, n + 1))
        random.shuffle(lst)
        return lst.copy()


def cocktail_sort(array_origin: list[int]) -> float:
    start = time()
    array = array_origin.copy()
    left = 0
    right = len(array) - 1
    while left <= right:
        for i in range(left, right, 1):
            if array[i] > array[i + 1]:
                array[i], array[i + 1] = array[i + 1], array[i]
        right -= 1

        for i in range(right, left, -1):
            if array[i - 1] > array[i]:
                array[i], array[i - 1] = array[i - 1], array[i]
        left += 1
    return time() - start


def timer(n: int, type_list: str) -> float:
    """
    Замеряет время сортировки
    :param n: длина массива
    :param type_list: тип массива
    :return: время в секундах
    """
    return cocktail_sort(generate_list(n, type_list))


def table(n1: int, n2: int, n3: int) -> None:
    t1 = timer(n1, 'sort')
    t2 = timer(n2, 'sort')
    t3 = timer(n3, 'sort')
    t4 = timer(n1, 'unsort')
    t5 = timer(n2, 'unsort')
    t6 = timer(n3, 'unsort')
    t7 = timer(n1, 'sort_reverse')
    t8 = timer(n2, 'sort_reverse')
    t9 = timer(n3, 'sort_reverse')
    print('-' * 85)
    print('|{:^20}|{:^20}|{:^20}|{:^20}|'.format('', n1, n2, n3))
    print('-' * 85)
    print('|{:^20}|{:^20.4g}|{:^20.4g}|{:^20.4g}|'.format('Упорядоченный список', t1, t2, t3))
    print('-' * 85)
    print('|{:^20}|{:^20.4g}|{:^20.4g}|{:^20.4g}|'.format('Случайный список', t4, t5, t6))
    print('-' * 85)
    print('|{:^20}|{:^20.4g}|{:^20.4g}|{:^20.4g}|'.format('Обратный список', t7, t8, t9))
    print('-' * 85)


N1 = input('Введите N1: ')
N2 = input('Введите N2: ')
N3 = input('Введите N3: ')
if int_proof(N1) and int_proof(N2) and int_proof(N3) and int(N1) > 0 and int(N2) > 0 and int(N3) > 0:
    table(int(N1), int(N2), int(N3))
else:
    print('Неправильный ввод!')
