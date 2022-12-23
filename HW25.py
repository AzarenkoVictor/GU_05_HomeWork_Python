# Задайте число. Составьте список чисел Фибоначчи, в том числе для отрицательных индексов.

# Пример:
# - для k = 8 список будет выглядеть так: [-21 ,13, -8, 5, −3, 2, −1, 1, 0, 1, 1, 2, 3, 5, 8, 13, 21]

k = int(input("Введите число k: "))


def fibonacci_minus(k):
    a, b = 0, 1
    for i in range(k+1):
        yield a
        a, b = b, a - b


def fibonacci(k):
    a, b = 1, 1
    for i in range(k):
        yield a
        a, b = b, a + b


number_minus = list(fibonacci_minus(k))
number_minus.reverse()
number = list(fibonacci(k))
number_final = []
number_final.append((number_minus)+(number))
print(number_final)
