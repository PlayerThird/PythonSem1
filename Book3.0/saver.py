from tkinter import ttk
import phone_book


def add_contact(pb: phone_book.PhoneBook):

    pb = pb
    ent_name = ttk.Entry()
    ent_name.pack(padx=6, pady=6)
    ent_tel = ttk.Entry()
    ent_tel.pack(padx=6, pady=6)
    ent_com = ttk.Entry()
    ent_com.pack(padx=6, pady=6)

    def input_contact():
        name = ent_name.get()
        phone = ent_tel.get()
        comm = ent_com.get()
        pb.new_contact(name, phone, comm)
    save = ttk.Button(text="Save", command=input_contact)
    # print(save)
    save.pack()


