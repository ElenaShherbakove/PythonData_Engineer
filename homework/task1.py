"""
Треугольник существует только тогда, когда сумма любых двух его сторон больше третьей.
 Дано a, b, c - стороны предполагаемого треугольника.
   Требуется сравнить длину каждого отрезка-стороны с суммой двух других.
     Если хотя бы в одном случае отрезок окажется больше суммы двух других, то треугольника с такими сторонами не существует.
       Отдельно сообщить является ли треугольник разносторонним, равнобедренным или равносторонним.
"""
a = int(input("введите a:\n"))
b = int(input("введите b:\n"))
c = int(input("введите c:\n"))

if (a or b or c) < 0:
    print("Стороны не могут быть отрицательной длины")
if a+b < c or b+c<a or c+a<b:
    print("Такого треугольника существовать не может")    
elif a == b == c:
    print("Треуголник равностороний")
elif a == b or b == c or a == c:
    print("Треугольник равнобедреннй")
else:
    print("Треугольник разносторонний")
    