# @Time    : 
# @Author  : chen
"""isinstance() 函数是 python中的一个内置函数，主要用于检测变量类型，返回值是bool值 ，在python内置函数中，
与该函数相似的还有另外一个内置函数  type()。"""
"""
isinstance(object, classinfo)
参数：
object: 实例对象。
classinfo: 可以是直接或者间接类名、基本类型或者由它们组成的元组。
返回值：如果对象的类型与classinfo类型相同则返回
True，否则返回False
"""
# %%
a = 2
print(isinstance(a, int))  # 结果返回 True
print(isinstance(a, str))  # 结果返回 False
print(isinstance(a, (str, int, list)))  # 是元组中的一个，结果返回 True
"""isinstance()会认为子类是一种父类类型，考虑继承关系。
type()不会认为子类是一种父类类型，不考虑继承关系。"""
#%%


# %%
class Animation:
    pass
class Dog(Animation):
    pass
print(isinstance(Animation(), Animation))  # returns True
print(type(Animation()) == Animation)  # returns True
print(isinstance(Dog(), Animation))  # returns True
print(type(Dog()) == Dog)  # returns True
print(type(Dog()) == Animation)  # returns False