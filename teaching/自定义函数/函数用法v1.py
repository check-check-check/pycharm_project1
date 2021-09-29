# @Time    : 
# @Author  : chen
#%%编程方式无非就两种：面向对象和面向过程，不论是哪一种，它们都是编程的一种规范或者是如何编程的方法论。
# 面向对象---》类---》class
# 面向过程---》过程---》def
# 函数式编程---》函数---》def
# 函数和过程都是可以调用的实体，不同：过程就是没有返回值的函数而已，函数有返回值。

# 函数的作用：1.减少重复代码 2.使程序变的可扩展 3.使程序变得易维护

# 定义一个函数

def func1(x):
    """testing1"""
    print('in the func1')
    return y
# 定义过程
def func2():
    '''testing2'''
    print('in the func2')
# 调用函数
x=func1()

#调用过程
y=func2()

print('from func1 return is %s' %x)
print('from func2 return is %s' %y)
