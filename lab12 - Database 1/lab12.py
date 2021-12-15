"""
База данных
Яремчук Иван
ИУ7-16Б
"""


from ivanpy.foolproof import input_proof, float_proof, int_proof


def create_menu() -> int:
    """
    Создает бесконечное меню и ждет корректного номера команды
    :return: номер команды
    """
    print('0. Выйти из программы\n'
          '1. Выбрать файл для работы\n'
          '2. Инициализировать базу данных\n'
          '3. Вывести содержимое базы данных\n'
          '4. Добавить запись в базу данных\n'
          '5. Поиск по номеру пакета\n'
          '6. Поиск записей с курсом акций больше значения и данным сектором\n')
    command_index = input('Введите номер команды: ')
    if input_proof(inpt=command_index, type_proof='int', left_limit=0, right_limit=6):
        command_index = int(command_index)
        return command_index
    else:
        return create_menu()


def init_db(field_types: list[str], field_names: list[str], file_path: str) -> None:
    """
    Инициализирует файл как базу данных
    Все, что там было, очищается
    :param field_types: типы полей
    :param field_names: имена полей
    :param file_path: путь файла
    """
    with open(file_path, 'w+') as file:
        file.write(create_head_db(field_types) + '\n')
        file.write(create_head_db(field_names))


def create_head_db(fields: list[str]) -> str:
    """
    Создает head базы данных
    :param fields: поля
    :return: head
    """
    return ifs.join(fields)


def select_file(file_path: str) -> None:
    """
    Выбирает/создает файл
    :param file_path: путь файла
    """
    global current_file
    try:
        open(file_path, 'a+').close()
        current_file = file_path
    except:
        print('Файл не найден и его нельзя создать')


def screen_split(line: str) -> list[str]:
    """
    Разбирает запись на элементы учитывая экранирование
    :param line: запись
    :return: разбитую запись
    """
    list_line = ['']
    line = line.replace('\n', '')
    screen_symbol = False
    for symbol in line:
        if symbol == ifs:
            if screen_symbol:
                list_line[-1] += ifs
            else:
                list_line.append('')
            screen_symbol = False
        elif symbol == '\\':
            if screen_symbol:
                screen_symbol = False
                list_line[-1] += symbol
            else:
                screen_symbol = True
        else:
            screen_symbol = False
            list_line[-1] += symbol
    return list_line


def print_db() -> None:
    """
    Выводит содержание базы данных
    """
    with open(current_file, 'r') as file:
        line_types = screen_split(file.readline())
        line_names = screen_split(file.readline())
        for name in line_names:
            print('{:^25}'.format(name), end=' ')
        print()
        for line in file:
            line = screen_split(line)
            for obj, obj_type in zip(line, line_types):
                if obj_type == 'str':
                    print('{:^25}'.format(obj), end=' ')
                elif obj_type == 'int':
                    print('{:^25.5g}'.format(int(obj)), end=' ')
                else:
                    print('{:^25.5g}'.format(float(obj)), end=' ')
            print()
        print()


def check_curr_file() -> bool:
    """
    Проверяет файл на принадлежность к базам данных
    :return: является ли файл базой данных
    """
    try:
        with open(current_file, 'r') as file:
            line_types = screen_split(file.readline())
            line_names = screen_split(file.readline())
            if len(line_types) != len(line_names) or line_types == [''] or line_names == ['']:
                return False
            for line in file:
                line = screen_split(line)
                for obj, obj_type in zip(line, line_types):
                    if obj_type == 'int':
                        if not int_proof(obj):
                            return False
                    elif obj_type == 'float':
                        if not float_proof(obj):
                            return False
            return True
    except:
        return False


def screen(row: str) -> str:
    """
    Экранирует запись
    :param row: изначальная запись
    :return: экранированная запись
    """
    return row.replace('\\', '\\\\').replace(';', '\\;')


def can_record(row: str) -> bool:
    """
    Проверяет на возможность записи
    :param row: запись
    :return: возможна ли запись
    """
    row = screen_split(row)
    with open(current_file, 'r') as file:
        types = screen_split(file.readline())
        if len(row) != len(types):
            return False
        for obj, obj_type in zip(row, types):
            if obj_type == 'int' and not int_proof(obj):
                return False
            if obj_type == 'float' and not float_proof(obj):
                return False
    return True


