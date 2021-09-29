# @Time    : 
# @Author  : chen
# %% 题目1: 已知：name=['zhangsan','lisi','wngwu'],用map来处理字符串列表啊,把列表中所有人都变成11,比方:zhangsan_11.

name = ['zhangsan', 'lisi', 'wngwu']
# 匿名函数--隐式
m = map(lambda i: i + "_11", name)  # map()映射，第一个参数为函数，第二个参数为可迭代对象,返回一个可迭代对象
print(m, list(m))

# 自定义函数--显示
def fun(x):
    return x + '_11'

m = map(fun, name)
print(m, list(m))

"""另外,用map来处理下述l,然后用list得到一个新的列表,列表中每个人的名字都是_22结尾,l=[{'name':'alex'},{'name':'y'}]"""
l = [{'name': 'alex'}, {'name': 'y'}]

m = map(lambda dic: dic['name'] + '_22', l)
print(m, list(m))

# 或者：
def fun(dic):
    dic['name'] = dic['name'] + '_22'
    return dic
m = map(fun, l)
print(m, list(m))

# %%题目2：用filter来处理,得到股票价格大于20的股票名字，已知：shares={'IBM':36.6,'Lenovo':23.2,'oldboy':21.2,'ocean':10.2,}
shares = {'IBM': 36.6, 'Lenovo': 23.2, 'oldboy': 21.2, 'ocean': 10.2, }
print(shares.keys())
m = filter(lambda key: shares[key] > 20, shares)
print(m, list(m))
# 或者：
m = filter(lambda key: shares[key] > 20, shares.keys())
print(m, list(m))

# 或者：
m = filter(lambda value: value > 20, shares.values())
print(m, list(m))

"""
遍历shares和shares.keys()，结果其实是一样的
for i in shares.keys():
    print(i)
for i in shares:
    print(i)
"""

# %%题目3：
"""
(1).map来得出一个包含数字的迭代器，数字指的是：购买每支股票的总价格
(2).用filter过滤出，单价大于100的股票有哪些
(3).基于1的结果，用reduce来计算，购买这些股票总共花了多少钱（选做）
"""
portfolio = [
    {'name': 'IBM', 'shares': 100, 'price': 91.1},
    {'name': 'AAPL', 'shares': 50, 'price': 543.22},
    {'name': 'FB', 'shares': 200, 'price': 21.09},
    {'name': 'HPQ', 'shares': 35, 'price': 31.75},
    {'name': 'YHOO', 'shares': 45, 'price': 16.35},
    {'name': 'ACME', 'shares': 75, 'price': 115.65}]

# %%(1).map来得出一个包含数字的迭代器，数字指的是：购买每支股票的总价格
m = map(lambda dic: dic['shares'] * dic['price'], portfolio)
print(m, list(m))
# %%(2).用filter过滤出，单价大于100的股票有哪些
m = filter(lambda dic: dic['price'] > 100, portfolio)
print(m, list(m))
# %%(3).基于(1)的结果，用reduce来计算，购买这些股票总共花了多少钱（选做）
import functools
m = map(lambda dic: dic['shares'] * dic['price'], portfolio)
m = functools.reduce(lambda x, y: x * y, list(m))
print(m)

#%% 题目4：
"""
利用内置函数zip()，实现如下功能：
l1 = ['you',11,22,33]
l2 = ['are',11,22,33]
l3 = ['good',11,22,33]
l4 = ['boy',11,22,33]
请获取字符串s = 'you_are_good_boy'
"""
l1 = ['you',22,33]
l2 = ['are',11,22,33]
l3 = ['good',11,22,33]
l4 = ['boy',11,22,33]
s=zip(l1,l2,l3,l4)
# print(list(s))
print('_'.join(list(s)[0]))

