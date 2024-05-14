"""
Добавьте в пакет, созданный на семинаре шахматный модуль.
 Внутри него напишите код, решающий задачу о 8 ферзях.
   Известно, что на доске 8×8 можно расставить 8 ферзей так, чтобы они не били друг друга.
     Вам дана расстановка 8 ферзей на доске, определите, есть ли среди них пара бьющих друг друга.
       Программа получает на вход восемь пар чисел, каждое число от 1 до 8 - координаты 8 ферзей.
         Если ферзи не бьют друг друга верните истину, а если бьют - ложь.
"""

__all__ = ['queens_shess']

def queens_shess(queens):
    for i in range(8):
        for j in range(i + 1, 8):
            # Проверяем, находятся ли два ферзя на одной и той же горизонтали, вертикали или диагонали
            if queens[i][0] == queens[j][0] or \
               queens[i][1] == queens[j][1] or \
               abs(queens[i][0] - queens[j][0]) == abs(queens[i][1] - queens[j][1]):
                return False
    return True

if __name__ == '__main__':
  queens = [[1, 7], [2, 5], [3, 3], [4, 1], [5, 6], [6, 8], [7, 2], [8, 4]]
  # [[1, 4], [3, 5], [8, 2], [5, 1], [7, 8], [6, 6], [4, 3], [2, 7]]
  # [[8, 8], [1, 5], [6, 1], [4, 6], [2, 7], [5, 3], [7, 4], [3, 2]]
  # [[5, 3], [3, 2], [8, 4], [2, 7], [4, 6], [6, 1], [1, 5], [7, 8]]
  print(queens_shess(queens)) 
  