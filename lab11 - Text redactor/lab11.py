"""
Текстовый редактор
операции + и -
Найти предложение, содержащее слово с максимальным количеством согласных букв
ИУ7-16Б
Яремчук Иван
"""


from ivanpy.foolproof import input_proof


def create_menu() -> int:
    """
    Создает бесконечное меню и ждет корректного номера команды
    :return: номер команды
    """
    print('0. Выйти из программы\n'
          '1. Выровнять текст по левому краю\n'
          '2. Выровнять текст по правому краю\n'
          '3. Выровнять текст по ширине\n'
          '4. Удаление всех вхождений заданного слова\n'
          '5. Замена одного слова другим во всём тексте\n'
          '6. Вычисление арифметических выражений внутри текста (+ и -)\n'
          '7. Найти предложение, содержащее слово с максимальным количеством согласных букв\n')
    command_index = input('Введите номер команды: ')
    if input_proof(inpt=command_index, type_proof='int', left_limit=0, right_limit=7):
        command_index = int(command_index)
        return command_index
    else:
        return create_menu()


def max_len_line(text: list[str]) -> int:
    """
    Находит максимальную длину строки
    :param text: текст
    :return: максимальную длину строки
    """
    mx = 0
    for line in text:
        mx = max(mx, len(line))
    return mx


def clean_string(text: list[str]) -> list[str]:
    """
    Удаляет пустые строки и лишние пробелы
    :param text: текст
    :return: "чистый" текст
    """
    dlt = []
    for line in range(len(text)):
        if text[line]:
            text[line] = ' '.join(text[line].split())
        else:
            dlt.append(line)
    dlt.reverse()
    for ind in dlt:
        text.pop(ind)
    return text


def left_align(text: list[str]) -> list[str]:
    """
    Выравнивает по левому краю
    :param text: текст
    :return: выравненный текст
    """
    text = clean_string(text)
    mx = max_len_line(text)
    text = list(map(lambda x: x.ljust(mx, ' '), text))
    return text


def right_align(text: list[str]) -> list[str]:
    """
    Выравнивает по правому краю
    :param text: текст
    :return: выравненный текст
    """
    text = clean_string(text)
    mx = max_len_line(text)
    text = list(map(lambda x: x.rjust(mx, ' '), text))
    return text


