"""Добавьте в модуль с загадками функцию, которая хранит словарь списков. 
Ключ словаря - загадка, значение - список с отгадками. 
Функция в цикле вызывает загадывающую функцию, чтобы передать ей все свои загадки."""

"""def storage():
    puzzles = {
        'Зимой и летом одним цветом': ['ель', 'ёлка', 'сосна'],
        'Не лает, не кусает, в дом не пускает': ['замок'],
        'Сидит дед во сто шуб одет': ['лук', 'луковица'],
    }
    for key, value in puzzles.items():
        result = secrets(key, value)
        print(f'Угадал с {result} попытки' if result > 0 else 'Не угадал')

if __name__ == '__main__':
    storage()

21:36
def save(puzzle: str, count: int):
    _data.update({puzzle: count})


def show():
    res = (f'Загадку "{key}" разгадали с {value}-й попытки' if value > 0
           else f'Загадку "{key}" не разгадали'
           for key, value in _data.items())
    print('\n'.join(res))"""