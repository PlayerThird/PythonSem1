path_to_r = 'text.txt'
path_to_w = 'text_2.txt'# В проводнике Copу path
#file = open(path_to_r, 'r', encoding='UTF-8'): # r -- read -- чтение perem любое название
with open(path_to_r, 'r', encoding='UTF-8') as perem: # perem -- любое название
    data1 = perem.read() # Открыл файл, и после конца табов закрывает файл(чтобы не писать file.close())
# data2 = file.readline() # file -- если не используем as выше
# data3 = file.readlines()# Считывает всё, пилит настройки и выдаёт список

# file.close()

print(data1)
# print(data2)
# print(data3)
with open(path_to_w, 'w', encoding='UTF-8') as perem1: # w-- записаь в файл, если такого файла нет, создаёт и записывает
    perem1.write('\nА нам всё равно...')

with open(path_to_w, 'a', encoding='UTF-8') as perem1: # a--открыть для записи, добавив в конец файла, если он существует
    perem1.write('\nА нам всё равно...')