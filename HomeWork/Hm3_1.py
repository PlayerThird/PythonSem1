# Задаем длину списка наполненного рандомными числами от 1 до 100.
# Вводим искомое число X
# Программа должна вывести в консоль сколько раз встречается в заданном списке искомое число X,
# которое мы вводим с клавиатуры, либо выводим на экран, максимально близкое ему по значению
import random

dlina = int(input("Введите размер списка:"))
slovar = {}

spisok = (random.randint(1, 100) for _ in range(dlina))
for item in spisok:
    slovar[item] = slovar.get(item,0) + 1
chislo = int(input("Введите число, которое ищите:"))
search_fir = chislo
search_sec = chislo
if chislo == spisok(chislo,):
    print(spisok(chislo))
else:
    while (spisok(chislo,) != search_fir) or (spisok(chislo,) != search_sec):
        search_fir += 1
        search_sec -= 1
    if spisok.get(search_fir) != None:
        print(spisok(search_fir))
    else:
        print(spisok(search_sec))