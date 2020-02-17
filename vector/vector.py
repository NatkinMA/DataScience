'''
Домашнее задание N8
Создать класс для представления трехмерных векторов (обычных евклидовых).
С помощью специальных методов: "__add__", "__mul__", "__abs__", "__bool__", "__str__"
- определить сложение векторов, умножение вектора на число, длинна вектора, булево значение
(True - если длинна > 0) и строковое представление объекта.
'''

import math

class Vector:

    def __init__(self, x: float, y: float, z: float):
        self._x = x
        self._y = y
        self._z = z

    def __add__(self, other):
        if isinstance(other, Vector):
            return Vector(self._x + other.x, self._y + other.y, self._z + other.z)
        else:
            return None

    def __mul__(self, other):
        return Vector(other * self._x, other * self._y, other * self._z)

    def __rmul__(self, other):
        return self.__mul__(other)

    def __abs__(self):
        return math.sqrt(self._x**2 + self._y**2 + self._z**2)

    def __bool__(self):
        return abs(self) > 0

    def __str__(self):
        return '{' + str(self._x) + ', ' + str(self._y) + ', ' + str(self._z) + '}'

    @property
    def x(self):
        return self._x

    @property
    def y(self):
        return self._y

    @property
    def z(self):
        return self._z