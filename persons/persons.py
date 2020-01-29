'''
Домашнее задание №4
В файле data.txt содержатся данные о пользователях. Формат хранения данных похож на таблицу,
в первой строке - названия полей, в последующих строках - непосредственно данные.
Нужно построчно считать данные из файла, провалидировать их, сформировать словарь person
и положить его в список persons.
Ключи для словаря person взять из названия полей (первая строка файла).
Каждая строка (кроме первой) содержит данные об одном человеке, которые разделены с помощью
любых комбинаций следующих символов: '\t', '-', ';'
Если данные не прошли валидацию, в словарь person по соответствующему ключу нужно положить
значение None.

Валидация данных:
- id - целое положительное число
- name - строка содержащая только буквы латинского алфавита
- age - целое положительное число
- phone - строка состоящая из цифр и знака '+', который может стоять только на 1-ом месте.
Максимальная длинна строки - 12 символов.
- email - строка состоящая из 4 частей: 1) не пустая строка только из букв и цифп, 2)
символ '@', 3) строка только из букв, 4) символ '.', 5) строка только из букв
- role - один из вариантов: 'admin', 'user', 'guest'
- status - один из вариантов: 'active', 'inactive'
'''

import re


def get_headers(str_line):
    return re.findall('([a-z]+)', str_line)


def get_person(lst_headers, str_line):
    dict_person = dict.fromkeys(lst_headers, None)
    lst_data = re.findall('[^\t\n;-]+', str_line)
    if re.fullmatch('\d+', lst_data[0]):
        dict_person[lst_headers[0]] = lst_data[0]
    if re.fullmatch('[A-Z][a-z]+', lst_data[1]):
        dict_person[lst_headers[1]] = lst_data[1]
    if re.fullmatch('\d{2}', lst_data[2]):
        dict_person[lst_headers[2]] = lst_data[2]
    if re.fullmatch('\+?\d{,11}', lst_data[3]):
        dict_person[lst_headers[3]] = lst_data[3]
    if re.fullmatch('[A-Z]?[a-z0-9]+@[A-Za-z]+\.?[A-Za-z]*', lst_data[4]):
        dict_person[lst_headers[4]] = lst_data[4]
    if re.fullmatch('admin|user|guest', lst_data[5]):
        dict_person[lst_headers[5]] = lst_data[5]
    if re.fullmatch('active|inactive', lst_data[6]):
        dict_person[lst_headers[6]] = lst_data[6]
    return dict_person


if __name__ == '__main__':
    try:
        input_file = open('data.txt', 'r')
        headers = get_headers(input_file.readline())
        persons = []
        for line in input_file.readlines():
            persons.append(get_person(headers, line))
        input_file.close()
        print(persons)
    except FileNotFoundError:
        print('FileNotFoundError: data.txt not found')
