# Дана последовательность из N целых чисел и число K.
# Необходимо сдвинуть всю последовательность (сдвиг - циклический) на K элементов вправо, K – положительное число.
N = int(input("Введите N(размер массива)"))
K = int(input("Введите K"))
new_arr = [i for i in range(N)]
print(new_arr)
arr_first = new_arr[:K]
print(arr_first)
arr_two = new_arr[K:]
print(arr_two)
my_list = arr_two + arr_first
print(my_list)
