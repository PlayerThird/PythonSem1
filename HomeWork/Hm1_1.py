# Найдите сумму цифр трехзначного числа.
# Пример:
# 123 -> 6 (1 + 2 + 3)
# 100 -> 1 (1 + 0 + 0)
number = int(input("Введите число"))
sum = int(number % 10 + number % 100 / 10 + number % 1000/ 100)
print(number % 10)
print(number % 100 / 10)
print(number % 1000/ 100)
print(f"Сумма равна = {sum}")