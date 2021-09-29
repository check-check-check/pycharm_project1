# @Time    : 
# @Author  : chen
"""python 类有多继承特性，如果继承关系太复杂，很难看出会先调用那个属性或方法。
为了方便且快速地看清继承关系和顺序，可以用__mro__方法来获取这个类的调用顺序。"""
#%% 类方法__mro__(method resolution order)，即解析方法调用的顺序
#%%举例
class X(object): pass
class Y(object): pass
class A(X, Y): pass
class B(Y): pass
class C(A, B): pass
print(C.__mro__)

#%% 类的__bases__属性:通过该属性可以查看该类的所有直接父类，该属性返回所有直接父类组成的元组。注意是直接父类！
print(C.__bases__)
print(A.__bases__)
print(B.__bases__)

# %% 对象的__class__属性（指明了所属类型）
print([].__class__)
print(().__class__)
print(C().__class__)