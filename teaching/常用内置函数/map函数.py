# @Time    : 
# @Author  : chen
#%%
'''map() 会根据提供的函数对指定序列做映射。第一个参数 function 以参数序列中的每一个元素调用 function 函数，
返回包含每次 function 函数返回值的新列表。'''
def square(x) :
    return x ** 2
print(list(map(square, range(4))))
print(list(map(lambda x: x ** 2, [1, 2, 3, 4, 5]))) # 使用 lambda 匿名函数)
# 提供了两个列表，对相同位置的列表数据进行相加
print(list(map(lambda x, y: x + y, [1, 3, 5, 7, 9], [2, 4, 6, 8, 10])))
