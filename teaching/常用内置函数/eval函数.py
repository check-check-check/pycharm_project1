# @Time    : 
# @Author  : chen
"""
eval函数的简介和语法：
eval()函数用来执行一个字符串表达式，并返回表达式的值。还可以把字符串转化为list、tuple、dict。
eval函数的语法：
eval(expression[,globals[,locals]])
参数：
expression：表达式。
globals：变量作用域，如果被提供，必须是一个字典对象。
locals：变量作用域，如果被提供，可以说任何映射对象。
"""
#%% 1. 字符串转换成列表：
a = "[1,2,3,4,5]"
b = eval(a)
print(b)
# a是字符串类型数据，b是列表类型数据
#%% 2. 字符串转换成字典 ：
a = '{"name":"guo","age":25}'
print(a, type(a))
b = eval(a)
print(b, type(b))
# a为字符串类型数据，b为字典类型数据
#%% 3. 字符串转换为元组：
a = "(1,2,3,4,5)"
print(eval(a), type(eval(a)))
# a的数据结构是字符串 b的数据结构是元组
#%% 4. eval()返回表达式的值：
x = 4
eval("3*x")
# 返回值为12
#%%
x = 10
g = {'a': 4}
eval("a+1",g)
# 返回值为  5
#%%
a = 10
b = 20
c = 30
g = {'a': 6, 'b': 8}
t = {'b': 100, 'c': 10}
eval('a+b+c', g, t)




