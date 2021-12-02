# cos(x) правые прямоугольники


import math


def func(x: float) -> float:
    return math.cos(x)


def integral(x: float) -> float:
    return math.sin(x)


def r_riemann(n: int, left: float, right: float):
    result = 0
    step = (right - left) / n
    for i in range(1, n + 1):
        x0 = left + (i - 1) * step
        x1 = left + i * step
        result += func(x1) * (x1 - x0)
    return result


def n_accuracy_eps(eps: float, left: float, right: float):
    n = 1
    back_integral = r_riemann(1, left, right)
    while True:
        if abs(back_integral - r_riemann(2 * n, left, right)) < eps:
            return back_integral
        n *= 2
        back_integral = r_riemann(n, left, right)


l_limit = float(input('Введите левую границу: '))
r_limit = float(input('Введите правую границу: '))
if l_limit > r_limit:
    print('Неправильные данные')
    exit()
epsilon = float(input('Введите точность: '))
print('Интеграл с точностью {:.4g} - {:.6g}'.format(epsilon, n_accuracy_eps(epsilon, l_limit, r_limit)))
