student = ''
choise = 0

def init_questin():
    choise = int(input('Выберите действие: 1- Запись, 2 - Вывод '))
    return choise

def add_student():
    id = input('Введите id ')
    name = input('Введите имя ')
    last_name = input('Введите фамилию ')
    tel = input('Введите телефона ')
    comment = input('Введите комментрий ')
    student = f'{id},{name},{last_name},{tel},{comment}\n'
    return student

def init(a):
    global student
    student = a

def init_choise(b):
    global choise
    choise = b