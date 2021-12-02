"""
Вычисление приближенного интеграла с помощью: 1) Левых прямоугольников 2) Буля
ИУ7-16Б
Яремчук Иван
"""

import math
from ivanpy.foolproof import print_wrong, input_proof


def function(x: float) -> float:
    """
    Возвращает результат функции
    :param x: значение x
    :return: значение функции
    """
    return 4


def integral_analytical(x: float) -> float:
    """
    Возвращает значение первообразной
    :param x: значение x
    :return: значение первообразной
    """
    return 4*x


def print_table(l1: float, l2: float, l3: float, l4: float, n1: int, n2: int) -> None:
    """
    Выводит таблицу интегралов
    :param l1: интеграл метода прямоугольников для n1
    :param l2: интеграл метода прямоугольников для n2
    :param l3: интеграл метода Буля для n1
    :param l4: интеграл метода Буля для n2
    :param n1: количество отрезков разбиения 1
    :param n2: количество отрезков разбиения 1
    """
    print('-' * 34)
    print('|          |{:^10.4g}|{:^10.4g}|'.format(n1, n2))
    print('-' * 34)
    print('|Л прямоуг |{:^10.4g}|{:^10.4g}|'.format(l1, l2))
    print('-' * 34)
    if n1 % 4 != 0 and n2 % 4 != 0:
        print('|   Буля   |    NaN   |    NaN   |')
    elif n1 % 4 != 0:
        print('|   Буля   |    NaN   |{:^10.4g}|'.format(l4))
    elif n2 % 4 != 0:
        print('|   Буля   |{:^10.4g}|    NaN   |'.format(l3))
    else:
        print('|   Буля   |{:^10.4g}|{:^10.4g}|'.format(l3, l4))
    print('-' * 34)


def l_riemann(n: int, l_limit: float, r_limit: float) -> float:
    """
    Находит интеграл по методу левых прямоугольников
    :param n: количество отрезков разбиения
    :param l_limit: левая граница
    :param r_limit: правая граница
    :return: значение интеграла
    """
    result = 0
    step = (r_limit - l_limit) / n
    for i in range(n):
        x0 = l_limit + i * step
        x1 = x0 + step
        result += function(x0) * (x1 - x0)
    return result


def boole(n: int, l_limit: float, r_limit: float) -> float:
    """
    Находит интеграл по методу Буля
    :param n: количество отрезков разбиения
    :param l_limit: левая граница
    :param r_limit: правая граница
    :return: значение интеграла
    """
    if n % 4 != 0:
        return math.inf
    result = 0
    counter = 0
    temp_sum = 0
    coef = [7, 32, 12, 32, 7]
    step = (r_limit - l_limit) / n
    for i in range(n + 1):
        x = l_limit + i * step
        temp_sum += coef[counter] * function(x)
        counter += 1
        if counter == 5:
            result += temp_sum * 2 * step / 45
            counter = 0
            temp_sum = coef[counter] * function(x)
            counter += 1
    return result


def n_accuracy_eps(epsilon: float, l_limit: float, r_limit: float, max_iter: int, type_f='l_riemann') -> int:
    """
    Находит n, для которого значение будет вычесленно с заданной точностью
    :param epsilon: точность
    :param l_limit: левая граница
    :param r_limit: правая граница
    :param max_iter: максимальное колиечство итераций
    :param type_f: метод нахождения интеграла
    :return: значение найденного n
    """
    def integral(num: int) -> float:
        """
        Находит значение интеграла
        :param num: количество отрезков разбиения
        :return: значение интеграла
        """
        if type_f == 'l_riemann':
            return l_riemann(num, l_limit, r_limit)
        else:
            return boole(num, l_limit, r_limit)

    n = 1
    while True:
        if abs(integral(n) - integral(2 * n)) < epsilon:
            return n
        if n > max_iter:
            return -1
        n *= 2


# Предзаданные параметры
n_iters = 1000000

# Ввод
eps = input('Введите точность: ')
if input_proof(inpt=eps, type_proof='float', left_limit=0):
    eps = float(eps)
else:
    print_wrong()
start = input('Введите начало отрезка: ')
if input_proof(inpt=start):
    start = float(start)
else:
    print_wrong()
end = input('Введите конец отрезка: ')
if input_proof(inpt=end, left_limit=start):
    end = float(end)
else:
    print_wrong()
len_section1 = input('Введите количество участков разбиения: ')
if input_proof(inpt=len_section1, type_proof='int', left_limit=1):
    len_section1 = int(len_section1)
else:
    print_wrong()
len_section2 = input('Введите количество участков разбиения: ')
if input_proof(inpt=len_section2, type_proof='int', left_limit=1):
    len_section2 = int(len_section2)
else:
    print_wrong()

# Подсчет интегралов и вывод таблицы
I1 = l_riemann(len_section1, start, end)
I2 = l_riemann(len_section2, start, end)
I3 = boole(len_section1, start, end)
I4 = boole(len_section2, start, end)
print_table(I1, I2, I3, I4, len_section1, len_section2)

# Нахождение истинного интеграла
integral_true = integral_analytical(end) - integral_analytical(start)

# Нахождение ошибок для n1
absolute_error_riemann = abs(integral_true - I1)
absolute_error_boole = abs(integral_true - I3)
relative_error_riemann = absolute_error_riemann / abs(I1) if I1 != 0 else 0
relative_error_boole = absolute_error_boole / abs(I3) if I3 != 0 else 0

# Нахождение ошибок для n1
absolute_error_riemann1 = abs(integral_true - I2)
absolute_error_boole1 = abs(integral_true - I4)
relative_error_riemann1 = absolute_error_riemann1 / abs(I2) if I2 != 0 else 0
relative_error_boole1 = absolute_error_boole1 / abs(I4) if I4 != 0 else 0

# Вывод величин абсолютных ошибок
print('Абсолютная ошибка метода прямоугольников:'
      ' {:.4g} для n1 и {:.4g} для n2'.format(absolute_error_riemann, absolute_error_riemann1))
if absolute_error_boole1 == math.inf:
    absolute_error_boole1 = relative_error_boole1
if absolute_error_boole == math.inf:
    absolute_error_boole = relative_error_boole
print('Абсолютная ошибка метода Буля:'
      ' {:.4g} для n1 и {:.4g} для n2'.format(absolute_error_boole, absolute_error_boole1))

# Вывод величин относительных ошибок
print('Относительная ошибка метода прямоугольников:'
      ' {:.4g} для n1 и {:.4g} для n2'.format(relative_error_riemann, relative_error_riemann1))
print('Относительная ошибка метода Буля:'
      ' {:.4g} для n1 и {:.4g} для n2'.format(relative_error_boole, relative_error_boole1))

# Вывод n для менее точного метода
if absolute_error_riemann <= absolute_error_boole and absolute_error_riemann1 <= absolute_error_boole1\
        or len_section1 % 4 != 0 and len_section2 % 4 != 0:
    print('Более точный метод левых прямоугольников')
    ans = n_accuracy_eps(type_f='boole', l_limit=start, r_limit=end, epsilon=eps, max_iter=n_iters)
    print('Для метода Буля:')
else:
    print('Более точный метод Буля')
    ans = n_accuracy_eps(type_f='l_riemann', l_limit=start, r_limit=end, epsilon=eps, max_iter=n_iters)
    print('Для левых прямоугольников:')

if ans == -1:
    print('За {} итераций нужная точность {:.4g} не достигнута'.format(n_iters, eps))
else:
    print('При n = {} будет достигнута точность {:.4g}'.format(ans, eps))
