# Задаем длину списка наполненного рандомными числами от 1 до 100.
# Вводим искомое число X
# Программа должна вывести в консоль сколько раз встречается в заданном списке искомое число X,
# которое мы вводим с клавиатуры, либо выводим на экран, максимально близкое ему по значению
import random

dlina = int(input("Введите размер списка:"))

spisok = (random.randint(1, 100) for _ in range(dlina))
print(spisok)

slovar = {}
for item in spisok:
    slovar[item] = slovar.get(item, 0) + 1
print(slovar)
chislo = int(input("Введите число, которое ищите:"))
search_fir = chislo
search_sec = chislo
if slovar.get(chislo) is not None:

    print('{} встречается:{} раз'.format(chislo, slovar[chislo]))
else:
    while (slovar.get(search_fir) != None) and (slovar.get(search_sec) != None):
        search_fir += 1
        search_sec -= 1
    if slovar.get(search_fir) != None:

        print('{} встречается:{} раз'.format(search_fir, slovar[search_fir]))
    elif slovar.get(search_sec) != None:

        print('{} встречается:{} раз'.format(search_sec, slovar[search_sec]))