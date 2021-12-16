def write_words(words: str) -> None:
    with open(current_file, 'a+') as file:
        file.write(' ' + words)


def read_words() -> None:
    with open(current_file, 'r') as file:
        for line in file:
            for word in line.split():
                print_word = True
                for symbol in word:
                    if symbol in 'бвгджзйклмнпрстфхцчшщБВГДЖЗЙКЛМНПРСТФХЦЧШЩ':
                        print_word = False
                if print_word:
                    print(word, end=' ')
    print()


current_file = '1.txt'
while True:
    print('0 - выход\n'
          '1 - запись слов\n'
          '2 - вывод слов без согласных')
    command = int(input('Введите команду: '))
    if command == 0:
        exit()
    elif command == 1:
        write_words(input('Введите слова через пробел: '))
    elif command == 2:
        read_words()
