# 38. Напишите программу, удаляющую из текста все слова, содержащие ""абв"".(Задание из семинара)

text = "цуацуаава ааывапаа, аабв ББББГГГГВВВ. Абв"
text_list = text.split()
result = list(filter(lambda x: not "абв" in x.lower() ,text_list))
print(result)
