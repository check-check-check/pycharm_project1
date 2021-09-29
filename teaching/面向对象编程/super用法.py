# @Time    : 
# @Author  : chen
#%% super的介绍来看,其作用为返回一个代理对象作为代表调用父类或亲类方法
"""super()的主要用法有两种： 在单类继承中，其意义就是不需要父类的名称来调用父类的函数，因此当子类改为继承其他父类的时候，不需要
对子类内部的父类调用函数做任何修改就能调用新父类的方法。 比如："""
class base1:
    def __init__(self):
        print("base1 class")

class A(base1):
    def __init__(self):
        base1.__init__(self)

class B(base1):
    def __init__(self):
        super(B, self).__init__()
# 这里要注意的是由于super将传入self作为调用__init__默认的第一个变量，因此在声明的时候不需要显式表示self。

obj1 = A()
obj2 = B()
#%%多继承
"""而在多类继承中super()是必不可少的（多类继承是python的一大特色），super()的**__mro__变量**记录了方法解析搜索顺序，
既一个类的所有父类的调用顺序（MRO用来保证多类继承的时候各父类被逐一调用并只被调用一次）。例如："""
class base1:
    def __init__(self):
        print("base1 class")
class B(base1):
    def __init__(self):
        print('B')
        super(B, self).__init__()
        print('C')
class minin(base1):
    def __init__(self):
        print("minin")
        super(minin, self).__init__()
        print('D')

class C(B, minin):
    pass
obj1 = C()
C.__mro__    # 2. 方法解析顺序（MRO）： C -> B -> mixin -> base1
#%% 我们经常在类的继承当中使用super()， 来调用父类中的方法。
class A:
    def func(self):
        print('OldBoy')
class B(A):
    def func(self):
        super().func()
        print('LuffyCity')
A().func()
B().func()
#%% 如果不使用super的话，想得到相同的输出结果，还可以这样写B的类：
class B(A):
    def func(self):
        A.func(self)
        print('LuffyCity')
B().func()
"""
这样能实现相同的效果，只不过传了一个self参数。那为什么还要使用super()呢？
那我看看有这样的一个继承关系的类（钻石继承）：
      Base
      /  \
     /    \
    A      B
     \    /
      \  /
       C
"""
#%%先看一下案例
# 代码是这样的：
class Base:
    def __init__(self):
        print('Base.__init__')
class A(Base):
    def __init__(self):
        Base.__init__(self)
        print('A.__init__')
class B(Base):
    def __init__(self):
        Base.__init__(self)
        print('B.__init__')
class C(A, B):
    def __init__(self):
        A.__init__(self)
        B.__init__(self)
        print('C.__init__')
C()
"""注意到：每个子类都调用父类的__init__方法，想把所有的初始化操作都做一遍，但是出现了一个问题，Base类的__init__方法被调用了两次，这是
多余的操作，也是不合理的。"""
# 那我们改写成使用super()的写法：
print(''.center(40,'-'))
class Base:
    def __init__(self):
        print('Base.__init__')
class A(Base):
    def __init__(self):
        super().__init__()
        print('A.__init__')
class B(Base):
    def __init__(self):
        super().__init__()
        print('B.__init__')
class C(A, B):
    def __init__(self):
        super().__init__()
        print('C.__init__')
C()
print(C.__mro__)
#%% super([type[, object-or-type]])
# 返回一个代理对象，该对象将方法调用委托给类的父类或兄弟类。这对于访问类中已重写的继承方法非常有用
# super是一个类，实例化之后得到的是一个代理的对象，而不是得到了父类，并且我们使用这个代理对象来调用父类或者兄弟类的方法。
# super() -> same as super(__class__, <first argument>)
# super(type) -> unbound super object
# super(type, obj) -> bound super object; requires isinstance(obj, type)
# super(type, type2) -> bound super object; requires issubclass(type2, type)
# 可见super至少需要一个参数，并且类型需要是类。
print(super(C))
# print(super()) #不传参数的会报错。只传一个参数的话是一个不绑定的对象，不绑定的话也就没什么用了
# 在定义类当中可以不写参数，Python会自动根据情况将两个参数传递给super。
class C(A, B):
    def __init__(self):
        print(super())
        super().__init__()
        print('C.__init__')
C()
# 所以我们在类中使用super的时候参数是可以省略的。
#%%第三种用法， super(type, obj) 传递一个类和对象，得到的是一个绑定的super对象。这还需要obj是type的实例，可以不是直接的实例，
# 是子类的实例也行。
a = A()
print(super(A))
print(super(A, a))
print(super(Base, a))
#%%第三种用法， super(type, type2)传递两个类，得到的也是一个绑定的super对象。这需要type2是type的子类
print(super(Base, A))
print(super(Base, B))
print(super(Base, C))
#%% 接下来我们就该说说查找顺序了，两个参数，是按照哪个参数去计算MRO呢？
# 我们将C类中的super的参数填写上，并且实例化，看看输出的结果。
class C(A, B):
    def __init__(self):
        super(C, self).__init__()
        print('C.__init__')
print(C())
# 看结果和之前super没填参数的结果是一样的。那我们将super的第一个参数改为A：
class C(A, B):
    def __init__(self):
        super(A, self).__init__()
        print('C.__init__')
print(C())
print(C.mro())
# 这是因为Python是按照第二个参数来计算MRO，这次的参数是self，也就是C的MRO。在这个顺序中跳过一个参数（A）找后面一个类（B），执行他的方法。

#%%再看一个综合案例
# class A():
#     def go(self):
#         print ("go A go!")
#     def stop(self):
#         print ("stop A stop!")
#     def pause(self):
#         raise Exception("Not Implemented")
# class B(A):
#     def go(self):
#         super(B, self).go()
#         print ("go B go!")
# class C(A):
#     def go(self):
#         super(C, self).go()
#         print ("go C go!")
#     def stop(self):
#         super(C, self).stop()
#         print ("stop C stop!")
# class D(B,C):
#     def go(self):
#         super(D, self).go()
#         print ("go D go!")
#     def stop(self):
#         super(D, self).stop()
#         print ("stop D stop!")
#     def pause(self):
#         print ("wait D wait!")
# class E(B,C):
#     pass
# a = A()
# b = B()
# c = C()
# d = D()
# e = E()
# # 说明下列代码的输出结果
# a.go()
# print('--------')
# b.go()
# print('--------')
# c.go()
# print('--------')
# d.go()
# print('--------')
# e.go()
# print('--------')
# a.stop()
# print('--------')
# b.stop()
# print('--------')
# c.stop()
# print('--------')
# d.stop()
# print('--------')
# e.stop()
# print(D.mro())
# a.pause()
# b.pause()
# c.pause()
# d.pause()
# e.pause()