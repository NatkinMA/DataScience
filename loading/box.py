'''
 Коробка, атрибуты:
    высота,
    ширина,
    длина,
    масса.
'''


class Box:
    __height = float()
    __width = float()
    __length = float()
    __weight = float()

    def __init__(self, height, width, length, weight):
        self.__height = height
        self.__width = width
        self.__length = length
        self.__weight = weight

    def __repr__(self):
        return '\nBox size: ' + str(self.__height) \
               + 'x' + str(self.__width) \
               + 'x' + str(self.__length) \
               + ', weight: ' + str(self.__weight)

    def get_height(self):
        return self.__height

    def get_width(self):
        return self.__width

    def get_length(self):
        return self.__length

    def get_weight(self):
        return self.__weight

    def get_value(self):
        return self.__length * self.__width * self.__height

    def __str__(self):
        return '\nBox size: ' + str(self.__height) \
               + 'x' + str(self.__width) \
               + 'x' + str(self.__length) \
               + ', weight: ' + str(self.__weight)