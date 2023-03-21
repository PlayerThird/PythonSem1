from tkinter import ttk
def show_contacts(book: list[dict], error_message: str):
    if not book:
        print(error_message)
        return False
    else:
        for i, contact in enumerate(book,1):
            label3 = ttk.Label(text=f"{i}. {contact.get('name'):<20} "
                  f"{contact.get('phone'):<20} "
                  f"{contact.get('comment'):<20}",background="#1fb2db")
            label3.pack(expand=True)
        return True



def add_contact() -> dict:
    ent_name = ttk.Entry()
    ent_name.pack(padx=6, pady=6)
    ent_tel = ttk.Entry()
    ent_tel.pack(padx=6, pady=6)
    ent_com = ttk.Entry()
    ent_com.pack(padx=6, pady=6)
    save = ttk.Button(text="Save", command=input_cont)
    name = ent_name.get()
    phone = ent_tel.get()
    comm = ent_com.get()
    return {'name': name, 'phone': phone, 'comment': comm}


def input_index(message: str):
    return int(input(message))

def change_contact(book: list[dict], index: int):
    print('Введите новые данные или оставьте пустое поле, если нет изменений')
    contact = add_contact()
    return {'name': contact.get('name') if contact.get('name') else book[index-1].get('name'),
            'phone': contact.get('phone') if contact.get('phone') else book[index-1].get('phone'),
            'comment': contact.get('comment') if contact.get('comment') else book[index-1].get('comment')}

def show_message(message: str):
    return f"{'-'*len(message)}\n{(message)}\n{('-'*len(message))}"
