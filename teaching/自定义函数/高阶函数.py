# @Time    : 
# @Author  : chen
"""高阶函数：一个函数可以作为参数传给另外一个函数，或者一个函数的返回值为另外一个函数（
若返回值为该函数本身，则为递归），满足其一则为高阶函数。"""


# %% 情况1：参数为函数
def bar():
    print("in the bar..")


def foo(func):
    func()
    print("in the foo..")


foo(bar)


# %%情况2：返回值为函数
def bar():
    print("in the bar..")


def foo(func):
    print("in the foo..")
    return bar


res = foo(bar)
res()
'''以上两个示例中，函数foo()为高阶函数，示例一中函数bar作为foo的参数传入，示例二中函数bar作为foo的返回值。
注：函数名（例如bar 、foo）-->其为该函数的内存地址；函数名+括号（例如 bar()、foo() )-->调用该函数。'''

# %%高阶函数-map、filter、reduce
# map函数接收的是两个参数，一个函数，一个序列，其功能是将序列中的值处理再依次返回至列表内。其返回值为一个迭代器对象
num = [1, 2, 3, 4, 5]


def square(x):
    return x ** 2


# map函数模拟
def map_test(func, iter):
    num_1 = []
    for i in iter:
        ret = func(i)
        # print(ret)
        num_1.append(ret)
    return num_1.__iter__()  # 将列表转为迭代器对象


# map_test函数
print(list(map_test(square, num)))
# map函数
print(list(map(square, num)))

# 当然map函数的参数1也可以是匿名函数、参数2也可以是字符串
print(list(map_test(lambda x: x.upper(), "amanda")))
print(list(map(lambda x: x.upper(), "amanda")))

# %% filter函数也是接收一个函数和一个序列的高阶函数，其主要功能是过滤。其返回值也是迭代器对象
names = ["Alex", "amanda", "xiaowu"]


# filter函数机制
def filter_test(func, iter):
    names_1 = []
    for i in iter:
        if func(i):  # 传入的func函数其结果必须为bool值，才有意义
            names_1.append(i)
    return names_1


# filter_test函数
print(filter_test(lambda x: x.islower(), names))
# filter函数
print(list(filter(lambda x: x.islower(), names)))

# %% reduce函数也是一个参数为函数，一个为可迭代对象的高阶函数，其返回值为一个值而不是迭代器对象
# reduce函数不是内置函数，而是在模块functools中的函数，故需要导入
from functools import reduce

nums = [1, 2, 3, 4, 5, 6]


# reduce函数的机制
def reduce_test(func, array, ini=None):  # ini作为基数
    if ini == None:
        ret = array.pop(0)
    else:
        ret = ini
    for i in array:
        ret = func(ret, i)
    return ret


# reduce_test函数，叠乘
print(reduce_test(lambda x, y: x * y, nums, 1))
# reduce函数，叠乘
print(reduce(lambda x, y: x * y, nums, 1))

