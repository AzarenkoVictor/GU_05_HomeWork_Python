# Напишите программу, которая найдёт произведение пар чисел списка.
# Парой считаем первый и последний элемент, второй и предпоследний и т.д.

# Пример:
# - [2, 3, 4, 5, 6] => [12, 15, 16];
# - [2, 3, 5, 6] => [12, 15]

import random
n = int(input("Введите длинну списка чисел "))
list = [random.randint(0, 9) for i in range(n)]
list2 = []
print(list)
for i in range(0, (len(list)+1)//2):
    list2.append(list[i] * list[-i-1])
print(list2)