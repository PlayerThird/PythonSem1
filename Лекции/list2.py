list_1 = [1,5]
print(list_1)
list_1.append(8)
print(list_1)
for i in range(5):
    list_1.append(i)
print(list_1)

# удаление последнего элемента
list_1 = [12,45,3,8,3,4]
print(list_1.pop())

# срезы
list_1 = [1,2,3,4,5,6,7,8,9,10]
print(list_1[0])              # 1
print(list_1[1])              # 2
print(list_1[len(list_1)-1])  # print(list_1[-1]) то же самое 10
print(list_1[-5])             # 6
print(list_1[:])              # [1,2,3,4,5,6,7,8,9,10]
print(list_1[:2])             # [1,2]
print(list_1[len(list_1)-2:]) # [9,10]
print(list_1[2:9])            # [3,4,5,6,7,8,9]
print(list_1[6:-18])          # []
print(list_1[0:len(list_1):6])# [1,7]
print(list_1[::6])            # [1,7]