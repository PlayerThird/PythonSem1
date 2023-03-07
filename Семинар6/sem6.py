# Даны два массива чисел.
# Требуется вывести те элементы первого массива (в том порядке, в каком они идут в первом массиве), которых нет во втором массиве.
# Пользователь вводит число N - количество элементов в первом массиве, затем N чисел - элементы массива.
# Затем число M - количество элементов во втором массиве.
# Затем элементы второго массива
from random import randint
fir_num = int(input("Кол-во эл 1го списка:"))
sec_num = int(input("Кол-во эл 2го списка:"))
finish = list()
first_dic = [randint(1, 15) for i in range(fir_num)]
second_dic = [randint(1, 15) for i in range(sec_num)]
print(first_dic)
print(second_dic)
for item in first_dic:
    if item not in second_dic:
        finish.append(item)
if not finish:
    print("Все повторяются")
else:
    print(finish)