# @Time    : 
# @Author  : chen
dict_oper = {
    '+': lambda x, y: x + y,
    '-': lambda x, y: x - y,
    '*': lambda x, y: x * y,
    '/': lambda x, y: x / y}
x=1
y=2
print(dict_oper.get('+')(x, y))