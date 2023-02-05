
import telebot
from telebot import types 
bot = telebot.TeleBot("5915462287:AAF8eSL32rH18hGDTRH8H44O6kWpfSq1I04") 
import time

import modul

@bot.message_handler(commands = ["start"])         
def start(message):
    print(f'Бот запущен пользователем !')
    bot.send_message(message.chat.id,'Привет. Это бот-калькулятор !')   
    start(message)

def start(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    but1 = types.KeyboardButton("Rомплексные числа")   
    but2 = types.KeyboardButton("Действительные числа")
    markup.add(but1)   
    markup.add(but2) 
    bot.send_message(message.chat.id,"Выберите систему чисел", reply_markup = markup) 
    bot.register_next_step_handler(message, get_type)


def get_type(message):
    global type_num
    type_num = str(message.text)
    type_w(message)

def type_w(message):
    if type_num == "Rомплексные числа":
        bot.send_message(message.chat.id,'Выбран режим работы с комплексными числами !')
        bot.send_message(message.chat.id, "Введи 1е число ")    
        bot.register_next_step_handler(message, get_value_complex_a)
    else:
        bot.send_message(message.chat.id,'Выбран режим работы с действительными числами !')
        bot.send_message(message.chat.id,"Введи 1е число ")
        bot.register_next_step_handler(message, get_value_int_a)

def get_value_int_a(message):
    global a
    a = int(message.text)
    line_creator(message)
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)  
    but1 = types.KeyboardButton("+") 
    but2 = types.KeyboardButton("-")
    but3 = types.KeyboardButton("/")
    but4 = types.KeyboardButton("*")
    but5 = types.KeyboardButton("//") 
    but6 = types.KeyboardButton("%") 
    markup.add(but1)    
    markup.add(but2)  
    markup.add(but3)
    markup.add(but4)
    markup.add(but5)    
    markup.add(but6) 
    bot.send_message(message.chat.id,"Введите знак", reply_markup = markup)
    bot.register_next_step_handler(message, get_value_int_sign)

def get_value_int_sign(message):
    global sign
    sign = message.text
    line_creator(message)
    bot.send_message(message.chat.id,"Введи 2е число ")
    bot.register_next_step_handler(message, get_value_int_b )

def get_value_int_b(message):
    global b
    b = int(message.text)
    line_creator(message)
    modul_init(message)


def get_value_complex_a(message):
    global a
    a = complex(message.text)
    line_creator(message)
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)  
    but1 = types.KeyboardButton("+") 
    but2 = types.KeyboardButton("-")
    but3 = types.KeyboardButton("/")
    but4 = types.KeyboardButton("*")
    markup.add(but1)    
    markup.add(but2)  
    markup.add(but3)
    markup.add(but4)
    bot.send_message(message.chat.id,"Введите знак", reply_markup = markup)
    bot.register_next_step_handler(message, get_value_complex_sign)

def get_value_complex_sign(message):
    global sign
    sign = message.text   
    line_creator(message) 
    bot.send_message(message.chat.id, "Введи 2е число ")  
    bot.register_next_step_handler(message, get_value_complex_b)

def get_value_complex_b(message):
    global b
    b = complex(message.text)
    line_creator(message)
    modul_init(message)


def modul_init(message):
    modul.init(a,b)
    res = "ошибка ввода"
    if sign == "+":
        res = modul.summ()
    elif sign == "-":
        res = modul.diff()
    elif sign == "*":
        res = modul.multi()
    elif sign == "/":
        res = modul.div()
    elif sign == "//":
        res = modul.div_cel()
    elif sign == "%":
        res = modul.div_ost()
    out(message,res)


def out(message,res):
    bot.send_message(message.chat.id,f'{res}')

def line_creator(message):
    seconds = time.time()
    local_time = time.ctime(seconds)
    line = str (message.from_user.first_name) + ' - ' + str(local_time) + ' - ' + str(message.text)+'\n'
    log_creator(line)

def log_creator(text):
    with open ('log.txt', 'a') as data:
        data.writelines(text)

bot.infinity_polling() 