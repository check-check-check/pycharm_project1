# @Time    : 
# @Author  : chen
# 继承的实现原理
# 菱形问题：在Python中，一个子类是可以同时继承多个父类的，这固然可以带来一个子类可以对多个不同父类加以重用的好处，
# 但也有可能引发著名的 Diamond problem菱形问题(或称钻石问题，有时候也被称为“死亡钻石”)，菱形其实就是对下面这种
# 继承结构的形象比喻：
"""     B
    A /   \ D     A类在顶部，B类和C类分别位于其下方，D类在底部将两者连接在一起形成菱形。
      \ C /
"""
# 这种继承结构下导致的问题称之为菱形问题：如果A中有一个方法，B和/或C都重写了该方法，而D没有重写它，那么D继承的是哪个
# 版本的方法：B的还是C的？如下所示:
#%%
class A(object):
    def test(self):
        print('from A')
class B(A):
    def test(self):
        print('from B')
class C(A):
    def test(self):
        print('from C')
class D(B,C):
    pass
obj = D()
obj.test() # 结果为：from B
#%% 继承原理
D.mro()
# 对于你定义的每一个类，Python都会计算出一个方法解析顺序(MRO)列表，该MRO列表就是一个简单的所有基类的线性顺序列表，
# python会在MRO列表上从左到右开始查找基类,直到找到第一个匹配这个属性的类为止。

#%% 组合
"""在一个类中以另外一个类的对象作为数据属性，称为类的组合。组合与继承都是用来解决代码的重用性问题。不同的是：继承是一种“是”
的关系，比如老师是人、学生是人，当类之间有很多相同的之处，应该使用继承；而组合则是一种“有”的关系，比如老师有生日，老师有
多门课程，当类之间有显著不同，并且较小的类是较大的类所需要的组件时，应该使用组合，如下示例"""
class Course:
    def __init__(self,name,period,price):
        self.name=name
        self.period=period
        self.price=price
    def tell_info(self):
        print('<%s %s %s>' %(self.name,self.period,self.price))

class Date:
    def __init__(self,year,mon,day):
        self.year=year
        self.mon=mon
        self.day=day
    def tell_birth(self):
       print('<%s-%s-%s>' %(self.year,self.mon,self.day))

class People:
    school='清华大学'
    def __init__(self,name,sex,age):
        self.name=name
        self.sex=sex
        self.age=age

#Teacher类基于继承来重用People的代码，基于组合来重用Date类和Course类的代码
class Teacher(People): #老师是人
    def __init__(self,name,sex,age,title,year,mon,day):
        super().__init__(name,age,sex)
        self.birth=Date(year,mon,day) #老师有生日
        self.courses=[] #老师有课程，可以在实例化后，往该列表中添加Course类的对象
    def teach(self):
        print('%s is teaching' %self.name)


python=Course('python','3mons',3000.0)
linux=Course('linux','5mons',5000.0)
teacher1=Teacher('lili','female',28,'博士生导师',1990,3,23)

# teacher1有两门课程
teacher1.courses.append(python)
teacher1.courses.append(linux)

# 重用Date类的功能
teacher1.birth.tell_birth()

# 重用Course类的功能
for obj in teacher1.courses:
    obj.tell_info()