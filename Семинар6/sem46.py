# Два различных натуральных числа n и m называются дружественными, если сумма делителей числа n (включая 1, но исключая само n) равна числу m и наоборот.
# Например, 220 и 284 – дружественные числа. По данному числу k выведите все пары дружественных чисел, каждое из которых не превосходит k.
# Программа получает на вход одно натуральное число k, не превосходящее 105.
# Программа должна вывести  все пары дружественных чисел, каждое из которых не превосходит k.
# Пары необходимо выводить по одной в строке, разделяя пробелами.
# Каждая пара должна быть выведена только один раз (перестановка чисел новую пару не дает).
len_arr = int(input("Введите число"))
my_dict = {}
for i in range(1, len_arr):
    my_dict[i] = my_dict.get(i,0)
    for j in range(1, i//2+1):
        if i % j == 0:
            my_dict[i] = my_dict.get(i,0) + j

print(my_dict)

for key1, val1 in my_dict.items():
    for key2, val2 in my_dict.items():
        if key2>key1:
            if key1!=key2 and val1 == key2 and val2 == key1:
                print(f"{key1} {key2}")

