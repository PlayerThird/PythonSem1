# Напишите программу, которая принимает на вход строку, и отслеживает, сколько раз каждый символ уже встречался.
# Количество повторов добавляется к символам с помощью постфикса формата _n.
# my_list = [4,2,5,4,4,8,3,2,7]
# 4,2,5,4_1,4_2,8,3,2_1,7
string = input()
dict = {}

for i in string:
    dict[i] = dict.get(i,0) + 1
    if dict[i] == 1:
        print(i, end=", ")
    else:
        print(f"{i}_{dict[i] - 1}", end=", ")