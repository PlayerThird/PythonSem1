from tkinter import *
import conf_but
from tkinter import ttk



def main_button() -> Button:
    but1 = ttk.Button(text='1. Открыть файл', command=conf_but.case1)
    but1.pack()
    but2 = ttk.Button(text='2. Сохранить', command=conf_but.case2)
    but2.pack()
    but3 = ttk.Button(text='3. Показать контакты', command=conf_but.case3)
    but3.pack()
    but4 = ttk.Button(text='4. Добавить контакт', command=conf_but.case4)
    but4.pack()
    but5 = ttk.Button(text='5. Изменить контакт', command=conf_but.case5)
    but5.pack()
    but6 = ttk.Button(text='6. Выйти', command=conf_but.case6)
    but6.pack()
    def single_click(event):
        but6["text"] = "Это всё, на что ты способен?"

    def double_click(event):
        conf_but.case6()

    but6.bind("<ButtonPress-1>", single_click)
    but6.bind("<Double-ButtonPress-1>", double_click)






