# @Time    :
# @Author  : chen
#
#%%类中的变量访问
class variable:
    a = '我是类变量'

    def showvarible(self):
        b = '我是函数变量'
        print(variable.a)
        print(b)


variable().showvarible()

#%%我们还可以通过self去访问
class variable:
    a = '我是类变量'

    def showvarible(self):
        b = '我是函数变量'
        print(self.a)
        print(b)


variable().showvarible()
#%% 通过构造函数给定一个参数，类中可访问
class variable:

    def __init__(self, a):
        self.a = '我是类变量'

    def showvarible(self):
        b = '我是函数变量'
        print(self.a)
        print(b)


variable(1).showvarible()
