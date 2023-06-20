import model
import view


def start():
    while True:
        pb = model.get_note_book()
        choice = view.main_menu()
        match choice:
            case 1:
                model.open_file()
                view.show_message("Файл успешно открыт")
            case 2:
                model.save_file()
                view.show_message("Файл успешно сохранён")
            case 3:
                view.show_note(pb, 'Заметок нет или не открыт файл с ними')
            case 4:
                note = view.add_note()
                model.add_note(note)
            case 5:
                if view.show_note(pb, 'Заметок нет'):
                    index = view.input_index("Введите индекс заметки, которую хотите изменить")
                    oldnote = view.returnnote(pb,index)
                    note = view.change_contact(pb,index)
                    model.change_contact(oldnote,note)
                    view.show_message(f"Заметка успешно изменёна")
            case 6:
                return