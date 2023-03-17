
my_string = '452465467567547'
my_string = list(my_string)
print(my_string)

# for i in range(len(my_string)):
#     my_string[i] = int(my_string[i])

my_string = list(map(int, my_string))

print(my_string)

my_string= list(filter(lambda x: x%2 == 0, my_string)) # Фильтруем my_string с условием x%2 == 0
# Лябда выдаёт булевое значение

print(my_string)