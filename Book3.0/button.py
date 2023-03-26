from tkinter import *
import conf_but
from tkinter import ttk
import saver


def main_button() -> Button:
    # clear = ttk.Button(text='Очистить от мусора', command=conf_but.clear)
    # clear.pack()
    but1 = ttk.Button(text='1.Показать контакт', command=conf_but.case1)
    but1.pack()
    but2 = ttk.Button(text='2.Создать контакт', command=conf_but.case2)
    but2.pack()
    but3 = ttk.Button(text='3.Найти контакт', command=conf_but.case3)
    but3.pack()
    but4 = ttk.Button(text='4.Изменить контакт', command=conf_but.case4)
    but4.pack()
    but5 = ttk.Button(text='5.Удалить контакт', command=conf_but.case5)
    but5.pack()
    but6 = ttk.Button(text='6.Сохранить контакт', command=conf_but.case6)
    but6.pack()
    # but7 = ttk.Button(text='7.Выход', command=conf_but.case7)
    # but7.pack()
    #
    # def single_click(event):
    #     but7["text"] = "Закрыть можно только через крестик"
    #
    # def double_click(event):
    #     but7["text"] = conf_but.case7()
    #
    # def focus(event):
    #     but7["text"] = "Ну попробуй"
    #
    # def left(event):
    #     but7["text"] = "Уже сдался? В)"
    #
    # but7.bind("<Enter>", focus)
    # but7.bind("<Leave>", left)
    #
    # but7.bind("<ButtonPress-1>", single_click)
    # but7.bind("<Double-ButtonPress-1>", double_click)
