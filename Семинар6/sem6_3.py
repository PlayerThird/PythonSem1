# Дан список чисел.
# Посчитайте, сколько в нем пар элементов, равных друг другу.
# Считается, что любые два элемента, равные друг другу образуют одну пару, которую необходимо посчитать.
# Вводится список чисел. Все числа списка находятся на разных строках.
from random import randint
fir_num = int(input("Кол-во эл 1го списка:"))
first_dic = [randint(1, 4) for i in range(fir_num)]
print(first_dic)
dict = dict()
for i in first_dic:
    dict[i] = dict.get(i,0) + 1
print(dict)
count = 0
for k,v in dict.items():
    if v//2 > 0:
        print(f"Элемент {k} встречается {v//2}")
        count += v//2
print(f"Всего встречается = {count}")