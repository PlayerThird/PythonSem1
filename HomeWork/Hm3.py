# билет с номером 385916 – счастливый,
# т.к. 3+8+5=9+1+6. Вам требуется написать программу,
# которая проверяет счастливость билета.
# Пример:
# 385916 -> yes
# 123456 -> no
ticket = int(input("Введите числа билетика"))

first_half_ticket = int(ticket%1000)
second_half_ticket = int((ticket - first_half_ticket)/ 1000)
print(first_half_ticket)
print(second_half_ticket)
first_sum = int(first_half_ticket % 10 + first_half_ticket % 100 / 10 + first_half_ticket % 1000/ 100)
second_sum = int(second_half_ticket % 10 + second_half_ticket % 100 / 10 + second_half_ticket % 1000/ 100)
print(first_sum)
print(second_sum)
print("Yes") if first_sum == second_sum else print("No")