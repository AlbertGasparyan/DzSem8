from os.path import exists
from scv_file import creating
from file_w import*
from export import from_file
from delete_file import delete
from replace_file import replace



def view():
    print(from_file('PhoneInfo.txt'))

def record_info():
    info=info_get()
    writing_txt(info)
    writing_scv(info)

def replace_info():
    replace()

def delete_info():
    delete()

def choice():
    flag = input("Для работы напиши \'да\', или любой символ для конца работы...\n ")
    while flag.lower()=='да':
        path = "PhoneInfo.scv"
        valid = exists(path)
        if not valid:
            creating()
        choice_action=input("Введите \'да\', если хотите записать новые данные\n")
        if choice_action.lower()=="да":
            record_info()
        else:
            view()
        choice_delete_replace=input('Если вы хотите удалить данные напишите - \'удалить\'\n'
                                    'Если вы хотите изменить файл напишите - \'изменить\'\n'
                                    'Или введите любой симовл для возврата в начало.')
        if choice_delete_replace.lower()=='удалить':
            delete_info()
        elif choice_delete_replace.lower()=='удалить':
            replace_info()
            record_info()
        else:
            view()

        flag=input("Для работы напиши \'да\', или любой символ для конца работы...\n ")
    print("Конец работы")












