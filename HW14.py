# Задайте список из N элементов, заполненных числами из промежутка [-N, N].
# Найдите произведение элементов на указанных позициях. Позиции хранятся в файле file.txt
# в одной строке одно число.


import random
number_n = int(input("Введите число N "))
number_list = [random.randint(-number_n, number_n) for i in range(number_n)]
print(number_list)

file = open("file.txt", "r")
multiply = 1
for k in file:
    multiply *= number_list[int(k)]
print(multiply)
