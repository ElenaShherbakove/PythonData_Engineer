"""Пользователь вводит строку из четырёх 
или более целых чисел, разделённых символом “/”. 

Сформируйте словарь, где:
второе и третье число являются ключами.
первое число является значением для первого ключа.
четвертое и все возможные последующие числа 
       хранятся в кортеже как значения второго ключа."""

a, b, c, *d = input('Введите четыре числа вида, например 4/8/8/8: ').split('/')
dictionary = {c: tuple(d), b: a}
print(dictionary)