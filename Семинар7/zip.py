my_string = 'fdgujtyjghjjh'
my_list = [i for i in range(10)]
print(my_string)
print(my_list)

# new_list =[]
# for i, item in enumerate(my_string):
#     new_list.append((my_string[i], my_list[i]))
new_list = list(zip(my_string, my_list))# Из 2 "списков" преобразует в список кортежей(работает с минимальным списком)
print(new_list)