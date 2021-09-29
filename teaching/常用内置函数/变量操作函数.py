# @Time    : 
# @Author  : chen
#%% globals：返回当前作用域内的全局变量和其值组成的字典
print(globals())
a = 10
print(globals()['a'])#多了一个a
#%% locals：返回当前作用域内的局部变量和其值组成的字典
def f():
    print('before define a ')
    print(locals())  # 作用域内无变量
    a = 1
    print('after define a')
    print(locals())  # 作用域内有一个a变量，值为1
f()
