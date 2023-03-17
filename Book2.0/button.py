from tkinter import *
import conf_but


def main_button() -> Button:
    Button(text='1. Открыть файл', command=conf_but.case1())
    # but1.pack()
    Button(text='2. Сохранить', command=conf_but.case2())
    # but2.pack()
    Button(text='3. Показать контакты', command=conf_but.case3())
    # but3.pack()
    Button(text='4. Добавить контакт', command=conf_but.case4())
    # but4.pack()
    Button(text='5. Изменить контакт', command=conf_but.case5())
    # but5.pack()
    Button(text='6. Выйти', command=conf_but.case6())
    # but6.pack()








