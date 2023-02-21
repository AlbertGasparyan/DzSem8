def creating():
    file = 'Phoneinfo.csv'
    with open(file, 'w', encoding='utf-8') as data:
        data.write(f'Last Name;First Name;Phone number;Description\n')