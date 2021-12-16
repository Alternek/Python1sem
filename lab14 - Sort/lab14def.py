# Пузырек с флагом


import random
import time


def generate_list(n: int, type_list: str) -> list[int]:
    if type_list == 'sort':
        return list(range(1, n + 1))
    if type_list == 'sort_reverse':
        return list(range(n, 0, -1))
    if type_list == 'unsort':
        lst = list(range(1, n + 1))
        random.shuffle(lst)
        return lst.copy()


def flag_sort(array_origin: list[int]) -> float:
    start = time.time()
    array = array_origin.copy()
    n = len(array)
    for i in range(n - 1):
        flag = True
        for j in range(n - 1 - i):
            if array[j] > array[j + 1]:
                array[j], array[j + 1] = array[j + 1], array[j]
                flag = False
        if flag:
            break
    return time.time() - start


def timer(n: int, type_list: str) -> float:
    return flag_sort(generate_list(n, type_list))


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


N1 = int(input('Введите N1:'))
N2 = int(input('Введите N2:'))
N3 = int(input('Введите N3:'))
table(N1, N2, N3)
