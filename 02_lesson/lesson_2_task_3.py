# 3)Площадь квадрата
import math


def square(side):
    s = side*side
    return s


side = float(input("Введите сторону квадрата: "))
s = square(side)
print(math.ceil(s))
