colors = {'red', 'green', 'blue'}
print(colors) # {'red', 'green', 'blue'}
colors.add('red')
print(colors)# {'red', 'green', 'blue'}
colors.add('grey')#
print(colors)# {'red', 'green', 'blue', 'grey'}
colors.remove('red')
print(colors)# {'green', 'blue', 'grey'}
colors.remove('red')# KeyError: 'red'
colors.discard('red')# ok
print(colors)# {'green', 'blue', 'grey'}
colors.clear()# { }
print(colors)# set()