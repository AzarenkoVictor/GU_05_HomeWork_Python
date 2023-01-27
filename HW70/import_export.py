import view

def import_student(student):
    with open('BD.txt','a') as data:
        data.writelines(student)

def export_student():
    with open('BD.txt','r') as data:
        for line in data:
            print(line)

        