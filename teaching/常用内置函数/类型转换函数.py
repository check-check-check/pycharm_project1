# @Time    : 
# @Author  : chen
# 常用类型转换函数介绍
# %% bool：根据传入的参数的逻辑值创建一个新的布尔值
print(bool())  # 未传入参数
print(bool(0))  # 数值0、空序列等值为False
print(bool(1))
# %% int：根据传入的参数创建一个新的整数
print(int())  # 不传入参数时，得到结果0
print(int(2.6))
# %% float：根据传入的参数创建一个新的浮点数
print(float(), float('3'))
# %% complex：根据传入参数创建一个新的复数
print(complex(3, 4))
print(complex('1+2j'))  # 传入字符串创建复数
# %% str：返回一个对象的字符串表现形式(给用户)
print(str(), str(None), str('abc'), str(123))
# %% bytearray：根据传入的参数创建一个新的字节数组，bytearray() 方法返回一个新字节数组。
# 这个数组里的元素是可变的，并且每个元素的值范围: 0 <= x < 256。
print(bytearray('中文', 'utf-8'))
# 寻找a中最长的连续‘1’是几个
a = [1, 0, 1, 1, 0, 0, 1, 1, 1]
print(bytearray(a))
print(max([len(i) for i in bytearray(a).split((b'\x00'))]))

# %% bytes：根据传入的参数创建一个新的不可变字节数组
print(bytes('中文', 'utf-8'))

# %% memoryview：根据传入的参数创建一个新的内存查看对象
v = memoryview(b'abcefg')
print(v[1], v[-1])

# %% ord：返回Unicode字符对应的整数
print(ord('a'))

# %% chr：返回整数所对应的Unicode字符
print(chr(97))

# %% bin：将整数转换成2进制字符串
print(bin(97))
# oct：将整数转化成8进制数字符串
# hex：将整数转换成16进制字符串
# %%
# tuple()：根据传入的参数创建一个新的元组
# list()：根据传入的参数创建一个新的列表
# dict()：根据传入的参数创建一个新的字典
# set()：根据传入的参数创建一个新的集合
# frozenset()：根据传入的参数创建一个新的不可变集合
# enumerate()：根据可迭代对象创建枚举对象
# range()：根据传入的参数创建一个新的range对象
# iter()：根据传入的参数创建一个新的可迭代对象
s = iter('abcd')
print(s)  # 字符串序列
print(next(s))
print(next(s))
print(next(s))
print(next(s))
# print(next(s))  # StopIteration报错

# %% slice()：根据传入的参数创建一个新的切片对象
"""语法：
class slice(stop)
class slice(start, stop[, step])"""
c1 = slice(5)
print(c1)  # 定义c1
c2 = slice(2, 5)  # 定义c2
print(c2)
c3 = slice(1, 10, 3)  # 定义c3
print(c3)
a = range(10)
print(list(a[c1]), list(a[c2]), list(a[c3]))


# %% super()：根据传入的参数创建一个新的子类和父类关系的代理对象
# 定义父类A
class A(object):
    def __init__(self):
        print('A.__init__')


# 定义子类B，继承A
class B(A):
    def __init__(self):
        print('B.__init__')
        super().__init__()

# super调用父类方法
b = B()
#%% object：创建一个新的object对象
a = object()
print(a)