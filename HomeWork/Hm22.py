# Даны два неупорядоченных набора целых чисел (может быть, с повторениями).
# Выдать без повторений в порядке возрастания все те числа, которые встречаются в обоих наборах.
# Пользователь вводит 2 числа. n - кол-во элементов первого множества. m - кол-во элементов второго множества.
# Затем пользователь вводит сами элементы множеств.
import random
prov = input("Вы хотите довериться Богу Рандома? (+ или -)")
multiplicity = int(input("Введите кол-во элементов первого множества"))
multiplicity_s = int(input("Введите кол-во элементов второго множества"))
spis_fir = list()
spis_sec = list()
if prov == "+":
    spis_fir = (random.randint(1, 10) for _ in range(multiplicity))
    spis_sec = (random.randint(1, 10) for _ in range(multiplicity_s))
    # print(f"Первый список: ")
    # for item in spis_fir:
    #     print(spis_fir)
    #
    # print(f"Второй список: ")
    # for item in spis_sec:
    #     print(spis_sec) очень странно выводит
else:
    print("Заполните первый список ↓")
    i = 0
    while i < multiplicity:
        spis_fir.append(input(f"{i+1}:"))
        i +=1
    print("Заполните второй список ↓")
    i = 0
    while i < multiplicity_s:
        spis_sec.append(input(f"{i+1}:"))
        i += 1
mnoj_fir = set()
mnoj_sec = set()
for item in spis_fir:
    mnoj_fir.add(item)
for item in spis_sec:
    mnoj_sec.add(item)
mnoj_fin = mnoj_fir.union(mnoj_sec)
mnoj_fin = sorted(mnoj_fin)

print(*mnoj_fin)
