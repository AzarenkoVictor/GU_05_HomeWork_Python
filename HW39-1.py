# 39(1). Создайте программу для игры с конфетами человек против человека.
# Реализовать игру игрока против игрока в терминале.
# Игроки ходят друг за другом, вписывая желаемое количество конфет.
# Первый ход определяется жеребьёвкой. В конце вывести игрока, который победил

# Условие задачи: На столе лежит 221 конфета.
# Играют два игрока делая ход друг после друга.
# Первый ход определяется жеребьёвкой. За один ход можно забрать не более чем 28 конфет.
# Все конфеты оппонента достаются сделавшему последний ход.

# В качестве дополнительного усложнения можно:
# a) Добавьте игру против бота ( где бот берет рандомное количество конфет от 0 до 28)
# b) Подумайте как наделить бота ""интеллектом""
# (есть алгоритм, позволяющий выяснить какое количесвто конфет необходимо брать, чтобы гарантированно победить,
# соответственно внедрить этот алгоритм боту )



# ------------------------Исходное Домашнее задание-------------------------------

# import random

# def input_number():
#     while True:
#         try:
#             temp_sweets = int(input("Введите количество конфет (от 1 до 28) "))
#             if 0 < temp_sweets < 29:
#                 return temp_sweets
#             else:
#                 print("Введи число от 1 до 28")
#         except:
#             print("Вводи цифры !")
# def who(user):
#     if not user % 2:
#         return print(f"\n Ходит {temp_user2} ")
#     else:
#         return print(f"\n Ходит {temp_user1} ")

# temp_user1 = input("Введите имя 1 игрока ")
# temp_user2 = input("Введите имя 2 игрока ")
# win_user = ""

# sweets = 221  # Магическое число !

# user = random.randint(1, 2)
# if user == 1:
#     print(f"\n Первым ходит {temp_user1}")
# else:
#     print(f"\n Первым ходит {temp_user2}")

# while sweets > 28:
#     temp_sweets = input_number()
#     sweets -= temp_sweets
#     user += 1
#     print(f"Остаток конфет: {sweets}")
#     if sweets > 28: 
#         who(user)
    
# else:
#     if not user % 2:
#         print(f"\n Победил {temp_user2} ")
#     else:
#         print(f"\n Победил {temp_user1} ")




# _-------------------- Усложнение а -----------------------------



import random

def input_number():
    while True:
        try:
            temp_sweets = int(input("Введите количество конфет (от 1 до 28) "))
            if 0 < temp_sweets < 29:
                return temp_sweets
            else:
                print("Введи число от 1 до 28")
        except:
            print("Вводи цифры !")
def who(user):
    if not user % 2:
        return print(f"\n Ходит {temp_user2} ")
    else:
        return print(f"\n Ходит {temp_user1} ")

temp_user1 = input("Введите имя 1 игрока ")
temp_user2 = 'Терминатор'
win_user = ""

sweets = 221  # Магическое число !

user = random.randint(1, 2)
if user == 1:
    print(f"\n Первым ходит {temp_user1}")
else:
    print(f"\n Первым ходит {temp_user2}")

def sweet_choise(user):
    if not user % 2:
        temp_sweets = random.randint(1,28)
        print(temp_sweets)
        return (temp_sweets)
    else: 
        temp_sweets = input_number()
        return (temp_sweets)

while sweets > 28:
    sweets -= sweet_choise(user)
    user += 1
    print(f"Остаток конфет: {sweets}")
    if sweets > 28: 
        who(user)
    
else:
    if not user % 2:
        print(f"\n Победил {temp_user2} ")
    else:
        print(f"\n Победил {temp_user1} ")