# Напишите программу, которая будет преобразовывать десятичное число в двоичное.

# Пример:
# - 45 -> 101101
# - 3 -> 11
# - 2 -> 10

number = int(input("Введите десятичное число: "))
number_bin = ''
 
while number > 0:
 temp = str(number % 2)
 number_bin = temp + number_bin
 number = int(number / 2)
 
print (number_bin)