import servise as s
file_name = "spravochnik.txt"
#file = open(path_to_r, 'r', encoding='UTF-8'): # r -- read -- чтение perem любое название
# name = input("Введите Имя")
# fam = input("Введите Фамилию")
# number = input("Введите Номер")
# full_contact = [name,fam,number]
while True:
    action = int(input("Введите номер меню:\n 1- показать файл\n 2- найти\n 3- добавить\n 4-редактировать\n 5- удалить\n 0- Выход"))
    if action == 0:
        break
    elif action == 1:
        s.print_contacts(s.load_data(file_name))
        print()
    elif action == 2:
        text = input("Введите имя:")
        s.find_contacts(s.load_data(file_name), text)
    elif action == 3:
        name = input("Введите имя")
        sec_name = input("Введите фамилию")
        number = input("Введите номер")
        s.add_data(file_name, file_name+""+ sec_name, number)
        print()
    elif action == 4:
        contacts = s.load_data(file_name)
    elif action == 5:
        break
    elif action == 0:
        break
    else:
        print("Такой цифры нет")
