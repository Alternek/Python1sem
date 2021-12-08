"""
Текстовый редактор
операции + и -
Найти предложение, содержащее слово с максимальным количеством согласных букв
ИУ7-16Б
Яремчук Иван
"""


from ivanpy.foolproof import input_proof


def create_menu() -> int:
    print('0. Выйти из программы',
          '1. Выровнять текст по левому краю',
          '2. Выровнять текст по правому краю',
          '3. Выровнять текст по ширине',
          '4. Удаление всех вхождений заданного слова',
          '5. Замена одного слова другим во всём тексте',
          '6. Вычисление арифметических выражений внутри текста (+ и -)',
          '7. Найти предложение, содержащее слово с максимальным количеством согласных букв')
    command_index = input('Введите номер комманды: ')
    if input_proof(inpt=command_index, type_proof='int', left_limit=0, right_limit=7):
        command_index = int(command_index)
        return command_index
    else:
        return create_menu()


def max_len_line(text: list[str]) -> int:
    mx = 0
    for line in text:
        mx = max(mx, len(line))
    return mx


def clean_string(text: list[str]) -> list[str]:
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
    text = clean_string(text)
    mx = max_len_line(text)
    text = list(map(lambda x: x.ljust(mx, ' '), text))
    return text


def right_align(text: list[str]) -> list[str]:
    text = clean_string(text)
    mx = max_len_line(text)
    text = list(map(lambda x: x.rjust(mx, ' '), text))
    return text


def justified_align(text: list[str]) -> list[str]:
    text = clean_string(text)
    mx = max_len_line(text)
    for line in range(len(text)):
        spc_cnt = text[line].count(' ')
        delta = mx - len(text[line])
        text[line] = text[line].replace(' ', ' '*(delta // spc_cnt + 1))
        text[line] = text[line].replace(' '*(delta // spc_cnt + 1), ' '*(delta // spc_cnt + 2), delta % spc_cnt)
    return text


def delete_word(text: list[str], word: str) -> list[str]:
    for line in range(len(text)):
        text[line] = text[line].replace(' ' + word, '')
        text[line] = text[line].replace(word, '')
        text[line] = text[line].replace(' ' + word.capitalize(), '')
        text[line] = text[line].replace(word.capitalize(), '')
    return text


def replace_word(text: list[str], word_original: str, word_final: str) -> list[str]:
    for line in range(len(text)):
        text[line] = text[line].replace(word_original, word_final)
    return text


def math_result(calc: str) -> int:
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
            text[line] = text[line].replace(for_replace, final_str)
    return text





text_original = """Но и это не    показалось Алисе 2 - 0 особенно странным. (Вспоминая об этом
позже, она      подумала, что ей следовало       бы удивиться, однако
   в тот миг все казалось ей
вполне естественным; 1 - 2 + 22 33 + 1.) Когда Кролик вдруг вынул часы из жилетного кармана и,
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

for i in math_plus_minus(text_original):
    print(i)
