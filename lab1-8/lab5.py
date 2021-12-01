"""
Вычисление суммы ряда с точностью
x_(n+1) = x ^ n / n
Яремчук Иван Валерьевич
ИУ7-16Б
"""


# x - аргумент, eps - точность, iter_count - количество итераций, step - шаг печати
# Ввод
x = float(input('Введите аргумент: '))
eps = float(input('Введите точность: '))
iter_count = int(input('Введите максимальное количество итераций: '))
step = int(input('Введите целый шаг печати: '))
# s - сумма ряда, added - добавление на шаге
s = 1
added = 1
# sum_eps_exists - дошли ли мы до суммы с точностью
sum_eps_exists = False
# Вывод таблицы
print('━' * 46)
print('┃ № итерации ┃       t       ┃       s       ┃')
print('┃' + '━' * 44 + '┃')
for num_step in range(1, iter_count):
    if (num_step - 1) % step == 0:
        print('┃ {:<11.5g}┃ {:<14.5g}┃ {:<14.5g}┃'.format(num_step, added, s))
    if added < eps:
        print('━' * 46)
        print('Сумма бесконечного ряда - {:.5g}, вычислена за {} итераций'.format(s, num_step))
        sum_eps_exists = True
        break
    # Изменение прибавления и добавление к сумме
    if num_step != 1:
        added *= (num_step - 1)
    added *= x
    added /= num_step
    s += added
if not sum_eps_exists:
    print('━' * 46)
    print('За {} итераций не дошли до суммы с точностью {}'.format(iter_count, eps))
