import model
import view
from tkinter import *
from tkinter import ttk

pb = model.get_phone_book()


def case1():
    model.open_file()
    view.show_message("Файл успешно открыт")
    print(model.get_phone_book())


def case2():
    if model.save_file("Что-то пошло не так, видимо список пуст"):
        label2 = ttk.Label(text=view.show_message("Файл успешно сохранён"))
        label2.pack()

def case3():
    view.show_contacts(pb, 'Телефонная книга пуста или не открыта')


def case4():
    contact = view.add_contact()
    model.add_contact(contact)


def case5():
    if view.show_contacts(pb, 'Телефонная книга пуста или не открыта'):
        index = view.input_index("Введите номер изменяемого контакта")
        contact = view.change_contact(pb,index)
        model.change_contact(contact, index)
        view.show_message(f"Контакт {model.get_phone_book()[index - 1].get('name')} успешно изменён")


def case6():
    Tk().protocol("WM_DELETE_WINDOW", Tk().destroy())
