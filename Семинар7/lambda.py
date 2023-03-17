operation = {'+': lambda x,y: x+y,
             '-': lambda x,y: x-y}
string = '3+2'
string = list(string)
print(string)

for i, item in enumerate(string):
    if string[i] in ['+','-']:
        print(operation.get(string[i])(int(string[i-1]), int(string[i+1])))
