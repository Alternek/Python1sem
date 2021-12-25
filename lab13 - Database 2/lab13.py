"""
База данных в бинарнике
Яремчук Иван
ИУ7-16Б
"""


from ivanpy.foolproof import input_proof, float_proof, int_proof
import struct


def create_menu() -> int:
    """
    Создает бесконечное меню и ждет корректного номера команды
    :return: номер команды
    """
    print('0. Выйти из программы\n'
          '1. Выбрать файл для работы\n'
          '2. Инициализировать базу данных (файл очищается)\n'
          '3. Вывести содержимое базы данных\n'
          '4. Добавить запись в базу данных\n'
          '5. Удалить запись из базы данных по индексу (нумерация с 0)\n'
          '6. Поиск по номеру пакета\n'
          '7. Поиск записей с курсом акций больше значения и данным сектором\n')
    command_index = input('Введите номер команды: ')
    if input_proof(inpt=command_index, type_proof='int', left_limit=0, right_limit=7):
        command_index = int(command_index)
        return command_index
    else:
        return create_menu()


def init_db() -> None:
    """
    Инициализирует файл как базу данных
    Все, что там было, очищается
    """
    open(current_file, 'bw+').close()


def select_file(file_path: str) -> None:
    """
    Выбирает/создает файл
    :param file_path: путь файла
    """
    global current_file
    try:
        open(file_path, 'ba+').close()
        current_file = file_path
    except FileNotFoundError:
        print('Файл не найден и его нельзя создать')


def record_split(rec: bytes) -> list:
    """
    Преобразует запись в байты
    :param rec: запись в байтах
    :return: запись в массиве
    """
    rec = rec.strip(b'\n')
    record_splited = list(struct.unpack(fields_types, rec))
    return record_splited


def print_db() -> None:
    """
    Выводит содержание базы данных
    """
    with open(current_file, 'br') as file:
        for name in fields_names:
            print('{:^25}'.format(name), end=' ')
        print()
        for line in file:
            record = record_split(line)
            for element in record:
                if float_proof(element):
                    print('{:^25.4g}'.format(element), end=' ')
                else:
                    element = element.replace(b'\x00', b'').decode()
                    print('{:^25}'.format(element), end=' ')
            print()


def record_check(line: bytes) -> bool:
    """
    Проверяет запись на правильность
    :param line: запись
    :return: правильная ли запись
    """
    try:
        line = line.strip(b'\n')
        struct.unpack(fields_types, line)
        return True
    except struct.error:
        return False


def delete_record(index: int) -> None:
    """
    Удаляет запись по индексу
    :param index: индекс
    """
    total = 0
    with open(current_file, 'br+') as file:
        for line in file:
            total += 1
    if total <= index:
        return
    with open(current_file, 'rb+') as file:
        for _ in range(index):
            b = file.read(153)
            file.seek(file.tell() - 153)
            file.write(b)
        threshhold = (total - 1) * 153
        while file.tell() != threshhold:
            file.seek(file.tell() + 153)
            read_bytes = file.read(153)
            file.seek(file.tell() - 2 * 153)
            file.write(read_bytes)
        file.truncate(threshhold)


def check_curr_file() -> bool:
    """
    Проверяет файл на принадлежность к базам данных
    :return: является ли файл базой данных
    """
    try:
        with open(current_file, 'br') as file:
            for line in file:
                if not record_check(line):
                    return False
    except FileNotFoundError:
        return False
    return True


def can_record(row: list[str]) -> bool:
    """
    Проверяет на возможность записи
    :param row: запись
    :return: возможна ли запись
    """
    el1 = input_proof(inpt=row[0], type_proof='int', left_limit=0, right_limit=2**63)
    el2 = len(row[1]) <= 64
    el3 = len(row[2]) <= 64
    el4 = input_proof(inpt=row[3], type_proof='float', left_limit=0, right_limit=2**52)
    el5 = input_proof(inpt=row[4], type_proof='float', left_limit=0, right_limit=2**52)
    return all((el1, el2, el3, el4, el5))


def write_record(row: list) -> None:
    """
    Делает запись
    :param row: запись
    """
    row[0] = int(row[0])
    row[1] = row[1].encode()
    row[2] = row[2].encode()
    row[3] = float(row[3])
    row[4] = float(row[4])
    with open(current_file, 'ba') as file:
        file.write(struct.pack(fields_types, *row))
        file.write(b'\n')


def find_packet(packet: int) -> None:
    """
    Находит записи с нужным пакетом
    :param packet: номер пакета
    """
    with open(current_file, 'br') as file:
        for name in fields_names:
            print('{:^25}'.format(name), end=' ')
        print()
        for line in file:
            record = record_split(line)
            if int(record[0]) == packet:
                for element in record:
                    if float_proof(element):
                        print('{:^25.4g}'.format(element), end=' ')
                    else:
                        element = element.replace(b'\x00', b'').decode()
                        print('{:^25}'.format(element), end=' ')
                print()


def find_stock(stock: float, sector: str) -> None:
    """
    Находит акции больше значения, чей сектор равен данному
    :param stock: акция
    :param sector: сектор
    """
    with open(current_file, 'br') as file:
        for name in fields_names:
            print('{:^25}'.format(name), end=' ')
        print()
        for line in file:
            record = record_split(line)
            elem_sector = record[2].replace(b'\x00', b'').decode()
            if float(record[3]) >= stock and elem_sector == sector:
                for element in record:
                    if float_proof(element):
                        print('{:^25.4g}'.format(element), end=' ')
                    else:
                        element = element.replace(b'\x00', b'').decode()
                        print('{:^25}'.format(element), end=' ')
                print()


# Глобальные параметры
current_file = ''
fields_names = ['Индекс пакета', 'Название', 'Сектор', 'Курс акций', 'Курс год назад']
fields_types = 'q64s64sdd'


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
            init_db()
        else:
            print('Файл не выбран или недоступен')
    elif command == 3:
        if check_curr_file():
            print_db()
        else:
            print('Файл не выбран, недоступен или не является базой данных')
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
            record = [input() for _ in range(len_record)]
            if len_record == 5 and can_record(record):
                write_record(record)
            else:
                print('Запись нельзя записать')
        else:
            print('Файл не выбран или не является базой данных')
    elif command == 5:
        ind = input('Введите индекс для удаления (нумерация с 0): ')
        if input_proof(inpt=ind, left_limit=0, type_proof='int'):
            delete_record(int(ind))
        else:
            print('Индекс не подходящий')
    elif command == 6:
        # Поиск записей по номеру пакета
        if check_curr_file():
            element_to_find = input('Введите значение для поиска по номеру пакета: ')
            if int_proof(element_to_find) and int(element_to_find) >= 0:
                find_packet(int(element_to_find))
            else:
                print('Номер пакета неправильный')
        else:
            print('Файл не выбран или не является базой данных')
    elif command == 7:
        # Поиск записей с курсом акций больше значения и данным сектором
        if check_curr_file():
            el1 = input('Введите значение для поиска по курсам акций, больше заданного: ')
            if float_proof(el1):
                el2 = input('Введите значение для поиска по сектору: ')
                find_stock(float(el1), el2)
            else:
                print('Курс акций неверен')
        else:
            print('Файл не выбран или не является базой данных')
