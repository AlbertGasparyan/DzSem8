def info_get():
    info=[]
    last_name=input('Enter your last name:')
    info.append(last_name)
    first_name=input('Enter your first name:')
    info.append(first_name)
    phone_number=''
    valid=False
    while not valid:
        try:
            phone_number=input('Enter your phone number:')
            if len(phone_number)!=11:
                print(f"It's not phone number.The phone number must consist of 11 symbol!")
            else:
                phone_number = input('Enter your phone number again:')
                valid=True
        except:
            print("Can you enter numbers instead of letters?)")
    info.append(phone_number)
    description= input("Enter descriptions for your number:")
    info.append(description)
    return info

def writing_scv(info):
    file = "PhoneInfo.scv"
    with open(file,'a',encoding='utf-8') as data:
        data.write(f"{info[0]};{info[1]};{info[2]};{info[3]}\n")

def writing_txt(info):
    file = "PhoneInfo.txt"
    with open(file,'a',encoding="utf-8") as data:
        data.write(f"Last name: {info[0]}\n\n"
                   f"First name: {info[1]}\n\n"
                   f"Phone number: {info[2]}\n\n"
                   f"Desscription: {info[3]}\n\n\n")


