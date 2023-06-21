import datetime
from datetime import date
import text_main


def main_menu() -> int:
    print(text_main.main_menu)
    length_menu = len(text_main.main_menu.split('\n')) - 1
    while True:
        choice = input("Выберите пункт меню:")
        if choice.isdigit() and 0 < int(choice) <= length_menu:
            return int(choice)
        else:
            print(f"Введите число от 1 до {length_menu}")


def show_note(note_book: list[dict], error_message: str):
    if not note_book:
        print(error_message)
        return False
    else:

        for i, note in enumerate(note_book):
            print(f"{note.get('index'):<5} "
                  f"{note.get('head'):<10} "
                  f"{note.get('body'):<30} "
                  f"{note.get('date'):<10}")
        return True


def add_note() -> dict:
    index = input("Введите индекс")
    head = input("Введите заголовок")
    body = input("Введите заметку")
    data = str(date.today())
    return {'index': index, 'head': head, 'body': body, 'date': data}


def input_index(message: str):
    return int(input(message))


def change_contact(notebook: list[dict], index: int):
    print('Введите новые данные или оставьте пустое поле, если нет изменений')
    note = add_note()
    return {'index': note.get('index') if note.get('index') else notebook[note.get(index)].get('index'),
            'head': note.get('head') if note.get('head') else notebook[note.get(index)].get('head'),
            'body': note.get('body') if note.get('body') else notebook[note.get(index)].get('body'),
            'date': str(date.today()) }


def show_message(message: str):
    print("-" * len(message))
    print(message)
    print('-' * len(message))


def returnnote(notebook: list[dict], index: int):
    for i, note in enumerate(notebook):
        ind = int(note.get('index'))
        if ind == int(index):
            return {'index':note.get('index'),
            'head':note.get('head'),
            'body':note.get('body'),
            'date':note.get('date')}

