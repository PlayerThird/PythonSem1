note_book = []
path = "note.txt"


def open_file():
    with open(path,'r',encoding='UTF-8') as file:
        data = file.readlines()
    for fields in data:
        fields = fields.strip().split(';')
        note = {'index': fields[0],
                   'head': fields[1],
                   'body': fields[2],
                   'date': fields[3]}#разделили строки на словарь
        note_book.append(note)

def save_file():
    data =[]
    for note in note_book:
        data.append(';'.join(list(note.values())))#склеиваем наш словарь
    data = '\n'.join(data)
    with open(path,'w', encoding='UTF-8') as file:
        file.write(data)#сохраняем склееный словарь в файл

def get_note_book():
    return note_book

def add_note(note: dict):
    note_book.append(note)

def change_contact(oldnote: dict,note: dict):
    for i,notus in enumerate(note_book):
        if notus == oldnote:
            note_book.pop(i)
            break
    note_book.append(note)