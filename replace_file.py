def replace():
    with open('PhoneInfo.txt','r',encoding='utf-8') as data:
        old_data=data.read()
    new_data=old_data.replace()

    with open('PhoneInfo.txt''w') as data:
        data.write(new_data)