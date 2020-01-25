'''
Для каждого из следующих типов данных: list, tuple, dict,
нужно посчитать:
- время выполнения скрипта осуществляющего поиск "иголок"
в "стоге" (выражение: needle in stack).
Операцию нужно провести для каждой "иголки" из набора.
- размер "cтога" в байтах (import sys / sys.getsizeof(obj))

"стог" - это набор данных типа float формируемых с помощью
библиотеки random (import random / random.random())
набор "иголок" - состоит на 50% из случайных элементов
содержащихся в стоге и на 50% из элементов точно
не содеращихся в стоге

Вычисления провести для различных размеров стога: 100 000,
1 000 000, 10 000 000 элементов.

Замер времени выполнения провести с помощью библиотеки timeit.
import timeit
time_start = timeit.default_timer()
# ваш скрипт
time_end = timeit.default_timer() - time_start

При формировании "стога" для структуры dict, в качестве
значений можно использовать 1

Для упрощения расчетов давайте внесем небольшие изменения в задание:
1) Ограничить размер набора "иголок" 1 000 элементов.
2) расчеты производить для: 1 000, 10 000, 100 000, 1 000 000 элементов.
Расчета для 10 000 000 производить не нужно.
'''

import random
import timeit
import sys


def time_for_find_needles_in_stack(stack, needles):
    time_start = timeit.default_timer()
    i = 0
    for needle in needles:
        for element in stack:
            if needle == element:
                break
    time_end = timeit.default_timer() - time_start
    return sys.getsizeof(stack), time_end


def get_time_for_find_needles_in_stacks(stack_size, needles_size):
    stack_list = [random.random() for i in range(stack_size)]
    stack_tuple = tuple(stack_list)
    stack_dict = dict(zip(stack_list, [1]*len(stack_list)))
    needles = []
    for i in range(needles_size):
        if i <= 500:
            k = random.randint(0, len(stack_list))
            needles.append(stack_list[k])
        else:
            needles.append(random.uniform(1, 2))
    return time_for_find_needles_in_stack(stack_list, needles), \
           time_for_find_needles_in_stack(stack_tuple, needles), \
           time_for_find_needles_in_stack(stack_dict, needles)


if __name__ == '__main__':
    print(get_time_for_find_needles_in_stacks(1000, 1000))
    print(get_time_for_find_needles_in_stacks(10000, 1000))
    print(get_time_for_find_needles_in_stacks(100000, 1000))
    print(get_time_for_find_needles_in_stacks(1000000, 1000))
