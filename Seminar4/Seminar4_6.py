"""Функция получает на вход список чисел и два индекса. 
Вернуть сумму чисел между переданными индексами. 
Если индекс выходит за пределы списка, сумма считается 
до конца и/или начала списка."""

def sum_range(numbers: list, x1: int, x2: int) ->int:
    """Возвращает сумму между индексами, включая их."""
    if x1 > x2:
        x1, x2 = x2, x1
    if x1 < 0:
        x1 = 0
    if x2 >= len(numbers):
        x2 = len(numbers) - 1
    return sum(numbers[x1:x2+1])


if __name__ == '__main__':
    numbers = [4, 5, 45, 78, 478, 145]
    x1 = 1
    x2 = 4
    print(sum_range(numbers, x1, x2))
    