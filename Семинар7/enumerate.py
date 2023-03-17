my_string = 'fdgujtyjghjjh'
my_string = list(my_string)
print(my_string)

# for i in range(len(my_string)):
#     print(f'{i}. {my_string[i]}')
for i, item in enumerate(my_string,1): #единичка, начало вывода списка...т.е. для красоты
     print(f'{i}. {item}')
