# t_(n+1) = 1/sqrt(n)
eps = float(input('Введите точность: '))
iter_count = int(input('Введите максимальное количество итераций: '))
step = float(input('Введите целый шаг печати: '))
s = 1
added = 1
sum_eps_exists = False
print('-'*46)
print('| № итераций |       t       |        s      |')
print('|' + '-'*44 + '|')
for iter_num in range(1, iter_count + 1):
    if (iter_num - 1) % step == 0:
        print('|{:<12}|{:<15.5g}|{:<15.5g}|'.format(iter_num, added, s))
    if added <= eps:
        print('-' * 46)
        print('Сумма бесконечного ряда - {:.5g}, вычислена за {} итераций'.format(s, iter_num))
        sum_eps_exists = True
        break
    added = 1 / iter_num ** 0.5
    s += added
if not sum_eps_exists:
    print('-' * 46)
    print('С точностью {} за {} итераций нельзя найти сумму'.format(eps, iter_count))
