
# 1. Написать функцию num_translate(), переводящую числительные от 0 до 10 c английского на русский язык. Например:
# >>> >>> num_translate("one")
# "один"
# >>> num_translate("eight")
# "восемь"
# Если перевод сделать невозможно, вернуть None.
# Подумайте, как и где лучше хранить информацию, необходимую для перевода: какой тип данных выбрать, в теле функции или снаружи.

def num_translate():
    translate_book = {"one": "один", "two": "два", 'three': "три", "four": 'четыре', 'five': 'пять',
                      'six': 'шесть', 'seven': "семь", 'eight': "восемь", 'nine': "девять",
                      'ten': 'десять'

                     }

    for num in translate_book.keys():
        tempor_word = input("Перевод слова {}".format(num))
        word_res = translate_book.get(num)
        if tempor_word == word_res:
            print('Верно, перевод слова {} - {}'.format(num,word_res))

num_translate()