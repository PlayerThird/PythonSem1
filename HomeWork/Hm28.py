# Напишите рекурсивную функцию sum(a, b), возвращающую сумму двух целых неотрицательных чисел.
# Из всех арифметических операций допускаются только +1 и -1.
# Также нельзя использовать циклы.
first_num = int(input("Введите число a: "))
second_num = int(input("Введите число b: "))


def sum(a, b):
    if b >= 1:
        return sum(a+1, b - 1)
    else:
        return a


print(sum(first_num, second_num))
