# Петя и Катя – брат и сестра.
# Петя – студент, а Катя – школьница.
# Петя помогает Кате по математике.
# Он задумывает два натуральных числа X и Y (X,Y≤1000), а Катя должна их отгадать.
# Для этого Петя делает две подсказки. Он называет сумму этих чисел S и их произведение P.
# Помогите Кате отгадать задуманные Петей числа.
import random

first,second = random.randint(0,1000),random.randint(0,1000)
print(f"Сумма этих чисел = {first+second}")
print(f"Произведение = {first*second}")
otvet_first = int(input("Какое первое число я загадал?"))
otvet_second = int(input("Какое второе число я загадал?"))
if first == otvet_first or second == otvet_first and first == otvet_second or second == otvet_second:
    print("Ля красава, мелкая")
else:
    print("Хаха, тупая школота ;)")