def justified_align(text: list[str]) -> list[str]:
    """
    Выравнивает по ширине
    :param text: текст
    :return: выравненный текст
    """
    text = clean_string(text)
    mx = max_len_line(text)
    for line in range(len(text)):
        spc_cnt = text[line].count(' ')
        delta = mx - len(text[line])
        text[line] = text[line].replace(' ', ' '*(delta // spc_cnt + 1))
        text[line] = text[line].replace(' '*(delta // spc_cnt + 1), ' '*(delta // spc_cnt + 2), delta % spc_cnt)
    return text


def delete_word(text: list[str], word: str) -> list[str]:
    """
    Удаляет слово
    :param text: текст
    :param word: слово для удаления
    :return: итоговый текст
    """
    for line in range(len(text)):
        text[line] = ' ' + text[line]
        for repl_s in ' .,!;:':
            text[line] = text[line].replace(' ' + word + repl_s, repl_s)
        text[line] = text[line][1:]
    return text


def replace_word(text: list[str], word_orig: str, word_final: str) -> list[str]:
    """
    Заменяет слово на другое слово
    :param text: текст
    :param word_orig: слово для замены
    :param word_final: слово на замену
    :return: итоговый текст
    """
    for line in range(len(text)):
        text[line] = ' ' + text[line]
        for repl_s in ' .,!;:':
            text[line] = text[line].replace(' ' + word_orig + repl_s, ' ' + word_final + repl_s)
        text[line] = text[line][1:]
    return text


def math_result(calc: str) -> int:
    """
    Считает результат мат выражения
    :param calc: мат выражение
    :return: результат
    """
    calc += '+'
    result = 0
    number = 0
    number_cont = False
    sign = 1
    for char in calc:
        if char == '+':
            if number_cont:
                result += sign * number
                number_cont = False
                number = 0
                sign = 1
        elif char == '-':
            if number_cont:
                result += sign * number
                number_cont = False
                number = 0
                sign = 1
            sign *= -1
        elif char in '0123456789':
            number_cont = True
            number = number * 10 + int(char)
    return result


def math_plus_minus(text: list[str]) -> list[str]:
    """
    Заменяет мат выражения на их результаты
    :param text: текст
    :return: итоговый текст
    """
    str_to_replace = []
    str_for_replace = []
    str_t_r = ''
    str_f_r = ''
    num_goes = False
    space_back = False
    for line in range(len(text)):
        for char in text[line]:
            if char in '+-':
                num_goes = False
                space_back = False
                str_t_r += char
                str_f_r += char
            elif char in '0123456789':
                if num_goes and space_back:
                    if str_t_r and str_t_r.lstrip('-') and str_t_r.lstrip('+'):
                        str_to_replace.append(str_t_r)
                        str_for_replace.append(str_f_r)
                    str_t_r = char
                    str_f_r = char
                else:
                    str_t_r += char
                    str_f_r += char
                num_goes = True
                space_back = False
            elif char == ' ':
                space_back = True
                str_f_r += char
            else:
                if str_t_r and str_t_r.lstrip('-') and str_t_r.lstrip('+'):
                    str_to_replace.append(str_t_r)
                    str_for_replace.append(str_f_r)
                str_t_r = ''
                str_f_r = ''
                num_goes = False
                space_back = False
    if str_t_r and str_t_r.lstrip('-') and str_t_r.lstrip('+'):
        str_to_replace.append(str_t_r)
    for for_replace, to_replace in zip(str_for_replace, str_to_replace):
        for_replace = for_replace.strip(' ')
        final_str = str(math_result(to_replace))
        for line in range(len(text)):
            text[line] = text[line].replace(for_replace, final_str, 1)
    return text


def find_word(text: list[str]) -> str:
    """
    Находит слово с наибольшим количество согласных букв
    :param text: текст
    :return: найденное слово
    """
    mx = 0
    word_ans = ''
    for line in text:
        for word in line.split():
            k = 0
            for symbol in word:
                if symbol in 'бвгджзйклмнпрстфхцчшщБВГДЖЗЙКЛМНПРСТФХЦЧШЩ':
                    k += 1
            if k > mx:
                word_ans = word
                mx = k
    return word_ans


def find_sentence(text: list[str]) -> str:
    """
    Находит предложение со словом, в котором наибольшее количество согласных букв
    :param text: текст
    :return: предложение
    """
    word = find_word(text)
    text = ' '.join(text)
    word_index = text.find(word)
    sentence = ''
    for ind in range(word_index - 1, -1, -1):
        if text[ind] in ').':
            break
        sentence = text[ind] + sentence
    for ind in range(word_index, len(text)):
        sentence += text[ind]
        if text[ind] in '.)':
            break
    return sentence.strip()


def clear_text(text: list[str]) -> list[str]:
    """
    Очищает и преобразует в массив текст
    :param text: текст
    :return: массив "чистых" слов
    """
    for line in range(len(text)):
        for del_type in '+-.,&!?1234567890():;':
            text[line] = text[line].replace(del_type, '')
    cl_text = []
    for line in text:
        for word in line.split():
            cl_text.append(word)
    return cl_text


def print_text(text: list[str]) -> None:
    """
    Выводит текст
    :param text: текст
    :return:
    """
    for line in text:
        print(line)


# Изначальный текст
text_original = """Но и это не    показалось Алисе 2 - 0 особенно странным. (Вспоминая об этом
позже, она      подумала, что ей следовало       бы удивиться, однако
   в тот миг все казалось ей
вполне естественным; 1 - 2 + 22 33 + 1) Когда Кролик ввввввдруг вынул часы из жилетного кармана и,
взглянув на них, помчался дальше, Алиса вскочила на ноги. Ее тут осенило: ведь
никогда раньше она не видела кролика с часами, да еще с
жилетным карманом в придачу! Сгорая от любопытства, она побежала
за ним по полю и только-только успела заметить, что он юркнул в нору под изгородью. В
тот же миг Алиса юркнула   (примечание: 1+31 + 5 - 2-1)  за ним следом, не думая  о том, как же она
будет выбираться обратно. Нора сначала шла прямо, ровная, как туннель, а потом
вдруг круто обрывалась вниз. Не успела Алиса33 32 32 - 1 и глазом моргнуть, как она
начала падать, словно в глубокий колодец.

Короткая строка,
Строка чуть длиннее,
Строка еще чуть длиннее,


Строка с числами: ----2+25, 2-2, 25 +3+4 +5, 2-23, 2-+2, asf131kna, gi2 + 3 -4fgaig1ga+akfh1+2,""".split('\n')

# Основной цикл
while True:
    command = create_menu()
    print()
    if command == 0:
        # Выйти из программы
        exit()
    elif command == 1:
        # Выровнять текст по левому краю
        text_original = left_align(text_original)
    elif command == 2:
        # Выровнять текст по правому краю
        text_original = right_align(text_original)
    elif command == 3:
        # Выровнять текст по ширине
        text_original = justified_align(text_original)
    elif command == 4:
        # Удаление всех вхождений заданного слова
        word_to_delete = input('Введите слово для удаления: ')
        if word_to_delete in clear_text(text_original.copy()):
            text_original = delete_word(text_original, word_to_delete)
        else:
            print('Такого слова нет')
    elif command == 5:
        # Замена одного слова другим во всём тексте
        word_original = input('Введите слово для замены: ')
        word_replace = input('Введите слово замену: ')
        if word_original in clear_text(text_original.copy()):
            text_original = replace_word(text_original, word_original, word_replace)
        else:
            print('Такого слова нет')
    elif command == 6:
        # Вычисление арифметических выражений внутри текста (+ и -)
        text_original = math_plus_minus(text_original)
    else:
        # Найти предложение, содержащее слово с максимальным количеством согласных букв
        print('Найденное предложение: ' + find_sentence(text_original))
    print()
    text_original = clean_string(text_original)
    print_text(text_original)
