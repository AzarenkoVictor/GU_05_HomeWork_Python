# Задайте список из вещественных чисел. Напишите программу,
# которая найдёт разницу между максимальным и минимальным значением дробной части элементов.

# Пример:
# - [1.1, 1.2, 3.1, 5, 10.01] => 0.19

import random
n = int(input("Введите длинну списка вещественных чисел "))
list = [round(random.uniform(1, 10), random.randint(1, 2)) for i in range(n)]
print(list)


def number_split(number):
    first_digit = (number * 100) % 100
    second_digit = (first_digit * 10) % 10
    two_digits = int((first_digit*10 + second_digit)//10)
    if two_digits > 0:
        return two_digits/100


max = 0
min = 10

for i in range(0, len(list)):
    if number_split(list[i]) > max:
        max = number_split(list[i])
    elif number_split(list[i]) < min:
        min = number_split(list[i])

print("Разница между максимальным и минимальным значением дробной части элементов равна ", round((max - min),2))
