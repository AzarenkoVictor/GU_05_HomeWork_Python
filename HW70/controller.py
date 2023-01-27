import view
import import_export

def button_click():
    b = view.init_questin()
    view.init_choise(b)
    if b == 1:
        a = view.add_student()
        view.init(a)
        import_export.import_student(a)
    elif b == 2:
        import_export.export_student()
    else:
        print('Неверный выбор')