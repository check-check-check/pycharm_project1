# @Time    : 
# @Author  : chen
#%%

name = set('sdd')
print(name)
set1=set(['abbcc','bbcce','deeff'])
print(set1)

#%% add--功能：增加集合元素

name = {'d', 's'}
name.add('d')
print(name)
# 返回结果：{'d', 's'}
name.add('sd')
print(name)
# 返回结果：{'sd', 'd', 's'}

#%%clear--功能：清空集合元素

name = {'d', 's'}
name.clear()
print(name)
# 返回结果：{}

#%%copy--功能：浅拷贝

name = {'sd', 'd', 's'}
li = name.copy()
print(li)

#%%difference--求差集

diff001=name.difference(li)
print(diff001)
diff002=name.difference()
print(diff002)


#%%difference--求差集

set1=set(['wang','li','zhou',123])
set2={'wang','123','hu'}
set3={'li','han'}
print(set1.difference(set2,set3))
print(set1-set2-set3)

#%%difference_update功能：删除当前set中的所有包含在 new set 里的元素

li = ('s', 'd')
name = {'sd', 'd', 's'}
name.difference_update(li)
print(name)
# 返回结果：{'sd'}

#%%discard功能：移除元素

name = {'sd', 'd', 's'}
print(name.discard('s'))
# 返回结果：name：{'sd', 'd'}

#%%intersection功能：取交集,建立新的set集合

li = ('s', 'd')
name = {'sd', 'd', 's'}
print(name.intersection(li))
print(name)
# 返回结果：{'d', 's'}

#%%intersection_update功能：取交集,更新原来的set集合

li = ('s', 'd')
name = {'sd', 'd', 's'}
name.intersection_update(li)
print(name)
# 返回结果：{'d', 's'}

#%%isdisjoint 功能：没有交集，返回True,否则,返回False

li = {'s', 'd'}
name = {'sd', 'd', 's'}
print(name.isdisjoint(li))

#%%issubset功能：判断是否是子集

li = {'s', 'd'}
name = {'sd', 'd', 's'}
print(name.issubset(li))  #判断name是不是li的子集
# 返回结果：False
print(li.issubset(name))  #判断li是不是name的子集
# 返回结果：True

#%%issuperset功能：判断是否是父集

li = {'s', 'd'}
name = {'sd', 'd', 's'}
print(name.issuperset(li))  #判断name是不是li的父集
# 返回结果：True
print(li.issuperset(name))  #判断li是不是name的父集
# 返回结果：False

#%%pop功能：用于随机移除一个元素

#这个函数随机返回一个元素值，然后把这个值删除，如果set为空，调用这个函数会返回Key错误
name = {'sd', 'd', 's'}
print(name.pop())
se1 = {'a','s','sb'}
print(se1.pop())

#%%remove功能：移除指定集合元素

name = {'sd','d','s'}
print(name.remove('s'))
print(name)
# 返回结果：name:{'sd', 'd'}

#%%symmetric_difference

#功能：去两个集合的差集，建立新的set集合对象
name = {'sd', 'd', 's'}
li = {'s', 'd'}
print(name.symmetric_difference(li))
# 返回结果：{'sd'}

#%%symmetric_difference_update

#功能：去两个集合的差集，更新原来的集合对象
name = {'sd', 'd', 's'}
li = {'s', 'd'}
print(name.symmetric_difference_update(li))
print(name)
# 返回结果：{'sd'}

#%%union功能：并集，创建新的对象

name = {'sd', 'd', 's'}
li = {'s', 'd','h'}
print(name.union(li))
# 返回结果：{'h', 's', 'd', 'sd'}

#%%update功能：更新已有集合

name = {'sd', 'd', 's'}
name.update('df')
print(name)
# 返回结果：{'sd', 'd', 'f', 's'}

#%%

print(len(name))
print('s' in name)
print('s' not in name)

#%%
pow(3,2) == 3**2
