from pprint import pprint


def get_words():
    file_g_w = open('for_mod_7_2.txt', 'r')
    try:
        return file_g_w.read()
    finally:
        file_g_w.close()


def custom_write(file_name, *words, strings=None):
    strings_positions = {}
    if strings is None:
        strings = [*words]
    for str_ in strings:
        if str_ in get_words():
            print(f'Слово или идентичная строка: <{str_}> уже есть в файле, попробуйте записать иначе')
        else:
            file = open(file_name, 'a')
            byte_num = file.tell()
            file.write(str_)
            file.write('\n')
            file.close()
            file = open(file_name, 'r')
            for i, line in enumerate(file):
                a = (i + 1)
            str_num = a
            strings_positions.update({(str_num, byte_num): str_})
            file.close()

    print(strings_positions)


custom_write('for_mod_7_2.txt', 'board', '12 packs', 'Привет со строки три!', 'а это уже четвёртая строка')
