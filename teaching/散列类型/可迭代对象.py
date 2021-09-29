# @Time    : 
# @Author  : chen
# 说明：我们已经知道可以对list、tuple、dict、set、str等类型的数据使用
# for...in...的循环语法从其中依次拿到数据进行使用，我们把这样的过程称为遍历，也叫迭代。
# 把可以通过for...in...这类语句迭代读取一条数据供我们使用的对象称之为可迭代对象（Iterable）。
#%% 1.可迭代对象
# 字符串
str = 'ab cd'
for i in str:
    print(i)
# 列表
list1 = list(str)
print(list1)
for i in list1:
    print(i)
# 集合
set1 = set(str)
print(set1)
for i in set1:
    print(i)
# 元组
tuple1 = tuple(str)
print(tuple1)
for i in tuple1:
    print(i)
# 字典
dict1 = dict(zip(list1, list1))
print(dict1)
for key in dict1:  # 默认情况下，dict迭代的是key
    print(key, dict1[key])
for value in dict1.values():
    print(value)
for key, value in dict1.items():
    print(key, value)

#%% 2. 如何判断一个对象是否可以迭
# 可以使用 isinstance() 判断一个对象是否是 Iterable 对象：
from collections.abc import Iterable

print(isinstance(str, Iterable))
print(isinstance(list1, Iterable))
print(isinstance(tuple1, Iterable))
print(isinstance(dict1, Iterable))

#%% 3. 可迭代对象的本质
'''解释：我们分析对可迭代对象进行迭代使用的过程，发现每迭代一次（即在for...in...中每循环一次）
都会返回对象中的下一条数据，一直向后读取数据直到迭代了所有数据后结束。那么，在这个迭代
过程中就应该有一个“记录员”去记录每次访问到了第几条数据，以便每次迭代都可以返回下一条数据。
我们把这个能帮助我们进行数据迭代的“记录员”称为迭代器(Iterator)。可迭代对象的本质就是可以
向我们提供一个这样的“记录员”即迭代器帮助我们对其进行迭代遍历使用。'''
'''另外：可迭代对象通过__iter__方法向我们提供一个迭代器，我们在迭代一个可迭代对象的时候，
实际上就是先获取该对象提供的一个迭代器，然后通过这个迭代器来依次获取对象中的每一个数据。
那么也就是说，一个具备了__iter__方法的对象，就是一个可迭代对象。'''


class MyList(object):
    def __init__(self):
        self.container = []

    def add(self, item):
        self.container.append(item)

    def __iter__(self):
        pass
MyList1 = MyList()
MyList1.add(2)
MyList1.add(3)
MyList1.add(4)
print(MyList1.container)

from collections.abc import Iterable
print(isinstance(MyList1, Iterable))
#%% 4. iter()函数与next()函数
'''我们可以通过iter()函数获取这些可迭代对象的迭代器。
然后我们可以对获取到的迭代器不断使用next()函数来获取下一条数据。
iter()函数实际上就是调用了可迭代对象的__iter__方法。'''
li = [11, 22, 33, 44, 55]
li_iter = iter(li)
print(next(li_iter))
print(next(li_iter))
print(next(li_iter))
print(next(li_iter))
print(next(li_iter))
