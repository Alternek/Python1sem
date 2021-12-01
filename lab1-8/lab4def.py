# 2sin(3x)/(cos(x)^2+1)

import math


start_x = float(input('Введите начальное значение x: '))
end_x = float(input('Ввдите конечное значение x: '))
step_x = float(input('Введите шаг x: '))
star_count = 120
eps = 0.0001
mi_y = math.inf
ma_y = -math.inf
for x in range(math.floor((end_x - start_x)/step_x) + 2):
    x = start_x + x * step_x
    if x > end_x + eps:
        break
    y = 2 * math.sin(3 * x) / (math.cos(x) ** 2 + 1)
    if mi_y > y:
        mi_y = y
    if ma_y < y:
        ma_y = y
x_line_exists = True
x_pos = round((0 - mi_y) / (ma_y - mi_y) * star_count)
if x_pos == 0:
    x_pos = 1
if x_pos < 0 or x_pos > star_count:
    x_line_exists = False
print('┃━━━━━━━━━━┃{0:<10.4g}'.format(mi_y) + ' ' * (star_count - 20) + '{0:>10.4g}┃'.format(mi_y))
for x in range(math.floor((end_x - start_x)/step_x) + 2):
    y_line_exists = False
    if (start_x + (x - 1) * step_x) < 0 and (start_x + (x + 1) * step_x) > 0:
        y_line_exists = True
    x = start_x + x * step_x
    if x > end_x + eps:
        break
    y = 2 * math.sin(3 * x) / (math.cos(x) ** 2 + 1)
    pos = round((y - mi_y) / (ma_y - mi_y) * star_count)
    if pos == 0:
        pos = 1
    if y_line_exists:
        out_str = '-' * star_count
    if x_line_exists:
        if y_line_exists:
            out_str = '-' * (x_pos - 1) + '+' + '-'*(star_count - x_pos)
        else:
            out_str = ' ' * (x_pos - 1) + '|' + ' ' * (star_count - x_pos)
    else:
        out_str = ' ' * star_count
    out_str = out_str[:pos - 1] + '*' + out_str[pos:]
    print('┃{:<10.4g}┃'.format(x) + out_str + '┃')
print('┃' + '━'*(star_count + 11) + '┃')
