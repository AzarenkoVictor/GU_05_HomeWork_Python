# 40. Реализуйте RLE алгоритм: реализуйте модуль сжатия и восстановления данных.
# Модуль сжатия:
# Для чисел:
# Входные данные:
# 111112222334445
# Выходные данные:
# 5142233415
# Также должно работать и для букв:
# Входные данные:
# AAAAAAFDDCCCCCCCAEEEEEEEEEEEEEEEEE
# Выходные данные:
# 6A1F2D7C1A17E
# (5 - количество единиц, далее сама единица, 4 - количество двоек, далее сама двойка и т.д)
# Модуль восстановления работет в обратную сторону - из строки выходных данных, получить строку входных данных.

data = "AAAAAAFDDCCCCCCCAEEEEEEEEEEEEEEEEE"
data2 = "6A1F2D7C1A17E"


def coding(data):
    result = ""
    count = 0
    prev_sym = data[0]
    for sym in data:
        if sym != prev_sym:
            result += f'{count}{prev_sym}'
            prev_sym = sym
            count = 1
        else:
            count += 1
    else:
        result += f'{count}{prev_sym}'
    return result


def decoding(data):
    result = ""
    count = 0
    for sym in data:
        if sym.isdigit():
            count = int(sym)
        else:
            result += count * sym
    return result


print(coding(data))
print(decoding(data2))
