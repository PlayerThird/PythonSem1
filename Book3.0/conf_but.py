import delete
import frame

import phone_book
import saver
import search
import change
from tkinter import ttk
from tkinter.messagebox import showinfo

pb = phone_book.PhoneBook("phone.txt")

# def clear():
#     frame.new_frame()


def case1():#1.Показать контакт
    label = ttk.Label(text=pb,background="#1fb2db")
    label.pack()
    showinfo(title = "Контакты",message = pb)



def case2():#2.Создать контакт
    saver.add_contact(pb)



def case3():#3.Найти контакт
    search.search(pb)


def case4():#4.Изменить контакт
    change.change(pb)


def case5():# 5.Удалить контакт
    delete.delete(pb)

def case6():#6.Сохранить контакт
    pb.save()

# def case7():#7.Выход
#     root.destroy()