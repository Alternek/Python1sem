"""
Вычисление приближенного интеграла с помощью: 1) Левых прямоугольников 2) Буля
ИУ7-16Б
Яремчук Иван
"""

import math
from ivanpy.foolproof import print_wrong, input_proof


def function(x: float) -> float:
    return math.cos(x)


def integral_analytical(x: float) -> float:
    return math.sin(x)


def print_table(l1: float, l2: float, l3: float, l4: float, n1: int, n2: int) -> None:
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
    result = 0
    step = (r_limit - l_limit) / n
    for i in range(n):
        x0 = l_limit + i * step
        x1 = x0 + step
        result += function(x0) * (x1 - x0)
    return result


def boole(n: int, l_limit: float, r_limit: float) -> float:
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
    def integral(num: int) -> float:
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
        n += 1


n_iters = 10000
eps = 0.001

start = input('Введите начало отрезка: ')
if input_proof(inpt=start):
    start = float(start)
else:
    print_wrong()
end = input('Введите конец отрезка: ')
if input_proof(inpt=end):
    end = float(end)
else:
    print_wrong()
len_section1 = input('Введите количество участков разбиения: ')
if input_proof(inpt=len_section1, type_proof='int'):
    len_section1 = int(len_section1)
else:
    print_wrong()
len_section2 = input('Введите количество участков разбиения: ')
if input_proof(inpt=len_section2, type_proof='int'):
    len_section2 = int(len_section2)
else:
    print_wrong()

I1 = l_riemann(len_section1, start, end)
I2 = l_riemann(len_section2, start, end)
I3 = boole(len_section1, start, end)
I4 = boole(len_section2, start, end)
print_table(I1, I2, I3, I4, len_section1, len_section2)

integral_true = integral_analytical(end) - integral_analytical(start)

absolute_error_riemann = abs(integral_true - I1)
absolute_error_boole = abs(integral_true - I3)
relative_error_riemann = absolute_error_riemann / abs(I1) if I1 != 0 else 0
relative_error_boole = absolute_error_boole / abs(I3) if I3 != 0 else 0

absolute_error_riemann1 = abs(integral_true - I2)
absolute_error_boole1 = abs(integral_true - I4)
relative_error_riemann1 = absolute_error_riemann1 / abs(I2) if I2 != 0 else 0
relative_error_boole1 = absolute_error_boole1 / abs(I4) if I4 != 0 else 0

if absolute_error_riemann <= absolute_error_boole and absolute_error_riemann1 <= absolute_error_boole1:
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
    print('Для {} будет достигнута точность {:.4g}'.format(ans, eps))