def write_record(row: str) -> None:
    """
    Делает запись
    :param row: запись
    """
    with open(current_file, 'a') as file:
        file.write('\n' + row)


def find_element(element: str, index: int) -> None:
    """
    Находит записи по полю
    :param element: элемент
    :param index: индекс поля
    :return:
    """
    with open(current_file, 'r') as file:
        line_types = screen_split(file.readline())
        line_names = screen_split(file.readline())
        print('Найденные записи: ')
        for name in line_names:
            print('{:^25}'.format(name), end=' ')
        print()
        for line in file:
            line = screen_split(line)
            if line[index] == element:
                for obj, obj_type in zip(line, line_types):
                    if obj_type == 'str':
                        print('{:^25}'.format(obj), end=' ')
                    elif obj_type == 'int':
                        print('{:^25.4g}'.format(int(obj)), end=' ')
                    else:
                        print('{:^25.4g}'.format(float(obj)), end=' ')
                print()


def find_elements(elements: list, indexes: list[int]) -> None:
    """
    Находит записи по полям
    :param elements: элементы
    :param indexes: поля
    :return:
    """
    with open(current_file, 'r') as file:
        line_types = screen_split(file.readline())
        line_names = screen_split(file.readline())
        print('Найденные записи: ')
        for name in line_names:
            print('{:^25}'.format(name), end=' ')
        print()
        for line in file:
            line = screen_split(line)
            if float(line[indexes[0]]) >= elements[0] and line[indexes[1]] == elements[1]:
                for obj, obj_type in zip(line, line_types):
                    if obj_type == 'str':
                        print('{:^25}'.format(obj), end=' ')
                    elif obj_type == 'int':
                        print('{:^25.4g}'.format(int(obj)), end=' ')
                    else:
                        print('{:^25.4g}'.format(float(obj)), end=' ')
                print()


# Глобальные параметры
ifs = ';'
current_file = ''
fields_names = ['Индекс пакета', 'Название', 'Курс акций', 'Сектор', 'Курс год назад']
fields_types = ['int', 'str', 'float', 'str', 'float']

# Основной цикл
while True:
    # Вывод меню и чтение команды
    command = create_menu()
    if command == 0:
        # Выход из программы
        exit()
    elif command == 1:
        # Выбор файла для работы
        select_file(input('Введите путь до файла: '))
    elif command == 2:
        # Инициализация базы данных
        if current_file:
            init_db(fields_types, fields_names, current_file)
        else:
            print('Файл не выбран или недоступен')
    elif command == 3:
        # Вывод содержимого базы данных
        if current_file and check_curr_file():
            print_db()
        else:
            print('Файл не выбран или не является базой данных')
    elif command == 4:
        # Добавление записи в базу данных
        if check_curr_file():
            len_record = input('Введите длину записи: ')
            if input_proof(inpt=len_record, left_limit=1, right_limit=len(fields_types), type_proof='int'):
                len_record = int(len_record)
            else:
                print('Неверная длина')
                continue
            print('Введите запись по элементу в строке: ')
            record = ifs.join([screen(input()) for _ in range(len_record)])
            if can_record(record):
                write_record(record)
            else:
                print('Запись нельзя записать')
        else:
            print('Файл не выбран или не является базой данных')
    elif command == 5:
        # Поиск записей по номеру пакета
        if check_curr_file():
            element_to_find = input('Введите значение для поиска по номеру пакета: ')
            find_element(element_to_find, 0)
        else:
            print('Файл не выбран или не является базой данных')
    else:
        # Поиск записей с курсом акций больше значения и данным сектором
        if check_curr_file():
            el1 = input('Введите значение для поиска по курсам акций, больше заданого: ')
            if float_proof(el1):
                el2 = input('Введите значение для поиска по сектору: ')
                find_elements([float(el1), el2], [2, 3])
            else:
                print('Курс акций неверен')
        else:
            print('Файл не выбран или не является базой данных')
