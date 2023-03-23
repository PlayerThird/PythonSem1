from tkinter import ttk
import phone_book


def change(pb: phone_book.PhoneBook):

    pb = pb
    ent_ind = ttk.Entry()
    ent_ind.pack(padx=6, pady=6)
    ent_name = ttk.Entry()
    ent_name.pack(padx=6, pady=6)
    ent_tel = ttk.Entry()
    ent_tel.pack(padx=6, pady=6)
    ent_com = ttk.Entry()
    ent_com.pack(padx=6, pady=6)
    # name = ent_name.get()
    # phone = ent_tel.get()
    # comm = ent_com.get()
    def input_contact():
        index = int(ent_ind.get())
        name = ent_name.get()
        phone = ent_tel.get()
        comm = ent_com.get()
        pb.change(index -1,name, phone, comm)
    save = ttk.Button(text="Save", command=input_contact)
    # print(save)
    save.pack()



# def save_new_cont(name: str, phone: str, comm: str):
#     return {'name': name, 'phone': phone, 'comment': comm}
