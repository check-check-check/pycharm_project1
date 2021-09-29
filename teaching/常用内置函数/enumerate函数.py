# @Time    : 
# @Author  : chen
# enumerate() 枚举函数，用于将一个可遍历的数据对象(如列表、元组、字符串和字典)组合为一个索引序列，
# 同时列出数据和数据下标，一般用在 for 循环当中
#%% 例题1
seasons = ['apple', 'orange', 'purple', 'pear']
c = list(enumerate(seasons))
print(c)

b = list(enumerate(seasons, 1))
print(b)

seasons = {'x1':'apple', 'x2':'orange', 'x3':'purple', 'x4': 'pear'}
d = list(enumerate(seasons.values()))
d1 = list(enumerate(seasons.keys()))
print(d)
print(d1)

#%% 例题2
abc='abcdefg'
print(enumerate(abc))
print(list(enumerate(abc)))
for i in enumerate(abc):
    print(i)
for i,element in enumerate(abc,1):
    print(i,abc[i-1])

#%% 补充例题
# 如果要统计文件的行数，可以这样写：
filepath=r'G:\project\python-workplace\teaching\自定义函数\a.txt'
count = len(open(filepath, 'r').readlines())
print(count)
# 以上这种方法简单，但是可能比较慢，当文件比较大时甚至不能工作。可以利用enumerate()：
count = 0
for index, line in enumerate(open(filepath,'r')):
    count += 1
print(count)
