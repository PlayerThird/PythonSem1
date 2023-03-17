# В списке хранятся числа. Нужно выбрать только чётные числа и составить список пар(число; квадрат числа)
#Мой вариант
# spisok = [1,2,3,5,8,15,23,38]
# itog =[]
# for item in spisok:
#     if item%2==0:
#         itog.append(str(f"{item},{item*item}"))
# print(itog)
#Как должно выглядить
# data = [1,2,3,5,8,15,23,38]
# res = list()
#
# for i in data:
#     if i %2 == 0:
#         res.append((i, i**2))
#
# print(res)
def select(f, col): # f -- функция, col -- значение
    return [f(x) for x in col] # Возвращает список, к которой применили функцию f
def where(f,col):
    return [x for x in col if f(x)] # Возвращает элементы, которые прошли условие f(x)
data = [1,2,3,5,8,15,23,38]
res = select(int, data)
print(res)
res = where(lambda x: x%2 ==0,res)
print(res)
res = list(select(lambda x: (x, x**2), res))# возвращаем кортеж из х и х в квадрате
print(res)