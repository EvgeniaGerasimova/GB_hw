from data_create import name_data, surname_data, phone_data, address_data


def input_data():
    name = name_data()
    surname = surname_data()
    phone = phone_data()
    address = address_data()
    var = int(input(f'В каком формате записать данные?\n\n'
    f"1 вариант: \n"
    f"{name}\n{surname}\n{phone}\n{address}\n\n"
    f"2 вариант: \n" 
    f"{name};{surname};{phone};{address}\n"
    f"Выберите вариант: "))
    
    while var != 1 and var != 2:
        print("Неправильный ввод")
        var = int(input("Выберите вариант: "))
        
    if var == 1:
        with open('data_first_variant.csv', 'a', encoding = 'utf-8') as f:
            f.write(f"{name}\n{surname}\n{phone}\n{address}\n\n")
    elif var == 2:
        with open('data_second_variant.csv', 'a', encoding = 'utf-8') as f:
            f.write(f"{name};{surname};{phone};{address}\n\n")
         

def print_data():
    print("Вывожу данные из первого файла: \n")
    with open('data_first_variant.csv', 'r', encoding = 'utf-8') as f:
        data_first = f.readlines()
        data_first_list = []
        j = 0
        for i in range(len(data_first)):
            if data_first[i] == '\n' or i == len(data_first) - 1:
                data_first_list.append(''.join(data_first[j:i+1]))
                j=i
        print(''.join(data_first_list))
        
    print("Вывожу данные из второго файла: \n")
    with open('data_second_variant.csv', 'r', encoding = 'utf-8') as f:
        data_second = f.readlines()
        print(*data_second)
        
        
def remove_data():
    print('Из какого файла произвести удаление? \n 1 - справочник_1 \n 2 - справочник_2')
    var = int(input(f'Выберите вариант: '))
    
    while var != 1 and var != 2:
        print("Неправильный ввод")
        var = int(input("Выберите вариант: "))
        
    if var == 1:
        with open('data_first_variant.csv', 'r', encoding="utf-8") as f:
            a = input('Введите Имя или Фамилию для удаления: ')
            lines = f.readlines()
        with open('data_first_variant.csv', 'w', encoding="utf-8") as f:
            for line in lines:
                if a in line:
                    print("Данные удалены")
                else:
                    print(line)    
                    f.write(line)
    elif var == 2:
        with open('data_second_variant.csv', 'r', encoding="utf-8") as f:
            a = input('Введите Имя или Фамилию для удаления: ')
            lines = f.readlines()
        with open('data_second_variant.csv', 'w', encoding="utf-8") as f:
            for line in lines:
                words = line.split(';') 
                updated_line = ';'.join([word for word in words if word != a])
                f.write(updated_line) 
        print('Данные удалены')

                    
                    
def edit_data():
    print('В каком файле произвести изменения? \n 1 - справочник_1 \n 2 - справочник_2')
    var = int(input(f'Выберите вариант: '))
    
    while var != 1 and var != 2:
        print("Неправильный ввод")
        var = int(input("Выберите вариант: "))
        
    if var ==1:    
        search_word = input('Введите имя или фамилию для поиска: ')
        replace_word = input('Введите новое значение: ')
    
        with open('data_first_variant.csv', 'r', encoding="utf-8") as f:
            lines = f.readlines()
    
        with open('data_first_variant.csv', 'w', encoding="utf-8") as f:
            for line in lines:
                if search_word in line:
                    updated_line = line.replace(search_word, replace_word)
                    f.write(updated_line)
                else:
                    f.write(line)   
        print("Замена выполнена успешно")
    
    elif var == 2:
        with open('data_second_variant.csv', 'r', encoding="utf-8") as f:
                search_word = input('Введите имя или фамилию для замены: ')
                replacement = input('Введите новое имя или фамилию: ')
                lines = f.readlines()
    
        with open('data_second_variant.csv', 'w', encoding="utf-8") as f:
            for line in lines:
                words = line.split(';') 
                updated_words = [word if word != search_word else replacement for word in words]
                updated_line = ';'.join(updated_words) 
                f.write(updated_line)
        print("Замена выполнена успешно")