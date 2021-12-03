"""
Программа для работы с массивами
Яремчук Иван Валерьевич
ИУ7-16Б
"""


# Проверяет является ли строка int
def check_str_int(s):
    return s.lstrip('-').isdecimal()


# Проверяет является ли строка float
def check_str_float(s):
    s = s.lstrip('-')
    if s.find('e.') + 1 or s.find('.e') + 1 or s[0] == 'e' or s[-1] == 'e':
        return False
    s = s.replace('.', '', 1)
    s = s.replace('e-', '', 1)
    s = s.replace('e+', '', 1)
    s = s.replace('e', '', 1)
    return s.isdecimal()


# Выводит меню и принимает номер команды
def create_menu():
    print('0. Выйти из программы\n'
          '1. Проинициализировать список первыми n элементами x_n+1 = x^n / n\n'
          '2. Очистить список и ввести его с клавиатуры\n'
          '3. Добавить элемент в произвольное место списка\n'
          '4. Удалить произвольный элемент из списка (по номеру)\n'
          '5. Очистить список\n'
          '6. Найти значение K-го экстремума в списке\n'
          '7. Найти наиболее длинную возрастающую последовательность целых четных чисел\n')
    num_command = input('Введите номер комманды : ')
    if check_str_int(num_command) and 0 <= int(num_command) <= 7:
        return int(num_command)
    else:
        print('Вводите целые значения от 0 до 7')
        return create_menu()


# Инициализирует список первыми N элементами x_(n+1) = x^n / n
def ini_array(n):
    if n < 0:
        return []
    global_array = [1]
    x = input('Введите аргумент: ')
    if check_str_float(x):
        x = float(x)
    else:
        print('ВВОДИТЕ ЧИСЛА')
        return []
    added = 1
    for num_step in range(1, n):
        if num_step != 1:
            added *= (num_step - 1)
        added *= x
        added /= num_step
        global_array.append(added)
    return global_array


# Очищает список и вводит его с калвиатуры
def clear_create_array():
    arr = input().split()
    out_arr = []
    for el in arr:
        if check_str_float(el):
            out_arr.append(float(el))
        else:
            print('ВВОДИТЕ ЧИСЛА')
            return []
    return out_arr


# Добавляет элемент в произвольное место списка
def add_el(global_array, index, el):
    if index > len(global_array) or index < 0:
        print('Индекс вставки вне массива')
        return global_array
    global_array.insert(index, el)
    return global_array


# Удаляет элемент по индексу
def del_el(global_array, index):
    if index >= len(global_array) or index < 0:
        print('Индекс удаления вне массива')
        return global_array
    global_array.pop(index)
    return global_array


# Очищает массив
def clear_array():
    return []


# Находит k-тый экстремум
def find_ex_k(global_array, k):
    if k <= 0:
        print('Номер экстремума должен быть больше 0')
        return
    for ind in range(1, len(global_array) - 1):
        if global_array[ind - 1] >= global_array[ind] <= global_array[ind + 1]:
            k -= 1
        if global_array[ind - 1] <= global_array[ind] >= global_array[ind + 1]:
            k -= 1
        if global_array[ind - 1] == global_array[ind] == global_array[ind + 1]:
            k += 1
        if k == 0:
            k -= 1
            print('Значение экстремума - {:.2g}'.format(global_array[ind]))
    if k > 0:
        print('Экстремума под этим номером в массиве нет')


# Находит наиболее длинную возраст. посл. четных целых чисел
def find_sequence(global_array):
    temp_array = []
    result_array = []
    for el in global_array:
        if int(el) == float(el) and el % 2 == 0 and (temp_array == [] or temp_array[-1] < el):
            temp_array.append(el)
        else:
            if len(result_array) < len(temp_array):
                result_array = temp_array.copy()
            temp_array.clear()
    if result_array:
        print('Последовательность : ', end='')
        for el in result_array:
            print(format(el, '.2g'), end=' ')
        print('')
    else:
        print('Такой последовательности нет')


# Выводит массив
def print_array(global_array):
    if global_array:
        print('Массив : ', end='')
        for el in global_array:
            print(format(el, '.2g'), end=' ')
        print('\n')
    else:
        print('Массив пуст\n')


# Тело программы
changing_array = []  # массив для работы
while True:
    # Создание меню
    ind_command = create_menu()
    if ind_command == 0:
        # Завершение работы
        break
    if ind_command == 1:
        # Инициализация
        N = input('Введите n : ')
        if check_str_int(N):
            changing_array = ini_array(int(N))
        else:
            print('n должен быть целым')
    if ind_command == 2:
        # Очистить и создать из ввода массив
        changing_array = clear_create_array()
    if ind_command == 3:
        # Добавление элемента
        index_el = input('Введите индекс (1 элемент - это индекс 0) : ')
        elem = input('Введите элемент : ')
        if check_str_int(index_el) and check_str_float(elem):
            changing_array = add_el(changing_array, int(index_el), float(elem))
        else:
            print('ВВОДИТЕ ЧИСЛА')
    if ind_command == 4:
        # Удаление элемента
        index_del = input('Введите индекс (1 элемент - это индекс 0) : ')
        if check_str_int(index_del):
            changing_array = del_el(changing_array, int(index_del))
        else:
            print('ВВОДИТЕ ЦЕЛЫЕ ИНДЕКСЫ')
    if ind_command == 5:
        # Очистка массива
        changing_array = clear_array()
    if ind_command == 6:
        # Нахождение экстремума
        K = input('Введите номер экстремума : ')
        if check_str_int(K):
            find_ex_k(changing_array, int(K))
        else:
            print('ВВОДИТЕ ЦЕЛЫЕ ИНДЕКСЫ')
    if ind_command == 7:
        # Нахождение последовательности
        find_sequence(changing_array)
    # Ввывод массива
    print_array(changing_array)
