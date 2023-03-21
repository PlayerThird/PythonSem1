from tkinter import ttk
phone_book = []
path = "phone.txt"


def open_file():
    with open(path,'r',encoding='UTF-8') as file:
        data = file.readlines()
    for fields in data:
        fields = fields.strip().split(';')
        contact = {'name': fields[0],
                   'phone': fields[1],
                   'comment': fields[2]}#разделили строки на словарь
        phone_book.append(contact)

def save_file(error_message: str):
    data =[]
    if phone_book:
        for contact in phone_book:
            data.append(';'.join(list(contact.values())))#склеиваем наш словарь
        data = '\n'.join(data)
        with open(path,'w', encoding='UTF-8') as file:
            file.write(data)#сохраняем склеиный словарь в файл
            return True
    else:
        label = ttk.Label(text=error_message)
        label.pack()
        return False
def get_phone_book():
    return phone_book

def add_contact(contact: dict):
    phone_book.append(contact)

def change_contact(contact: dict, index: int):
    phone_book.pop(index-1)
    phone_book.insert(index-1, contact)