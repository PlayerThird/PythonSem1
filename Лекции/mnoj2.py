# Операции со множествами в Python
a = {1,2,3,5,8}
b = {2,5,8,13,21}
c = a.copy()          # копирование          # c = {1,2,3,5,8}
u = a.union(b)         #  обьединение        # u = {1,2,3,5,8, 13, 21}
i = a.intersection(b)   # пересечение        # i = {8, 2, 5}
dl = a.difference(b)    #  разность a И b    # dl = {1,3}
dr = b.difference(a)    #  разность b И a    # dr = {13, 21}
# a обьединяем с b -> разность с пересечение a и b
q = a.union(b).difference(a.intersection(b)) # {1, 21, 3, 13}
