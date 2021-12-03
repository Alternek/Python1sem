"""
Построение таблицы и графика функции на промежутке
Изменяется q (от 0 до 1.2 с шагом 0.05)
x_1 = 2.97 * q**4 + 4.84 * q**3 - 16.4 * q ** 2 + 41.2 * q - 33.2
x_2 = 2 - q * math.e ** q
Оператор : for
Доп. задание :
1) Определить значение x_1_max - x_2_max
Яремчук Иван Валерьевич
ИУ7-16Б
"""

import math


# start_x - начальное знач x, end_x - конечное знач x, step_X - шаг x
# Ввод данных
start_x = float(input('Введите начальное значение x: '))
end_x = float(input('Ввдите конечное значение x: '))
step_x = float(input('Введите шаг x: '))
# star_count - количество символов выхода
# eps - точность сравнения
star_count = 120
eps = 0.0001
# mi_y - минимальное значение f(x) на промежутке, ma_y - максимальное значение f(x) на промежутке
# ma_y2 - максимальное значение g(x) на промежутке
mi_y = math.inf
ma_y = -math.inf
ma_y2 = -math.inf
# Вывод таблицы x f(x) g(x)
print('┃' + '━'*32 + '┃')
print('┃' + 'q' + ' '*9 + '┃' + 'x_1' + ' '*7 + '┃' + 'x_2' + ' '*7 + '┃')
print('┃' + '━'*32 + '┃')
for x in range(math.floor((end_x - start_x)/step_x) + 2):
    x = start_x + x*step_x
    if x > end_x + eps:
        break
    y1 = 2.97 * x**4 + 4.84 * x**3 - 16.4 * x ** 2 + 41.2 * x - 33.2
    y2 = 2 - x * math.e ** x
    if mi_y > y1:
        mi_y = y1
    if ma_y < y1:
        ma_y = y1
    if ma_y2 < y2:
        ma_y2 = y2
    print('┃{:<10.4g}┃{:<10.4g}┃{:<10.4g}┃'.format(x, y1, y2))
print('┃' + '━'*32 + '┃')
# x_pos - позиция оси x на графике, x_line_exists - сущесвование оси x на графике
x_line_exists = True
x_pos = round((0 - mi_y) / (ma_y - mi_y) * star_count)
if x_pos == 0:
    x_pos = 1
if x_pos < 0 or x_pos > star_count:
    x_line_exists = False
# y_out_count - количество засечек y
y_out_count = int(input('Введите количество засечек y (от 4 до 8): '))
if y_out_count not in [4, 5, 6, 7, 8]:
    exit('Количество засечек от 4 до 8')
# Вывод линии с засечек y
# width_y - длина шага засечек y, len_second_y - вторая засечка y, unused_stars -  оставшиеся символы засечек
# y_step - значение y на шаге засечек
width_y = math.floor(star_count / (y_out_count - 1))
y_step = (ma_y - mi_y) / (y_out_count - 1)
len_second_y = len(str(format(mi_y + y_step, '.4g')))
unused_stars = star_count - width_y * (y_out_count - 1)
print('┃━━━━━━━━━━┃{0:<{1}.4g}'.format(mi_y, width_y - len_second_y), end='')
for y_num in range(1, y_out_count):
    if y_num == 1:
        print('{:.4g}'.format(mi_y + y_step), end='')
    elif y_num == y_out_count - 1:
        print('{y:>{w_y}.4g}┃'.format(y=mi_y + y_step * y_num, w_y=width_y + unused_stars))
    else:
        print('{y:>{w_y}.4g}'.format(y=mi_y + y_step * y_num, w_y=width_y), end='')
print('┃' + '━' * 10 + '┃' + '━'*star_count + '┃')
# Вывод графика
for x in range(math.floor((end_x - start_x)/step_x) + 2):
    y_line_exists = False
    if (start_x + (x - 1) * step_x) < 0 and (start_x + (x + 1) * step_x) > 0:
        y_line_exists = True
    x = start_x + x * step_x
    if x > end_x + eps:
        break
    y = 2.97 * x**4 + 4.84 * x**3 - 16.4 * x ** 2 + 41.2 * x - 33.2
    # pos - позиция звездочки на графике
    pos = round((y - mi_y) / (ma_y - mi_y) * star_count)
    if pos == 0:
        pos = 1
    # out_str - строка вывода
    if y_line_exists:
        out_str = '-' * star_count
    if x_line_exists:
        if y_line_exists:
            out_str = '-'*(x_pos - 1) + '+' + '-'*(star_count - x_pos)
        else:
            out_str = ' ' * (x_pos - 1) + '|' + ' ' * (star_count - x_pos)
    else:
        out_str = ' ' * star_count
    out_str = out_str[:pos - 1] + '*' + out_str[pos:]
    print('┃{:<10.4g}┃'.format(x) + out_str + '┃')
print('┃' + '━'*(star_count + 11) + '┃')
# Доп задание
print('Разница между максимумом x_1 и максимумом x_2 = {:.4g}'.format(ma_y - ma_y2))
