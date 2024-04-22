"""Создайте пакет с всеми модулями, которые вы создали за время занятия. 
Добавьте в __init__ пакета имена модулей внутри дандер __all__. 
В модулях создайте дандер __all__ и укажите только те функции, которые могут верно работать за пределами модуля."""

from .ex2 import guess_number


__all__ = ['ex7', 'ex2']

22:02
from Seminars.Seminar6 import ex2
from Seminars.Seminar6 import guess_number