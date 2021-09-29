# @Time    : 
# @Author  : chen
# 注释：id(object)函数----返回的是对象的“身份证号”，唯一且不变，但在不重合的生命周期里，
# 可能会出现相同的id值。此处所说的对象应该特指复合类型的对象(如类、list等)，
# 对于字符串、整数等类型，变量的id是随值的改变而改变的;
# CPython 中 id() 函数用于获取对象的内存地址。

# %% 赋值语句
# Python 中赋值语句不复制对象，而是在目标和对象之间创建绑定 (Bindings) 关系
a = [1, 2, 3]
b = a
print(a, id(a))
print(b, id(b))
# 变量 a 与 b id 相同，也就说明他们指向同一地址，b 重复的引用了 a 指向的这个对象
a.append(4)
b.append(5)
print(a, id(a))
print(b, id(b))

# %% 当我们想通过赋值来获得一个新的对象，# Python 给我们提供了一个方法 copy() ，
# 通过此方法赋值的方式称为浅拷贝或浅层拷贝。
a = [1, 2, 3]
b = a.copy()
print(a, id(a))
print(b, id(b))
a.append(4)
b.append(5)
print(a, id(a))
print(b, id(b))
# 这样我们会获得一个与 a 内容一致新变量，其在内存中分别指向两个地址。

# %%深拷贝,先看个例子：
a = [1, 2, [3, 4]]
b = a.copy()
print(a, id(a), id(a[2]))
print(b, id(b), id(a[2]))
a.append(5)
a[2].append(6)
b.append(7)
b[2].append(8)
print(a, id(a), id(a[2]))
print(b, id(b), id(a[2]))
'''b 只拷贝的最外层的内容，而内层的内容是直接引用的。另外，
像这种列表中引用另一个列表的的形式，被称为复合对象。'''
# %%深拷贝,再看个例子：
'''如果想将内层的内容也作为新变量的一部分，需要用到标准库 copy 中的 deepcopy() 方法，
通过此方法赋值的方式称为深拷贝或深层拷贝。'''
import copy

a = [1, 2, [3, 4]]
b = copy.deepcopy(a)
print(a, id(a), id(a[2]))
print(b, id(b), id(a[2]))
a.append(5)
a[2].append(6)
b.append(7)
b[2].append(8)
print(a, id(a), id(a[2]))
print(b, id(b), id(a[2]))
