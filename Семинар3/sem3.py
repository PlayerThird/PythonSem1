# Дан список чисел.
# Определите, сколько в нем встречается различных чисел.
import random

my_list = [random.randint(0,10) for _ in range(20)] # Зарандомим список
print(my_list)
print(len(set(my_list)))#выдаёт кол-во элементов в массиве

