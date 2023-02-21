# Дано натуральное число A > 1.
# Определите, каким по счету числом Фибоначчи оно является, то есть выведите такое число n, что φ(n)=A.
# Если А не является числом Фибоначчи, выведите число -1.
number = int(input("Введите число"))
a1 = 0
a2 = 1
count = 2
result = 0
while result < number:
    result = a1 + a2
    a1 = a2
    a2 = result
    count +=1
if number == result:
    print(f"Число {number} по счету стоит на {count}")
else:
    print(f"Число {number} не является числом Фибоначи....-1")