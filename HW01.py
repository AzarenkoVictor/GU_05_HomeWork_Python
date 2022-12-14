# Напишите программу, которая принимает на вход цифру, обозначающую день недели, 
# и проверяет, является ли этот день выходным.
# Пример:
# - 6 -> да
# - 7 -> да
# - 1 -> нет

weekNumber = int(input("Введите число - день недели: "))

if weekNumber == 6 or weekNumber == 7:
    print ("Выходной")
elif weekNumber > 0 and weekNumber < 6:
    print ("Будний день")
else:
    print ("Введено некорректное значение")

# РЕШЕНИЕ 2
# weekNumber = int(input("Введите число - день недели: "))
# if weekNumber == 1:
#     print ("Понедельник - будни")
# elif weekNumber == 2:
#     print ("Вторник - будни")
# elif weekNumber == 3:
#     print ("Среда - будни")
# elif weekNumber == 4:
#     print ("Четверг - будни")
# elif weekNumber == 5:
#     print ("Пятница - будни")
# elif weekNumber == 6:
#     print ("Суббота - выходной")
# elif weekNumber == 7:
#     print ("Воскресенье - выходной")
# else:
#     print ("Введите корректное число")
