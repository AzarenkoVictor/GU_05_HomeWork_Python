# Напишите программу, которая принимает на вход
# координаты двух точек и находит расстояние между ними в 2D пространстве.
# Пример:
# - A (3,6); B (2,1) -> 5,09
# - A (7,-5); B (1,-1) -> 7,21

import math
firstNumX = int(input("Введите  X первой точки "))
firstNumY = int(input("Введите  Y первой точки "))
secondNumX = int(input("Введите  X второй точки "))
secondNumY = int(input("Введите  Y второй точки "))
print("Расстояние в 2D пространстве равно : ", math.sqrt((firstNumX-secondNumX) * (firstNumX-secondNumX) +
      (firstNumY-secondNumY) * (firstNumY-secondNumY)))
