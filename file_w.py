def info_get():
    info=[]
    last_name=input('Введите фамилию:')
    info.append(last_name)
    first_name=input('Введите имя:')
    info.append(first_name)
    phone_number=''
    valid=False
    while not valid:
        try:
            phone_number=input('Введите ваш номер телефона:')
            if len(phone_number)!=11:
                print(f"Вы ввели не корректный номер телефона!\nОн должен состоять из 11 цифр.")
            else:
                valid=True
        except:
            print("Попробуйте ввести цифры, а не буквы - должно сработать.")
    info.append(phone_number)
    description= input("Введите описание к вашему номеру:")
    info.append(description)
    return info

def writing_scv(info):
    file = "PhoneInfo.scv"
    with open(file,'a',encoding='utf-8') as data:
        data.write(f"{info[0]};{info[1]};{info[2]};{info[3]}\n")

def writing_txt(info):
    file = "PhoneInfo.txt"
    with open(file,'a',encoding="utf-8") as data:
        data.write(f"Фамилия: {info[0]}\n\n"
                   f"Имя: {info[1]}\n\n"
                   f"Номер телефона: {info[2]}\n\n"
                   f"Описание: {info[3]}\n\n\n")


