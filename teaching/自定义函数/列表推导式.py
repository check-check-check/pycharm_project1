# @Time    : 
# @Author  : chen

'''python中列表推导式用于使用其他列表创建一个新列表。
其基本形式为： [表达式 for 变量 in 列表]'''

# %% 只有输出表达式和输入序列的基本列表推导式
# 例题1：想得到1-10的平方组成的list
list_1 = [x ** 2 for x in range(1, 11)]
print(list_1)

# %% 带有条件判断的列表推导式
# 例题2：想得到1-10中为偶数的平方组成的list
example = [i ** 2 for i in range(1, 11) if i % 2 == 0]
print(example)

# %% 多个输入序列的列表推导式
# 例题3：想得到多重嵌套中的数是2的倍数的平方组成的list
example2 = [[1, 2, 3], [4, 5, 6], [7, 8, 9], [10]]
example3 = [j ** 2 for i in example2 for j in i if j % 2 == 0]
print(example3)

# 例题4：想得到多重嵌套的list中一重嵌套中list长度大于1的list中的数为2的倍数的平方组成的list
example4 = [[1, 2, 3], [4, 5, 6], [7, 8, 9], [10]]
exmaple5 = [j ** 2 for i in example2 if len(i) > 1 for j in i if j % 2 == 0]
print(exmaple5)

# %% 例题5：用列表推导式求矩阵的转置
a = [[1, 2, 3, 4],
     [5, 6, 7, 8],
     [9, 10, 11, 12]]


def T(a):
    if len(a) == 0:  # 空矩阵
        return []  # 满足条件，即跳出
    l = len(a[0])
    for i in range(1, len(a)):  # 是不是一个矩阵
        if l != len(a[i]):
            return []  # 满足条件，即跳出
    return [[a[j][i] for j in range(len(a))] for i in range(len(a[0]))]


print(T(a))
# %% 例题6：用列表推导打赢乘法表
str1 = [str(j) + '*' + str(i) + '=' + str(i * j).center(2) + ' ' + ('\n' if i == j else '')
        for i in range(1, 10) for j in range(1, i + 1)]
print(str1)
print(''.join(str1))  # join连接字符串数组。将字符串、元组、列表中的元素以指定的字符(分隔符)连接生成一个新的字符串

# %% 例题7： 用列表推导式构字典
print({i: i ** 3 for i in range(1, 11) if i % 2 == 1})

list1 = ['zhang', 'er', 'gou']
for ind, content in enumerate(list1):
    print(ind, content)

feature = [[1, 1], [1, -1], [1, 2], [-1, 1], [-1, -2]]
label = [1, 4, 1, 2, 3]
list2 = [1, 2, 3, 4, 5]
# zip(feature, label, list3)  # 可以打包更多
# 用zip打包列表
for point, local in zip(feature, label):
    print('坐标({:d}, {:d})在第{:d}象限'.format(point[0], point[1], local))

# 反向迭代
print([it for it in reversed(list2)])
