# Напишите функцию, которая принимает одно число и проверяет,
# является ли оно простым
numeric = int(input("Введите число"))


def poisk(number):
    for i in range(2, number, 1):
        if number % i == 0:
            return False
    return True

print(poisk(poisk(numeric)))
