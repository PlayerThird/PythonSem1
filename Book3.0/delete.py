from tkinter import ttk
import phone_book
from tkinter.messagebox import showinfo


def delete(pb: phone_book.PhoneBook):

    pb = pb
    ent_index = ttk.Entry()
    ent_index.pack(padx=6, pady=6)

    def input_contact():
        index = int(ent_index.get())
        pb.delete(index - 1)
    search_con = ttk.Button(text="Search", command=input_contact)
    # print(save)
    search_con.pack()



# def save_new_cont(name: str, phone: str, comm: str):
#     return {'name': name, 'phone': phone, 'comment': comm}
