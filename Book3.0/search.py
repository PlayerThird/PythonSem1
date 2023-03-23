from tkinter import ttk
import phone_book
from tkinter.messagebox import showinfo


def search(pb: phone_book.PhoneBook):

    pb = pb
    ent_word = ttk.Entry()
    ent_word.pack(padx=6, pady=6)

    def input_contact():
        word = ent_word.get()
        showinfo(title = "Итоги поиска",message = pb.search(word))
    search_con = ttk.Button(text="Search", command=input_contact)
    # print(save)
    search_con.pack()



