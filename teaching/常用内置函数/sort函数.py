# @Time    : 
# @Author  : chen
# sort 是应用在 list 上的方法
# 简单的列表排序
l = [1, 7, 4, 9, 2, 3, 5, 0, 8, 6]
l.sort(reverse=True)
print(l)
l.sort()
print(l)

# 类表中嵌套其他数据类型，如字典
a = [{'id':1,'name':'小明'}, {'id':3,'name':'小红'},{'id':2,'name':'老王'}]
# 根据字典的key值id进行降序排序并输出排序后的列表。
def function(date):
    print(date)
    print(date['id'])
    return date['id']
a.sort(key=function)
print(a)

##################简化版#################
a = [{'id':1,'name':'小明'}, {'id':3,'name':'小红'},{'id':2,'name':'老王'}]
a.sort(key=lambda keys: keys['id'])
print(a)
a = [{'id':1,'name':'小明'}, {'id':3,'name':'小红'},{'id':2,'name':'老王'}]
s = sorted(a, key=lambda keys: keys['id'])
print(s)


# 按照字符串排序
StrList = ['fb', 'bx', 'csw', 'qb', 'qqa', 'eeeed']
# 一般列表排列，但是大写在前，小写在后！！
StrList.sort()
print(StrList)  ##字符串列表是按照第一个字符的大小排序的
##输出：['Fast', 'Smooth', 'fast', 'is', 'is', 'smooth']

# 忽略大小写，按abcd顺序
StrList.sort(key=str.lower)
print(StrList)  ##输出：['Fast', 'fast', 'is', 'is', 'Smooth', 'smooth']

StrList.sort(key=str.upper)
print(StrList)
# 按照字符串长度排序
StrList.sort(key=len)
print(StrList)  ##输出：['is', 'is', 'fast', 'Fast', 'Smooth', 'smooth']

StrList.sort(key=len, reverse=True)  # 反序
print(StrList)  ##输出：['Smooth', 'smooth', 'fast', 'Fast', 'is', 'is']

# 假设用元组保存每一个学生的信息，包括学号，姓名，年龄。用列表保存所有学生的信息。
list1 = [(8, 'Logan', 20), (2, 'Mike', 22), (5, 'Lucy', 19)]
list1.sort()
print(list1)

list1 = [(8, 'Logan', 20), (2, 'Mike', 22), (5, 'Lucy', 19)]
list2=sorted(list1)
print(list2)
print(list1)


# sorted()方法
# a = [{'id':1,'name':'小明'}，{'id':3,'name':'小红'}，{'id':2,'name':'老王'}]
# 根据字典的key值id进行降序排序并输出排序后的列表。

a = [{'id': 1, 'name': '小明'}, {'id': 3, 'name': '小红'}, {'id': 2, 'name': '老王'}]

s = sorted(a, key=lambda keys: keys['id'])
print(s)
print(a)

# 对于同样一个无序的列表a，调用sorted(a)，对a进行排序后返回一个新的列表，而对a不产生影响。
# 对于一个无序的列表a，调用a.sort()，对a进行排序后返回a，sort()
# 函数修改待排序的列表内容。