# Основное дз(из семинара):
# Создать информационную систему позволяющую работать с учениками школы
# функции
# 1   Добавление нового студента (Поля - имя, фамилия)
# 2   Добавление предмета (добавляется всем ученикам сразу)
# 3   Добавление оценки ученику по предмету (выбираем ученика(из существующих), выбираем предмет(из сущ.),пишем оценку )
# 4   Показ списка учеников (имена фамилия)
# 5   Показ листа оценок конкретного ученика
# 10  Выход из программы
# Достаточно хранить данные в переменной

# Доп*:
# 6     ) Добавить функцию генерации сразу ста учеников и записи их в журнал
# (имя - рандомное из списка нескольких имен
# фамилия - рандомная из списка нескольких фамилий
# название предмета - рандом из списка с предметами
# оценка - рандом от 1 до 5)
# 7     ) Вывод средней оценки ученика по одному предмету
# 8     ) Вывод среднего балла по школе по конкретному предмету
# 9     )Вывод количества учеников претендующих на золотую медаль (все оценки либо 4 либо 5)
# Добавить хранение в файле, и импорт из файла

import view
import generator
import save_file
import random

global global_dict
global student_list
global lessons_list

student_list = []
lessons_list = []
global_dict = {}


def choise():
    while True:
        select = view.select()
        if select == 1:
            student = view.add_student()
            if student not in student_list:
                student_list.append(student)
                global_dict[student] = {}
                for lesson in lessons_list:
                    global_dict[student][lesson] = []

        if select == 2:
            lesson = view.add_lesson()
            if lesson not in lessons_list:
                lessons_list.append(lesson)
                for student in student_list:
                    global_dict[student][lesson] = []

        if select == 3:
            student = view.add_student()
            lesson = view.add_lesson()
            grade = view.add_grade()
            global_dict[student][lesson].append(grade)

        if select == 4:
            for student in global_dict:
                print(" ")
                print(student)
                for lesson in global_dict[student].items():
                    if lesson != "":
                        print(lesson)

        if select == 5:
            student = view.add_student()
            while student not in student_list:
                student = view.add_student()
            view.print_item(global_dict[student])

        if select == 6:
            for i in range(100):
                student = generator.random_student_selector()
                if student not in student_list:
                    student_list.append(student)
                    global_dict[student] = {}
                    for lesson in lessons_list:
                        global_dict[student][lesson] = []
                lesson = generator.random_lesson_selector()
                if lesson not in lessons_list:
                    lessons_list.append(lesson)
                    for student in student_list:
                        global_dict[student][lesson] = []
                for i in range(0, random.randint(1, 3)):
                    global_dict[student][lesson].append(
                        generator.random_grade_selector()
                    )

        if select == 7:
            average_grade_list = []
            sum_grade = 0
            count = 0
            student = view.add_student()
            lesson = view.add_lesson()
            for grade in global_dict[student][lesson]:
                if grade > 0:
                    average_grade_list.append(grade)
            for grade in average_grade_list:
                sum_grade += grade
                count += 1
            average_grade = sum_grade / count
            view.print_item(f'Оценки: {average_grade_list}\nСредний балл: {average_grade}')

        if select == 8:
            average_lesson_grade_list = []
            average_grage = 0
            sum_grade = 0
            count = 0
            lesson_select = view.add_lesson()
            while lesson_select not in lessons_list:
                lesson = view.add_lesson()
            for student in global_dict:
                for lesson in global_dict[student]:
                    if lesson == lesson_select:
                        for grade in global_dict[student][lesson]:
                            average_lesson_grade_list.append(grade)
                            sum_grade += grade
                            count += 1

            if count == 0:
                view.print_item(f"По {lesson_select} нет оценок ")
            else:
                average_grage = round((sum_grade / count), 2)
                view.print_item(
                    f"Список всех оценок по {lesson_select}: {average_lesson_grade_list}"
                )
                view.print_item(
                    f"Средняя оценка по {lesson_select} равна: {average_grage}"
                )

        if select == 9:
            star_student = 0
            star_student_list = []
            temp_student_list = []
            count = 0
            for student in global_dict:
                for lesson in global_dict[student]:
                    for grade in global_dict[student][lesson]:
                        temp_student_list.append(grade)
                if (1 or 2 or 3) not in temp_student_list:
                    star_student += 1
                    temp_student_list.clear()
                    star_student_list.append(student)
            view.print_item(f'Количество потенциальных медалистов: {star_student}\n{star_student_list}')

        if select == 10:
            break

        if select == 11:
            break

        if select == 12:
            break
