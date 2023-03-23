from tkinter import *
from tkinter import ttk # кнопки
import button


if __name__ == '__main__':
    root = Tk()
    root.title("Тел справка")
    root.geometry("500x700")
    icon = PhotoImage(file='icons8-brain-94.png')
    root.iconphoto(False, icon)

    def finish():
        root.destroy()  # ручное закрытие окна и всего приложения
        print("Заебумба, да? :)")

    main_menu = '''Главное меню:'''
    label = Label(text=main_menu)
    label.pack()
    button.main_button()



    #              заменить на функцию закрития по кнопке в меню
    # root.protocol("WM_DELETE_WINDOW", finish)#Закрытие приложение с сообщением

    root.mainloop()