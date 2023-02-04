
import random
import telebot
bot = telebot.TeleBot("") 

sweets = 221
win_user = ""  

@bot.message_handler(commands = ["start"])         
def start(message):
    global user
    bot.send_message(message.chat.id,'Привет. Играем в конфеты !')   
    bot.send_message(message.chat.id,f'Правила игры: \nКоличество конфет: {sweets}.\nМожно брать от 1 до 28 конфет') 
    
    user = random.randint(1, 2)
    
    if user == 1:
        bot.send_message(message.chat.id,f" Первым ходит Игрок")
    else:
        bot.send_message(message.chat.id,f" Первым ходит Терминатор")

    controller(message)


def controller(message):
    global sweets, user
    bot.send_message(message.chat.id,f"Остаток конфет: \n{sweets}")
    if sweets > 0:
        if not user % 2:
            bot.send_message(message.chat.id,f"Ход Терминатора")
            user += 1 
            bot_choise(message)                       
        else:
            bot.send_message(message.chat.id,f" Ход Игрока: ")
            user += 1
            bot.register_next_step_handler(message, user_choise)     
    else:
        if not user % 2: 
            bot.send_message(message.chat.id,f" Победил Игрок !")
        else:
            bot.send_message(message.chat.id,f" Победил Терминатор ")
        sweets = 221

def bot_choise(message):
    global sweets
    if  sweets <= 28:
        temp_sweets = sweets
        sweets -= temp_sweets
        bot.send_message(message.chat.id,f'Терминатор взял {temp_sweets} конфет')     
    else:
        temp_sweets = random.randint(1,28)
        sweets -= temp_sweets
        bot.send_message(message.chat.id,f'Терминатор взял {temp_sweets} конфет')
    

    controller(message)

def user_choise(message):
    global sweets 
    if True:
        try:
            temp_sweets = int(message.text)
            if 0 < temp_sweets < 29:
                sweets -= temp_sweets
                temp_sweets = int(message.text)
                sweets -= temp_sweets
                controller(message)
            else:
                bot.send_message(message.chat.id,f"Введите корректное количество конфет")
                a  = message.text
                bot.register_next_step_handler(message, user_choise)
        except:
            bot.send_message(message.chat.id,f"Вводи цифры !")
            a  = message.text
            bot.register_next_step_handler(message, user_choise)

bot.infinity_polling()