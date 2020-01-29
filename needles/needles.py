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

На счет задачи поиска иголок:
- вызов функции get_time_for_find_needles_in_stacks() можно поместить в цикл.
Например:
STACK_LENGTH = [1000, 10000, 100000, 1000000]
NEEDLES_LENGTH = 1000
...
for n in STACK_LENGTH:
  get_time_for_find_needles_in_stacks(n, NEEDLES_LENGTH)
- то же самое с вызовом функции  time_for_find_needles_in_stack, можно сформировать
список содержащий list, tuple и dict. И в цикле пройтись по этому списку и вызвать функцию.
- можно использовать needles.append(random.choice(stack_list)), вместо:
k = random.randint(0, (stack_size - 1))
needles.append(stack_list[k])
- или более просто сформировать набор иголок:
needles = [random.choice(stack_list) for _ in range(needles_length//2)]
needles.extend([random.uniform(1, 2) for _ in range(needles_length//2)])
- если в цикле не используется переменная цикла, ее лучше заменить на нижний подчкерк
например, [random.random() for _ in range(stack_size)]
- для поиска иголок в стоге достаточно было обойти в цикле все иголки и выполнить выражение needle in stack.
например,
for n in needles:
  if n in stask:
    pass
'''

import random
import timeit
import sys


def time_for_find_needles_in_stack(stack, needles):
    time_start = timeit.default_timer()
    i = 0
    for needle in needles:
        if needle in stack:
            pass
    time_end = timeit.default_timer() - time_start
    return sys.getsizeof(stack), time_end


def get_time_for_find_needles_in_stacks(stack_size, needles_size):
    stacks = []
    stack_list = [random.random() for i in range(stack_size)]
    stacks.append(stack_list)
    stack_tuple = tuple(stack_list)
    stacks.append(stack_tuple)
    stack_dict = dict(zip(stack_list, [1]*len(stack_list)))
    stacks.append(stack_dict)
    needles = [random.choice(stack_list) for _ in range(needles_size // 2)]
    needles.extend([random.uniform(1, 2) for _ in range(needles_size // 2)])
    for current_stack in stacks:
        print(time_for_find_needles_in_stack(current_stack, needles))


if __name__ == '__main__':
    STACK_LENGTH = [1000, 10000, 100000, 1000000]
    NEEDLES_LENGTH = 1000
    for n in STACK_LENGTH:
        get_time_for_find_needles_in_stacks(n, NEEDLES_LENGTH)
