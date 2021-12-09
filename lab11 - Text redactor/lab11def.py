# список строк, удалить предложения, содержащие самое длинное слово


def find_word(text: list[str]) -> str:
    mx = 0
    ans_word = ''
    for line in text:
        for word in line.split():
            word = word.strip('.,!()+-0123456789;:')
            if len(word) > mx:
                mx = len(word)
                ans_word = word
    return ans_word


def delete_sentences(text: list[str]) -> list[str]:
    word = find_word(text)
    text_linear = '\n '.join(text)
    while text_linear.find(word) + 1:
        word_index = text_linear.find(word)
        sentence = ''
        for ind in range(word_index - 1, -1, -1):
            if text_linear[ind] in ').!':
                break
            sentence = text_linear[ind] + sentence
        for ind in range(word_index, len(text_linear)):
            sentence += text_linear[ind]
            if text_linear[ind] in '.)!':
                break
        text_linear = text_linear.replace(sentence, '\n')
    text_clear = text_linear.split('\n')
    return text_clear


text_original = """Но и это не    показалось Алисе 2 - 0-0 - 0-0+0 о---0собенно странным. (Вспоминая об этом
позже, она      подумала, что ей следовало       бы удивиться, однако
   в тот миг все казалось ей
вполне естественным; 1 - 2 + 22 33 + 1) Когда Кролик  вынул часы из жилетного кармана и,
взглянув на них, помчался дальше, Алиса вскочила на ноги. Ее тут осенило: ведь
никогда      раньше она не видела кролика с часами, да еще с
жилетным карманом      в пр1и2д3а+ч4у! Сгорая от любопытства, она побежала
за ним по полю и только-только успела заметить, что он юркнул в нору под изгородью. В
тот же миг Алиса юркнула             за ним следом, не думая  о том, как же она
будет      выбираться обратно. Нора сначала шла прямо, ровная, как туннель,   а потом
вдруг круто обрывалась вниз. Не успела Алиса33 32 32 - 1 и глазом моргнуть, как она
начала падать, словно в глубокий колодец.

Строка.
Строкааааа.
Строкаааааааа.


Строка с выражениями: ----2+25, 2-2, 25 +3+4 +5, 2-23, 2-+2, asf131kna, gi2 + 3 -4fgaig1ga+akfh1+2,.""".split('\n')

print('Текст изначальный: \n')
for line in text_original:
    print(line)
text_original = delete_sentences(text_original)
print('Текст очищенный: \n')
for line in text_original:
    print(line)
