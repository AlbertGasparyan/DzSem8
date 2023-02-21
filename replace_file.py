def replace():
    search_text = input('Введите искомое значение:')
    replace_text = input('На тчо хотели бы поменять?')
    with open('PhoneInfo.txt','r',encoding='utf-8') as data:
        file=data.read()
        file=file.replace(search_text,replace_text)
    with open('PhoneInfo.txt','w',encoding='utf-8') as data:
        data.write(file)
    print(f'Было произведено изменение в файле\n'
      f'{search_text} на {replace_text}')