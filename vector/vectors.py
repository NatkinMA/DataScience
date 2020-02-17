'''
Домашнее задание N8
Создать класс для представления трехмерных векторов (обычных евклидовых).
С помощью специальных методов: "__add__", "__mul__", "__abs__", "__bool__", "__str__"
- определить сложение векторов, умножение вектора на число, длинна вектора, булево значение
(True - если длинна > 0) и строковое представление объекта.
'''

from vector import Vector


if __name__ == '__main__':
    my_vector = Vector(3, 2, 1)
    print(my_vector)
    print(my_vector + my_vector)
    print(my_vector * 5)
    print(7 * my_vector)
    print(abs(my_vector))
    print(bool(my_vector))