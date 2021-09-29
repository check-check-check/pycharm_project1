# @Time    :
# @Author  : chen
"""__dict__属性总结
1.类__dict__属性中包括类属性，类方法（非系统默认的，修改过的__init__()等，自己写的静态非静态方法），包括它实例化对象的方法
2.对象的属性就是__init__方法中带有的属性，子类默认继承父类__init__时候，子类创建对象的属性与父类一致，取决于你是否重写__init__属性，你可以尝试在子类重写__init__方法，并修改属性
3.可以通过操作对象__dict__属性来获取对象的属性。有时候会用到"""

#%% 使用以下例子来说明__dict__属性
class A(object):
    a = 0
    name = None
    b = 1
    def __init__(self,name):
        self.a = 2
        self.b = 3
        self.name = name
    def test(self):
        print ('a normal func.')
class B(A):
    def test_B(self):
        print ('func named test_B')
obj = A('Tom')
obj1 = B('Jerry')
print("父类对象A的__dict__属性")
print(A.__dict__)
print(obj.__dict__)
print("子类对象B的__dict__属性")
print(B.__dict__)
print(obj1.__dict__)


# 子类对象额外再添加属性
print("子类对象B额外再添加属性")
obj1.age = 10
print(B.__dict__)
print(obj1.__dict__)
