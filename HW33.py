# Задайте последовательность чисел.
# Напишите программу, которая выведет список неповторяющихся элементов исходной последовательности.

import random

list = [(random.randint(1, 9)) for i in range(10)]
print(list)

def unique(list):
    unique_list = []
    for i in range(len(list)):
        if list[i] not in unique_list:
            unique_list.append(list[i])
    return unique_list

print(unique(list))
