# Определить индексы элементов массива (списка), значения которых принадлежат заданному диапазону
# (т.е. не меньше заданного минимума и не больше заданного максимума)
import random

first_diap = int(input("Введите первый диапазон: "))
second_diap = int(input("Введите второй диапазон: "))
N = int(input("Введите размер списка: "))
spisok = [random.randint(1, 10) for _ in range(N)]
print(spisok)
if first_diap > second_diap:
    first_diap,second_diap = second_diap, first_diap
print("----------------------------")
for i in range(len(spisok)):
    if first_diap < spisok[i] < second_diap:
        print(f"{spisok[i]} : {i}")
