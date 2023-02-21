from os.path import exists
from scv_file import creating
from file_w import*
from export import from_file








def view():
    print(from_file('PhoneInfo.txt'))

def record_info():
    info=info_get()
    writing_txt(info)
    writing_scv(info)


def choice():
    flag = input("To continue working, press \'yes\', or any symbol to complete the work...\n ")
    while flag.lower()=='yes':
        path = "PhoneInfo.scv"
        valid = exists(path)
        if not valid:
            creating()
        choice_action=input("Enter \'yes\' if you want to record new data, "
                            "and any other character if you want to view the directory in the console:\n")
        if choice_action.lower()=="yes":
            record_info()
        else:
            view()
        flag=input("To continue working, press \'yes\', or any symbol to complete the work...\n")
    print("Work ending")












