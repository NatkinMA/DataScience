'''
Построчно считывать данные из файла (data.txt), который я вышлю в общую группу,
проводить через пайплайн обработки и записать в другой файл (output.txt).
Пайплайн обработки данных представляет собой 3 функции, каждая из которых
принимает строку на вход и возвращает измененную строку.
Что должны делать функции:
1) заменять точки и запятые на пробелы
2) заменять 2 пробела на 1
3) приводить весь текст в нижний регистр
'''


def replace_points(str_line):
    return str_line.replace('.', ' ')


def replace_commas(str_line):
    return str_line.replace(',', ' ')


def replace_double_space(str_line):
    return str_line.replace('  ', ' ')


def lower_case(str_line):
    return str_line.lower()


if __name__ == '__main__':
    try:
        input_file = open('data.txt', 'r')
        output_file = open('output.txt', 'w')

        for line in input_file.readlines():

            line = replace_points(line)
            line = replace_commas(line)
            line = replace_double_space(line)
            line = lower_case(line)
            output_file.write(line)

        input_file.close()
        output_file.close()
    except FileNotFoundError:
        print('FileNotFoundError: data.txt not found')
