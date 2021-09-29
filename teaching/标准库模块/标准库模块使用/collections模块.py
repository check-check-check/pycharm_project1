# @Time    : 
# @Author  : chen
"""
python提供的内置数据类型（int、float、str、list、tuple、dict）外，collections模块还提供了其他数据类型，
使用如下功能需先导入collections模块（import collections）：
计数器（counter）
有序字典（orderedDict）
默认字典（defaultdict）
可命名元组（namedtuple）
双向队列（deque）
"""
import collections

# %% 一、 计数器（Counter）：统计元素的个数，并以字典形式返回{元素：元素个数}
c = collections.Counter('abcdeabcdabcaba')
print(c)
print(c.most_common(2))
print(sorted(c, reverse=True))
print(''.join(sorted(c.elements())))
print(sum(c.values()))
print(c['a'])
# 修改计数器
for elem in 'shazam':
    # update counts from an iterable
    c[elem] += 1
print(c)
# 删除计数器中的元素
del c['b']
print(c['b'])
# 合并计数器
d = collections.Counter('simsalabim')
c.update(d)
print(c)
# 清空计数器
c.clear()
print(c)

# %% elements：返回一个迭代器，元素被重复多少次，在迭代器中就包含多少个此元素，所有元素按字母序排列，个数<1的不罗列
c = collections.Counter(a=2, b=1, c=3, d=-1)  # **kwargs参数
print(list(c.elements()))
# %% most_common：将元素出现的次数按照从高到低进行排序，并返回前N个元素，若多个元素统计数相同，按照字母顺序排列，
#  N若未指定，则返回所有元素
# %% update：增加元素的重复次数
c = collections.Counter(a=2, b=1, c=3, d=-1)  # **kwargs参数
print(c)
c.update('a')
print(c)
# %% subtract：减少元素重复次数
c = collections.Counter('which')
print(c)
c.subtract({'w': 2})
print(c)
# 从另一个计时器里减少元素个数
c.subtract(collections.Counter('watch'))
print(c)
# %% 二、有序字典（orderedDict）：继承了dict的所有功能，dict是无序的，orderedDict刚好对dict作了补充，记录了键值对插入的顺序，是有序字典
# python v3.6之前的版本dict是无序的，3.6版本之后（含v3.6）dict是有序的，目测为了兼容性以及100%有序性考虑，建议实现有序功能时使用orderedDict
import collections

dic = collections.OrderedDict({'name': 'Tom', 'age': 18, 'sex': 'boy'})
print(dic)
# %% 1. clear：清空字典
dic.clear()
print(dic)
# %% 2. popitem：有序删除，类似于栈，按照后进先出的顺序依次删除
import collections

dic = collections.OrderedDict({'name': 'Tom', 'age': 18, 'sex': 'boy'})
dic.popitem()
print(dic)
dic.popitem()
print(dic)
# %% 3. pop：删除指定键值对
import collections

dic = collections.OrderedDict({'name': 'Tom', 'age': 18, 'sex': 'boy'})
dic.pop('name')
print(dic)
# %% 4. move_to_end：将指定键值对移到最后位置
import collections

dic = collections.OrderedDict({'name': 'Tom', 'age': 18, 'sex': 'boy'})
dic.move_to_end('name')
print(dic)
# %% 5. setdefault：设置默认值，默认为None，也可指定值
import collections

dic = {'name': 'Tom', 'age': 18, 'sex': 'boy'}
dic = collections.OrderedDict(dic)
dic.setdefault('course')
print(dic)
dic.setdefault('grades', 100)
print(dic)
# %% 6. update：更新字典，有则更新，无则添加
import collections

dic = {'name': 'Tom', 'age': 18, 'sex': 'boy'}
dic.update({'grades': 100, 'age': 20})
print(dic)

# %%三、默认字典（defaultdict）：设置values默认类型，如list、tuple
import collections

# dic = {'name': 'Tom', 'age': 18, 'sex': 'boy'}
dic = collections.defaultdict(list)
dic['name'].append('English')
dic['name'].append('Chinese')
print(dic)
dic['age'].append(18)
dic['age'].append(20)
print(dic)

# %% 四、可命名元组（namedtuple）: 可通过名称访问元组中的元素，提高代码可读性
import collections

TupleName = collections.namedtuple('TupleName', ['a', 'b', 'c'])  # 通过namedtuple自定义一个TupleName类
obj = TupleName(11, 22, 33)  # 通过类创建对象obj
print(obj.a)
# 通过名称访问元组中的元素
print(obj.b)
print(obj.a * obj.c)

#%% 五、双向队列（deque）：类似于list，允许两端操作元素
# 1. append：从队列右侧添加元素
import collections
deq=collections.deque('abcd')
print(deq)
print(deq.append(11))
print(deq)

#%% 2.appendleft：从队列左侧添加元素
import collections
deq=collections.deque('abcd')
deq.appendleft(['efg'])
print(deq)
#%% 3.clear：清空队列
import collections
deq=collections.deque('abcd')
deq.clear()
print(deq)
#%%  4. count：统计队列中元素个数
import collections
deq=collections.deque('abcd')
print(deq.count('a'))
#%%  5.extend：从队列右侧扩展
import collections
deq=collections.deque('abc')
deq.extend(('d', 'e', 'f'))
print(deq)
#%% 6.extendleft：从队列左侧扩展
#%% 7.index：取元素索引位置
#%% 8.insert：在队列任意位置插入值
#%% 9. pop：从队列右侧移除值
#%% 10.popleft：从队列左侧移除值
#%% 11. remove：移除指定值
#%% 12.reverse：将队列中的元素反转
#%% 13. rotate：移动队列中的元素，若n<0，则将队列最左侧的元素依次移动至最右侧，反之，n>0，将队列最右侧元素移动至最左侧
import collections
deq=collections.deque('abcdef')
deq.rotate(2)
print(deq)
deq.rotate(-2)
print(deq)