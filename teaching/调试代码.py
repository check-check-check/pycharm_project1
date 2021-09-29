# @Time    : 
# @Author  : chen
a=input('输入：')
print(a, type(a))



#%% reduce()函数在库functools里，如果要使用它，要从这个库里导入。

from functools import reduce
def add(x, y):
    return x + y
print(reduce(add, [1,2,3,4,5]) )  # 计算列表和：1+2+3+4+5
print(reduce(lambda x, y: x+y, [1,2,3,4,5]))  # 使用 lambda 匿名函数
#%%
from functools import reduce
print(reduce(lambda x, y: x * 10 + y, [1 , 2, 3, 4, 5]))
#%%
from functools import reduce
scientists =({'name':'Alan Turing', 'age':105, 'gender':'male'},
             {'name':'Dennis Ritchie', 'age':76, 'gender':'male'},
             {'name':'Ada Lovelace', 'age':202, 'gender':'female'},
             {'name':'Frances E. Allen', 'age':84, 'gender':'female'})
def group_by_gender(accumulator , value):
    accumulator[value['gender']].append(value['name'])
    return accumulator
grouped = reduce(group_by_gender, scientists, {'male':[], 'female':[]})
print(grouped)
#%%
from functools import reduce
scientists =({'name':'Alan Turing', 'age':105, 'gender':'male'},
             {'name':'Dennis Ritchie', 'age':76, 'gender':'male'},
             {'name':'Ada Lovelace', 'age':202, 'gender':'female'},
             {'name':'Frances E. Allen', 'age':84, 'gender':'female'})
grouped = reduce(lambda acc, val: {**acc, **{val['gender']: acc[val['gender']]+ [val['name']]}}, scientists, {'male':[], 'female':[]})
print(grouped)
#%%
import  itertools
scientists =({'name':'Alan Turing', 'age':105, 'gender':'male'},
             {'name':'Dennis Ritchie', 'age':76, 'gender':'male'},
             {'name':'Ada Lovelace', 'age':202, 'gender':'female'},
             {'name':'Frances E. Allen', 'age':84, 'gender':'female'})
grouped = {item[0]:list(item[1])
           for item in itertools.groupby(scientists, lambda x: x['gender'])}
print(grouped)
#%%
from functools import reduce
scientists =({'name':'Alan Turing', 'age':105},
             {'name':'Dennis Ritchie', 'age':76},
             {'name':'John von Neumann', 'age':114},
             {'name':'Guido van Rossum', 'age':61})
def reducer(accumulator , value):
    sum = accumulator['age'] + value['age']
    return sum
total_age = reduce(reducer, scientists)
print(total_age)
#%%
from functools import reduce
scientists =({'name':'Alan Turing', 'age':105, 'gender':'male'},
             {'name':'Dennis Ritchie', 'age':76, 'gender':'male'},
             {'name':'Ada Lovelace', 'age':202, 'gender':'female'},
             {'name':'Frances E. Allen', 'age':84, 'gender':'female'})
def reducer(accumulator , value):
    sum = accumulator + value['age']
    return sum
total_age = reduce(reducer, scientists, 0) #reduce 有三个参数， 第三个参数是初始值的意思，是可有可无的参数。
print(total_age)
#%%
def f(x,day):
   day -= 1
   if day == 0:
      return x
   x = (x+1) * 2
   return f(x,day)
res = f(1,10)
print(res)


#%%



#%%
def selection_sort(arr):

    """选择排序"""
    # 第一层for表示循环选择的遍数
    for i in range(len(arr) - 1):
        # 将起始元素设为最小元素
        min_index = i
        # 第二层for表示最小元素和后面的元素逐个比较
        for j in range(i + 1, len(arr)):
            if arr[j] < arr[min_index]:
                # 如果当前元素比最小元素小，则把当前元素角标记为最小元素角标
                min_index = j
        # 查找一遍后将最小元素与起始元素互换
        arr[min_index], arr[i] = arr[i], arr[min_index]
    return arr
selection_sort([11, 99, 33, 69, 77, 88, 55, 11, 33, 36, 39, 66, 44, 22])
# 返回结果 [11, 11, 22, 33, 33, 36, 39, 44, 55, 66, 69, 77, 88, 99]
#%%
def selection_sort(arr):
    """选择排序"""
    # 第一层for表示循环选择的遍数
    for i in range(len(arr) - 1):
        # 将起始元素设为最大元素
        max_index = i
        # 第二层for表示最大元素和后面的元素逐个比较
        for j in range(i + 1, len(arr)):
            if arr[j] > arr[max_index]:
                # 如果当前元素比最大元素大，则把当前元素角标记为最大元素角标
                max_index = j
        # 查找一遍后将最大元素与起始元素互换
        arr[max_index], arr[i] = arr[i], arr[max_index]
    return arr
selection_sort([11, 99, 33, 69, 77, 88, 55, 11, 33, 36, 39, 66, 44, 22])
# %% 面向过程
l1 = {'name': 'alex', 'age': 10}
def fun(dic):
    return dic['name'], dic['age']
fun(l1)