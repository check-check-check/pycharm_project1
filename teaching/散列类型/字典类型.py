# @Time    : 
# @Author  : chen
#%%创建字典的五种方法

#方法一: 常规方法 .如果事先能拼出整个字典，则此方法比较方便
D1 = {'name':'Bob','age':40}
print(D1)
#方法二: 动态创建.如果需要动态地建立字典的一个字段，则此方法比较方便
D2 = {}
D2['name'] = 'Bob'
D2['age']  =  40
print(D2)
# 方法三:  dict--关键字形式
# 代码比较少，但键必须为字符串型。常用于函数赋值
D3 = dict(name='Bob',age=45)
print(D3)
# 方法四: dict--键值序列
# 如果需要将键值逐步建成序列，则此方式比较有用,常与zip函数一起使用
D4 = dict([('name','Bob'),('age',40)])
print(D4)
D4 = dict(zip(('name','age'),('bob',40)))
print(D4)
# 方法五: dict--fromkeys方法
# 如果键的值都相同的话,用这种方式比较好，并可以用fromkeys来初始化
D5 = dict.fromkeys(['A','B'],0)
print(D5)
# 如果键的值没提供的话，默认为None
D5 = dict.fromkeys(['A','B'])
print(D5)

#%%zip函数--使用zip()函数来可以把列表合并，并创建一个元组对的列表

lt1=[1,2,3]
lt2=[4,5,6]
lt3=zip(lt1,lt2)
#zip()是可迭代对象，使用时必须将其包含在一个list中，方便一次性显示出所有结果
print(id(lt3))
print(list(lt3))
print(id(lt3))
lt3=zip(lt1,lt2)
print(dict(lt3))

#%%

lt4=['dd','18','183']
lt5=['name','age','height']
a=zip(lt5,lt4)
print(dict(a))

#%% 字典中键值遍历方法

#%%方法1
D = {'x':1, 'y':2, 'z':3}
for key in D:
    print(key,D[key])
#%%方法2
# 字典items()方法以列表返回可遍历的(键, 值) 元组数组
D = {'x':1, 'y':2, 'z':3}
print(list(D.items()))
for key, value in D.items():
    print(key, value)
#%%方法3
# iterkeys方法已经被废除
# for key in D.iterkeys():
#     print(key,D[key])
#方法4
for value in D.values():
    print(value)
#方法5
# iteritems方法已经被废除
# for key, value in D.iteritems():
#     print(key, value)

#%%
D1 = {'name':'Bob','age':40}
D1.get('name1',100)


