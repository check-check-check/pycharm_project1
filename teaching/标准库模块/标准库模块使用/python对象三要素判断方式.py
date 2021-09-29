# @Time    : 
# @Author  : chen
# Python中对象包含的三个基本要素，分别是：id(身份标识)、type(数据类型)和value(值)。
# 1.== ：是python标准操作符中的比较操作符，用来比较判断两个对象的value(值)是否相等
# 2. is：也被叫做同一性运算符，这个运算符比较判断的是对象间的唯一身份标识，也就是id是否相同
# 3. Type()：获取python对象的类型，用来判断类型是否相等

#%%例题1：
x = y = [4,5,6]
z = [4,5,6]
print(x is y, id(x), id(y))
print(x is z, id(x), id(z))
print(y is z, id(y), id(z))
print(x == y)
print(x == z)
#%%例题2：
a = 1
b = 1
print(a is b,id(a), id(b))
"""
注意：事实上Python 为了优化速度，使用了小整数对象池，避免为整数频繁申请和销毁内存空间。
而Python 对小整数的定义是 [-5, 257)，只有数字在-5到256之间它们的id才会相等，超过了这
个范围就不行了，同样的道理，字符串对象也有一个类似的缓冲池，超过区间范围内自然不会相等了。
"""
#%%
print(id(1888),type(id(1888)))
print(id(1888))
