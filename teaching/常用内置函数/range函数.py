# @Time    : 
# @Author  : chen
# range() 函数可创建一个整数列表，一般用在 for 循环中;格式：range(start, stop[, step])
# %%
from collections import Iterable

a = range(10)  # 这是一个可迭代对象
print(a, type(a), isinstance(a, Iterable))
# type()函数详解：https://www.cnblogs.com/ilovepython/p/11068850.html
# %%
a = range(2, 10)
print(list(a))
a = range(2, 10, 2)
print(list(a))
