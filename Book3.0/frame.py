from tkinter import *
from tkinter import ttk # кнопки
import button



def new_frame():
    root = Tk()
    root.title("Тел справка")
    root.geometry("500x700")
    icon = PhotoImage(file='icons8-brain-94.png')
    root.iconphoto(False, icon)
    ttk.Style().theme_use("clam")

    def finish():
        root.destroy()  # ручное закрытие окна и всего приложения
        print("Заебумба, да? :)")

    main_menu = '''Главное меню:'''
    label = Label(text=main_menu)
    label.pack()

    button.main_button()
    close_button = ttk.Button(root, text="7. Закрыть окно", command=lambda: root.destroy())
    close_button.pack()
    # close_button = ttk.Button(root, text="Очистка", command=lambda: root.delete(ALL))
    # close_button.pack()



     #              заменить на функцию закрития по кнопке в меню
    root.protocol("WM_DELETE_WINDOW", finish)#Закрытие приложение с сообщением

    root.mainloop()