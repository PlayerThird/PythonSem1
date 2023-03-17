import model
import view

pb = model.get_phone_book()


def case1():
    model.open_file()
    view.show_message("Файл успешно открыт")


def case2():
    model.save_file()
    view.show_message("Файл успешно сохранён")


def case3():
    view.show_contacts(pb, 'Телефонная книга пуста или не открыта')


def case4():
    contact = view.add_contact()
    model.add_contact(contact)


def case5():
    if view.show_contacts(pb, 'Телефонная книга пуста или не открыта'):
        index = view.input_index("Введите номер изменяемого контакта")
        contact = view.change_contact()
        model.change_contact(contact, index)
        view.show_message(f"Контакт {model.get_phone_book()[index - 1].get('name')} успешно изменён")


def case6():
    return
