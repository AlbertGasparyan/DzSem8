import pathlib
from os.path import exists
from scv_file import creating
from file_w import*
from export import from_file
from replace_file import replace



def view():
    print(from_file('PhoneInfo.txt'))

def record_info():
    info=info_get()
    writing_txt(info)
    writing_scv(info)


def choice():
    flag = input("Для работы напиши \'пуск\', или любой символ для конца работы...\n ")
    while flag.lower()=='пуск':
        path = "PhoneInfo.scv"
        valid = exists(path)
        if not valid:
            creating()
        choice_action=input("Введите \'да\', если хотите записать новые данные."
                            "\nИли введите любой символ для возврата на шаг назад...\n")
        if choice_action.lower()=="да":
            record_info()
        else:
            view()
        choice_delete_replace=input('Если вы хотите удалить данные напишите - \'удалить\'\n'
                                    'Если вы хотите изменить файл напишите - \'изменить\'\n'
                                    'Или введите любой симовл для возврата в начало.\n')
        if choice_delete_replace.lower()=='удалить':
            file = pathlib.Path("PhoneInfo.txt")
            file.unlink()
            file = pathlib.Path("Phoneinfo.csv")
            file.unlink()
            file = pathlib.Path("PhoneInfo.scv")
            file.unlink()
            print("Все ваши файлы были удалены!")
        elif choice_delete_replace.lower()=='изменить':
            replace()
        else:
            view()

        flag=input("Для работы напиши \'пуск\', или любой символ для конца работы...\n ")
    print("Конец работы")












