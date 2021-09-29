# @Time    : 
# @Author  : chen
#%% all：判断可迭代对象的每个元素是否都为True值
print(all([1,2])) #列表中每个元素逻辑值均为True，返回True
print(all([0,1,2]))
print(all(()))#空元组
print(all({}))#空字典
#%% any：判断可迭代对象的元素是否有为True值的元素
print(any([1,2]))
print(any([0,1,2]))
print(any(()))
print(any({}))

#%% filter：使用指定方法过滤可迭代对象的元素
a = list(range(1,10)) #定义序列

def if_odd(x): #定义奇数判断函数
    return x%2==1
print(list(filter(if_odd,a)))

#%% map:使用指定方法去作用传入的每个可迭代对象的元素，生成新的可迭代对象
a = map(ord,'abcd')
print(list(a))

#%% next：返回可迭代对象中的下一个元素值
a = iter('abcd')
print(next(a))
print(next(a))
print(next(a))
print(next(a,4))
#传入default参数后，如果可迭代对象还有元素没有返回，则依次返回其元素值，如果所有元素已经返回，则返回default指
#定的默认值而不抛出StopIteration 异常

#%%reversed：反转序列生成新的可迭代对象
a = reversed(range(10)) # 传入range对象
print(list(a))
#%% sorted：对可迭代对象进行排序，返回一个新的列表
a = ['a','b','d','c','B','A']
print(sorted(a))  # 默认按字符ascii码排序
print(sorted(a,key = str.lower)) # 转换成小写后再排序，'a'和'A'值一样，'b'和'B'值一样
#%% zip：聚合传入的每个迭代器中相同位置的元素，返回一个新的元组类型迭代器
x = [1,2,3] #长度3
y = [4,5,6,7,8] #长度5
print(list(zip(x,y))) # 取最小长度3