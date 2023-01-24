# 46. Найти произведение пар чисел списка(парой считаем первый и последний, второй предпоследний и тд)

import random

num = [random.randint(1, 10) for i in range(10)]
print(num)

product = [num[i] * num[-i - 1] for i in range(len(num) // 2 + len(num) % 2)]
print(product)
