# Дан массив, состоящий из целых чисел.
# Напишите программу, которая в данном массиве определит количество элементов,
# у которых два соседних и, при этом, оба соседних элемента меньше данного.
# Сначала вводится число N — количество элементов в массиве Далее записаны N чисел — элементы массива.
# Массив состоит из целых чисел.

from random import randint
fir_num = int(input("Кол-во эл 1го списка:"))
first_dic = [randint(1, 15) for i in range(fir_num)]
print(first_dic)
count = 0
for i in range(len(first_dic)):
    if i == 0:
        if first_dic[-1] < first_dic[i] > first_dic[i+1]:
            count += 1
    if first_dic[i-1] < first_dic[i] > first_dic[i+1]:
        count += 1
    if i == len(first_dic):
        if first_dic[i-1] < first_dic[i] > first_dic[0]:
            count += 1
    else:
        break
print(count)