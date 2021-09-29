# @Time    : 
# @Author  : chen
#%% __import__：动态导入模块
# 如果一个模块经常变化就可以使用 __import__() 来动态载入
__import__('os') #等价于：import os
#%% isinstance：判断对象是否是类或者类型元组中任意类元素的实例
print( isinstance(1,int))
print( isinstance(1,str))
print( isinstance(1,(int,str)))

#%% issubclass：判断类是否是另外一个类或者类型元组中任意类元素的子类
print(issubclass)#判断类是否是另外一个类或者类型元组中任意类元素的子类
print(issubclass(bool,int))
print(issubclass(bool,str))
print(issubclass(bool,(str,int)))
#%% hasattr：检查对象是否含有属性
# 定义类A
class Student:
    def __init__(self, name):
        self.name = name

s = Student('Aim')
print(hasattr(s, 'name'))  # a含有name属性
print(hasattr(s, 'age'))  # a不含有age属性
#%% getattr：获取对象的属性值
#定义类Student
class Student:
    def __init__(self,name):
        self.name = name

print(getattr(s,'name')) #存在属性name
print(getattr(s,'age',6)) #不存在属性age，但提供了默认值，返回默认值
# print(getattr(s,'age')) #不存在属性age，未提供默认值，调用报错
#%% setattr：设置对象的属性值
class Student:
    def __init__(self, name):
        self.name = name
a = Student('Kim')
print(a.name)
print(setattr(a, 'name', 'Bob'))
print(a.name)
#%% delattr：删除对象的属性
#定义类A
class A:
    def __init__(self,name):
        self.name = name
    def sayHello(self):
        print('hello',self.name)
#测试属性和方法
a=A('Li')
print(a.name)
a.sayHello()
#删除属性
print(delattr(a,'name'))
# print(a.name)
#%% callable：检测对象是否可被调用
# 可调用对象，即任何可以通过函数操作符()来调用的对象
'''
callable(object)
作用：检查对象object是否可调用。如果返回True，object仍然可能调用失败；但如果返回False，调用对象ojbect绝对不会
成功。
'''
# 定义类B:类的实例对象前提是类中实现了__call__方法才是可调用的
class B:
    def __call__(self):
        print('instances are callable now.')
print(callable(B))  # 类B是可调用对象
b = B()  # 调用类B
print(callable(b)) # 实例b是可调用对象
b() # 调用实例b成功
#%%
