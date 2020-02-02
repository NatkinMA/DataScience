'''
Вагон, атрибуты:
    высота,
    ширина,
    длина,
    список коробок,
    текущая масса (состоящая из массы всех коробок загруженных в вагон),
    максимальная масса груза которую можно поместить в вагон
'''

from box import Box


class Carriage:
    __height = float()
    __width = float()
    __length = float
    __boxes = []
    __maximum_weight = float()
    __current_weight = float()
    __filled_value = float()

    def __init__(self, height, width, length, maximum_weight):
        self.__height = height
        self.__width = width
        self.__length = length
        self.__maximum_weight = maximum_weight
        self.__current_weight = 0.0

    def __str__(self):
        return 'Carriage size: ' + str(self.__height) \
               + 'x' + str(self.__width) \
               + 'x' + str(self.__length) \
               + '. \nMaximum weight: ' + str(self.__maximum_weight) \
               + '. \nCurrent weight: ' + str(self.__current_weight) \
               + '. \nLoad boxes: ' + str(self.__boxes)

    def load(self, boxes):
        unload_boxes = []
        for box in boxes:
            if (box.get_height() < self.__height) and (box.get_width() < self.__width) and (
                    box.get_length() < self.__length) and (
                    (box.get_weight() + self.__current_weight) < self.__maximum_weight) and (
                    (box.get_value() + self.__filled_value) < self.get_value()):
                self.__boxes.append(box)
                self.__current_weight = self.__current_weight + box.get_weight()
                self.__filled_value = self.__filled_value + box.get_value()
            else:
                unload_boxes.append(box)
        return unload_boxes

    def get_value(self):
        return self.__height * self.__width * self.__length
