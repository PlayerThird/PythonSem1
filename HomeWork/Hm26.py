# Напишите программу, которая на вход принимает два числа A и B,
# и возводит число А в целую степень B с помощью рекурсии.
first_num = int(input("Введите число: "))
second_num = int(input("Введите степень: "))


def step(a, b):
    if b > 1:
        return a * step(a, b - 1)
    else:
        return a


print(step(first_num, second_num))
