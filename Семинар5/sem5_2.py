# Хакер Василий получил доступ к классному журналу и хочет заменить все свои минимальные оценки на максимальные.
# Напишите программу, которая заменяет оценки Василия,
# но наоборот: все максимальные – на минимальные.

from random import randint
ocenki = [randint(1, 5) for i in range(8)]
i=int(0)
print(ocenki)
def change(ocenki):
    for i in range(len(ocenki)):
        if ocenki[i] == 5:
            ocenki[i] = 1
        elif ocenki[i] == 4:
            ocenki[i] = 2
        return ocenki
print(change(ocenki))