from tkinter import *
from tkinter import ttk # кнопки
import button
import text_fields

if __name__ == '__main__':
    root = Tk()
    root.title("Test window")
    root.geometry("400x400")
    icon = PhotoImage(file='icons8-brain-94.png')
    root.iconphoto(False, icon)

    def finish():
        root.destroy()  # ручное закрытие окна и всего приложения
        print("Заебумба, да? :)")

    main_menu = '''Главное меню:'''
    label = Label(text=main_menu)
    label.pack()

    # clicks = 0
    # def click_button():
    #     global clicks
    #     clicks += 1
    #     # изменяем текст на кнопке
    #     btn["text"] = f"Clicks {clicks}"
    #
    #
    # btn = ttk.Button(text="Click Me", command=click_button)
    # btn.pack()
    but = ttk.Button(text="Start",command= button.main_button)
    but.pack()

    #              заменить на функцию закрития по кнопке в меню
    root.protocol("WM_DELETE_WINDOW", finish)#Закрытие приложение с сообщением

    root.mainloop()