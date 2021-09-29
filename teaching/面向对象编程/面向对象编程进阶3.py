# @Time    : 
# @Author  : chen
#%%单继承案例分析1
class Animal:
    def __init__(self, name='动物', color='白色'):
        self.__name = name
        self.color = color

    def __test(self):
        print(self.__name)
        print(self.color)

    def test(self):
        print(self.__name)
        print(self.color)

class Dog(Animal):
    def dogTest1(self):
        # print(self.__name) #不能访问到父类的私有属性
        print(self.color)

    def dogTest2(self):
        #self.__test() #不能访问父类中的私有方法
        self.test()

A = Animal()
# print(A.__name) #程序出现异常，不能访问私有属性
print(A.color)
#A.__test() #程序出现异常，不能访问私有方法
A.test() #可通过test()方法间接调用私有变量
print("------分割线-----")
D = Dog(name = "小花狗", color = "黄色")
D.dogTest1()
D.dogTest2()
"""小结：
1.私有的属性，不能通过对象直接访问，但是可以通过方法访问
2.私有的方法，不能通过对象直接访问
3.私有的属性、方法，不会被子类继承，也不能被访问
4.一般情况下，私有的属性、方法都是不对外公布的，往往用来做内部的事情，起到安全的作用"""
#%% 多继承案例分析2
# 所谓多继承，即子类有多个父类，并且具有它们的特征
#coding=utf-8
class base(object):
    def test(self):
        print('----base test----')

# 定义一个父类
class A(base):
    def test(self):
        print('----A test----')

# 再定义一个父类
class B(base):
    def test(self):
        print('----B test----')

# 定义一个子类，继承自A、B
class C(A,B):
    pass

c = C()
c.test()
print(C.__mro__) #可以查看C类的对象搜索方法时的先后顺序