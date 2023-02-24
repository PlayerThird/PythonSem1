# Требуется вывести все целые степени двойки
# (т.е. числа вида 2k), не превосходящие числа N.
stepen = 0
chislo = int(input("Введите число"))
prozved = 1
while prozved <= chislo:
    prozved *= 2
    stepen += 1
print(f"Степень равна {stepen-1}")