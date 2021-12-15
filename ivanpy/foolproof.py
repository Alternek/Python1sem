from math import inf


def int_proof(s):
    """
    проверяет строку на принадлежность целым числам
    :param s: str: строка на проверку
    :return: bool: является ли строка целым числом
    """
    return s.lstrip('-').isdecimal()


def float_proof(s):
    """
    проверяет строку на принадлежность float
    :param s: str: строка на проверку
    :return: bool: является ли строка float
    """
    try:
        float(s)
        return True
    except TypeError or ValueError:
        return False


def input_proof(inpt: str, left_limit=-inf, right_limit=+inf, amount_of_numbers=1, type_proof='float'):
    """
    проверяет ввод на корректность
    :param inpt: str: строка на проверку
    :param left_limit: float: левая граница чисел
    :param right_limit: float: правая граница чисел
    :param amount_of_numbers: int: количество чисел (0 для любого количества)
    :param type_proof: str: тип проверки
    :return: bool: является ли ввод корректным
    """
    def proof(num: str):
        if type_proof == 'float':
            return float_proof(num)
        elif type_proof == 'char':
            return len(num) == 1
        else:
            return int_proof(num)

    inputs = inpt.split()
    if len(inputs) != amount_of_numbers and amount_of_numbers != 0:
        return False
    if False in list(map(proof, inputs)):
        return False
    if type_proof != 'char':
        inputs = list(map(float, inputs))
        if False in list(map(lambda x: left_limit <= x <= right_limit, inputs)):
            return False

    return True


def print_wrong():
    """
    Выводит сообщение о некорректных значениях и закрывает программу
    :return:
    """
    print('Вводите корректные значения!')
    exit()


def input_matrix(square=False, type_proof='float') -> list[list]:
    """
    Собирает матрицу из потока ввода
    :param square: bool: является ли матрица квадратной
    :param type_proof: str: какой тип данных будет в матрице
    :return: list[list]: матрица
    """
    if square:
        input_n = input('Введите ширину матрицы: ')
    else:
        input_n = input('Введите ширину и высоту матрицы через пробел: ')
    if input_proof(inpt=input_n, left_limit=1, type_proof='int', amount_of_numbers=0):
        if square:
            if input_proof(inpt=input_n, left_limit=1, type_proof='int', amount_of_numbers=1):
                n = int(input_n)
                m = n
            else:
                print_wrong()
        else:
            if input_proof(inpt=input_n, left_limit=1, type_proof='int', amount_of_numbers=2):
                input_n = input_n.split()
                n = int(input_n[0])
                m = int(input_n[1])
            else:
                print_wrong()
        print('Введите матрицу построчно: ')
        matrix = []
        for i in range(n):
            inpt = input()
            if input_proof(inpt=inpt, amount_of_numbers=m, type_proof=type_proof):
                if type_proof == 'int':
                    matrix.append([int(i) for i in inpt.split()])
                elif type_proof == 'float':
                    matrix.append([int(i) for i in inpt.split()])
                else:
                    matrix.append([i for i in inpt.split()])
            else:
                print_wrong()
        return matrix
    else:
        print_wrong()


def input_array(length=0, type_proof='float', left_limit=-inf, right_limit=+inf) -> list:
    """
    Собирает массив из потока ввода
    :param length: int: длина массива
    :param type_proof: str: тип проверки элементов
    :param left_limit: float: левая граница
    :param right_limit: float: правая граница
    :return: list: массив
    """
    inpt = input('Введите массив через пробел: ')
    if input_proof(inpt=inpt, amount_of_numbers=length, type_proof=type_proof):
        if type_proof == 'float':
            arr = [float(i) for i in inpt.split()]
        else:
            arr = [int(i) for i in inpt.split()]
        if min(list(map(lambda x: left_limit <= x <= right_limit, arr))):
            return arr
        else:
            print_wrong()
    else:
        print_wrong()
