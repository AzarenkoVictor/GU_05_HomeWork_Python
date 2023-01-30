import random

random_student_name =('Иван', 'Виктор', 'Никита', 'Ольга', 'Александр', 'Людмила', 'Николай' )
random_student_last_name = ('Иванов','Петров','Сидоров','Фридман','Греф','Сталин','Троцкий')
random_lessons_list = ('Математика','Информатика','Русский Язык','Английский Язык','Физика','Химия','Физкультура')

def random_student_selector():
    random_student = random_student_name[random.randint(0,6)] + ' ' + random_student_last_name[random.randint(0,6)]
    return random_student

def random_lesson_selector():
    random_lesson = random_lessons_list[random.randint(0,6)]
    return random_lesson

def random_grade_selector():
    random_grade = random.randint(1,5)
    return random_grade
