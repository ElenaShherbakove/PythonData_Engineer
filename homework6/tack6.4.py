"""
Напишите функцию в шахматный модуль.
 Используйте генератор случайных чисел для случайной расстановки ферзей в задаче выше.
 Проверяйте различный случайные варианты и выведите 4 успешных расстановки.
"""

import random
from task6_3 import queens_shess

__all__ = ['list_shess']

def list_shess(counts: int) -> list:
    list_correct = []
    while len(list_correct) < counts:
        queen_new = []
        for j in range(8):
            new_x = random.randint(1, 8)
            new_y = random.randint(1, 8)
            queen_new.append(list((new_x, new_y)))
        if queens_shess(queen_new) == True:
            list_correct.append(queen_new)
    return list_correct
