

def custom_write(file_name, strings):
    strings_positions = {}
    file_name = 'test.txt'

    book = open(file_name, 'a', encoding='utf-8')
    for i, s in enumerate(strings):
        key = (i + 1, book.tell())
        strings_positions[key] = s
        book.write(s + '\n')
    book.close()

    return strings_positions


def text():
    info = [
        'Text for tell.',
        'Используйте кодировку utf-8.',
        'Because there are 2 languages!',
        'Спасибо!'
    ]

    result = custom_write('test.txt', info)
    for elem in result.items():
        print(elem)


text()
