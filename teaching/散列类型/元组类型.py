# @Time    : 
# @Author  : chen

# Python 的元组与列表类似，不同之处在于元组的元素不能修改。
# 元组使用小括号()，列表使用方括号[]。
letters = ('a', 'b', 'c', 'd', 'e', 'f', 'g')
print(letters[0])  # 输出 'a'
print(letters[0:3])  # 输出一组 ('a', 'b', 'c')

# %%1 创建元组
tup1 = ('baidu', 'google', 12, 34)
tup2 = (1, 2, 3, 4, 5)
tup3 = "a", "b", "c", "d"  # 小括号可以省咯
tup4 = (1,)
tup4_1 = 1,
tup4_2 = (1)
print(tup4 == tup4_1)
print(tup4 == tup4_2)
# 创建空元组
tup5 = ()

# 查看tup4和tup3的类型
print(tup3, type(tup3))
print(tup4, type(tup4))
print(tup5, type(tup5))

# %%2 访问元组
tup1 = ('baidu', 'google', 1, 2)
tup2 = (1, 2, 3, 4, 5, 6, 7)
print(tup1[0:2])
print(tup2[1:4])
# %%3 修改元组
'''元组中的值一旦定义就不能修改，但是我们可以通过元组与元组之间的连接关系来对元组进行修改
注意： 以下修改元组属于非法操作，因为元组不支持通过索引列来修改，只能对元组进行复制和连接操作
tup1[0] = 100 （不能进行此操作）'''
tup1 = ('baidu', 'google', 1, 2)
tup2 = (1, 2, 3, 4, 5, 6, 7)
print(tup1 + tup2)
# %%4 删除元组
# 由于元组的不可修改性，所以元组中的元素值是不允许删除的，但我们可以使用 del 语句来删除整个元组，
tup1 = ('baidu', 'google', 1, 2)
print(tup1)
del tup1
# print ("删除后的元组 tup : ")
# print (tup1)

# %%元组运算符
'''与字符串一样，元组之间可以使用 + 号和 * 号进行运算。这就意味着他们可以组合和复制，
运算后会生成一个新的元组。总而言之对整个元组进行一些运算后就会生成一个新的元组。'''
# 求元组tup1的长度
tup1 = ('baidu', 'google', 1, 2)
print(len(tup1))

# 连接元组:两个甚至对个元组的连接使用 + 连接符
tup1 = (1, 2, 3)
tup2 = (4, 5, 6)
tup3 = (7, 8, 9)
print(tup1 + tup2 + tup3)

# 复制元组
tup1 = ('abc')
# 元组复制需要加上分隔符后面复制的内容就按照分隔符分隔开
print(tup1 * 3)
print((tup1,) * 3)

# 判断元素:判断元组中元素是否存在使用关键字 in 进行判断，判断结果返回布尔值
tup1 = ('abc')
print('a' in tup1)

# 元组中指定位置元素访问
content = ('hello', 'world', '!')
print(content[1:])
print(content[-1])

# 元组内置函数
tuple1 = ('hello', 'world', '!')
# 计算元组元素个数。
print(len(tuple1))
# 返回元组中元素最大值。
print(max(tuple1))
# 返回元组中元素最小值。
print(min(tuple1))
# 将列表转换为元组。
# tuple(list)
