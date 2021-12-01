def print_matrix(matrix: list[list], type_el='float'):
    """
    Выводит матрицу в поток вывода
    :param matrix: list[list]: выводит матрицу
    :param type_el: str: тип элементов в матрице
    :return:
    """
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            if type_el != 'char':
                print('{:^7.3g}'.format(matrix[i][j]), end=' ')
            else:
                print('{:^7}'.format(matrix[i][j]), end=' ')
        print()
