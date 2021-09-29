# @Time    : 
# @Author  : chen
# object.__new__(cls[, ...]), 用于创建(传递进来的)类cls的新实例。__new__()是一个静态方法，该方法将实例被请求的类作为
# 第一个参数，将类调用时传递的参数作为剩下的参数。__new__()的返回值应该是新的对象实例。(通常是类cls的实例)。
"""
1. 一个类创建新实例的典型实现是使用super().__new__(cls[, ...])语句结合适当的参数来调用父类的__new__方法。如果有需要的话可以
在返回实例之前修改实例。
2. 如果__new__()返回类cls的实例，那么该实例的__init__()方法将会像__init__(self[, ...])这样被调用。其中self是新实例，其余的
参数是传递给__new__()的参数。
3. 如果__new__()没有返回类cls的实例，那么新实例的__init__()方法将不会被执行。
4. 使用__new__()方法主要是为了允许不可变类型（如int, str, tuple）的子类定制实例。在自定类时，也可以在元类(metaclass)中重写。"""
# %% 任何一个类都会继承一个object的基类，并继承基类的__new__方法。我们重构上面的A类的__new__函数
class A:
    def __init__(self, value):
        print("into __init__")
        self.value = value

    # def __new__(cls, *args, **kwargs):
    #     print("into __new__")
    #     return super(A, cls).__new__(cls)
    def __new__(cls, *args, **kwargs):
        print("into __new__")
        instance = object.__new__(cls) #等价于 instance = super(A, cls).__new__(cls)
        return instance
a = A(10)
# __new__()在__init__之前执行：
# 注意到：在调用__init__进行函数的初始化之前，类先调用了__new__方法，并且返回了一个instance对象，之后调用了函数的__init__方法。
# 注意对于__new__函数而言，其必须有放回值，且这个返回值为类的实例，否则无法进行实例的初始化。而__init__则不允许有返回值。

# %% __new__的作用
# （1）__new__方法主要是当你继承一些不可变的class时(比如int, str, tuple)， 提供给你一个自定义这些类的实例化过程的途径。
# 假如我们需要一个永远都是正数的整数类型:
class PositiveInteger(int):
    def __init__(self, value):
        super(PositiveInteger, self).__init__(self, abs(value))

obj1 = PositiveInteger(-3)
print(obj1)

#%%
class PositiveInteger1(int):
    def __new__(cls, value):
        return super(PositiveInteger1, cls).__new__(cls, abs(value))

i = PositiveInteger(-3)
print(i)
