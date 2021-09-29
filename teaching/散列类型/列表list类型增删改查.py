# @Time    : 
# @Author  : chen
#%% 1.增加：往列表里增加元素:

# 创建列表
service = ['http','ssh','ftp']
##用连接的方式
print(service + ['firewalld'])
#append:追加一个元素到列表中
service.append('firewalld')
print(service)
# extend:拉伸 追加多个元素到列表中
service.extend(['mysql','firewalld'])
print(service)
#在指定索引位置插入元素  ##在第二个元素的位置插入samba作为第二个元素
service.insert(1,'samba')
print(service)

#%%2.删除：

# 创建列表
service = ['http','ssh','web','ftp']
##弹出最后一个元素
a1=service.pop()
a2 = service.pop(0)  ##弹出第1个元素  ###可以将其赋值
print(a1,a2)
print(service)
##指定删除对象的名字  ##直接删除，不能将其赋值   ##不能指定序号，只能指定要删除对象的

a3=service.remove('ssh')
print(a3)
print(service)

del service   ##直接删除整个列表
print(service)

#%%3.赋值：

# 创建列表
service = ['http','ssh','ftp']
##通过索引 重新赋值
service[0] = 'mysql'
print(service)
##通过切片给前两个元素重新赋值
service[:2] = ['samba','iscsi']
print(service)

#%%4.查看：

# 创建列表
service = ['http','ssh','ssh','ftp']
# 查看出现的次数
print(len(service))
print(service.count('ssh'))
# 查看指定元素的索引值
# 最小索引值
service.index('ssh')
# 从1-3中查找【第二个元素和第三个元素之间】【不取上限】
service.index('ssh',1,3)

#%%5.排序：

# sort 排序 对字符串排序不区分大小写
names = ['alice','Bob','coco','Harry']
# 按照ASCLL排序   ###先排序首字母为大写的，再排序首字母是小写的
names.sort()
print(names)

###对字符串排序不区分大小写，相当于将所有元素转换为小写，再排序
names.sort(key=str.lower)
print(names)
###相当于将所有元素转换为大写，再排序
names.sort(key=str.upper)
print(names)
