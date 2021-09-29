# @Time    : 
# @Author  : chen
"""面向对象的三大特征：封装，继承和多态"""
# 封装的意思是说对象数据和操作该数据的指令都是对象自身的一部分，封装能够实现尽可能对外部世界隐藏数据
# 继承的思想是当你定义了一个对象后，你可以扩展该对象，创建一些新的对象
# 多态性是指以不同的方式、不同的类来实现一个公共接口的能力
#%% 1._init__方法:构造函数，在创建实例对象时自动执行
class Student:
    def __init__(self, name='小明'): #有默认值
        self.name = name

    def output(self):
        print("这个学生的名字是", self.name)
s1 = Student()
s2 = Student('李雷')
s1.output()
s2.output()
#%% 2.self 的作用及绑定概念：
"""Python严格要求方法需要有实例才能被调用，这种限制其实就是Python所谓的绑定概念。python类的定义中是通过传入self来实现
绑定的。如下例子，直接使用类对象来调用output方法就出错了，必须要先创建实例对象才可以。这里的self指已创建的实例对象"""
Student.output()
#%% 如果类定义某个函数中没有self参数，则类对象也可以直接调用此函数.
class Student:
    def __init__(self,name='小明',score=80):
        self.name = name
        self.score = score
    def output(self):
        print("这个学生的名字是",self.name)
    def output_grad():
        print("这个学生的成绩是80")
Student.output_grad()
# 但直接使用实例对象调用output_grad()会出错，这是因为实例对象默认传入参数self（即实例对象自身）。
s3 = Student()
s3.output_grad()
#%% 3.Python公有和私有（伪私有）：Python定义私有函数（或变量）时，使用的方法是在函数/变量名前加两个下划线“__”。
class Student:
    def __init__(self, name='小明', score=80, age=15):
        self.name = name
        self.score = score
        self.__age = 15

    def getAge(self):
        return self.__age
s3 = Student()
print(s3.name, s3.score)
# 可通过getAge()方法调用私有变量。
print(s3.getAge())
# 但是无法直接调用私有变量
print(s3.__age)

#%% 伪私有
# 之所以说python实现的是伪私有，是因为python是通过改变变量名来实现私有的，并不是真正的私有。Python在私有变量前会加上
# '_类名'作为新的变量名，故s3.__age调用就出错，使用s3._Student__age可正常获取__age的值:
print(s3._Student__age)

#%% 4.继承
# (1）如果子类重写了父类的方法就会将父类的方法覆盖掉
class Person:
    def __init__(self, name='小明', age=15):
        self.name = name
        self.age = 15
    def output(self):
        print(self.name, '的年纪是', self.age)

class Student(Person):
    def __init__(self, score=80):
        self.score = score

    def output(self):

        print(self.name, '的成绩是', self.score)
s5 = Student()
s5.output()
"""上例中，__init__方法被重写了，父类的__init__方法被覆盖，无法获取self.name和self.age信息。可以使用super()解决。如下例，
super()表示父类，super().__init__()表示调用父类的__init__()方法。"""
# output()方法也被重写覆盖了，所以输出的是成绩（子类），而不是年龄（父类）。
#%%
class Person:
    def __init__(self, name='小明', age=15):
        self.name = name
        self.age = 15
    def output(self):
        print(self.name, '的年纪是', self.age)

class Student(Person):
    def __init__(self, score=80):
        super().__init__()
        self.score = score

    def output(self):
        print(self.name, '的成绩是', self.score)
s5 = Student()
s5.output()
#%% (2) 多重继承：将没有继承关系的类对象放在一起（组合）
class Turtle:
    def __init__(self, x):
        self.num = x
class Fish:
    def __init__(self, y):
        self.num = y

class Pool:
    def __init__(self, x, y):
        self.turtle = Turtle(x)
        self.fish = Fish(y)
    def print_num(self):
        print("水池里共有乌龟 %d 只，小鱼 %d 条！" % (self.turtle.num, self.fish.num))

p1 = Pool(3,100)
p1.print_num()
#%% 5. 多态
"""多态的好处就是，当我们需要传入更多的子类，例如新增 Student、Teacher等时，我们只需要继承 Person 类型就可以了，而 output 方法
既可以不重写（使用Person的），也可以重写一个特有的。这就是多态的意思。"""
"""Student可以看作是Person, Person不能看作是Student. 调用方只管调用，不管细节，而当我们新增一种Person的子类时，只要确保新方法
编写正确，而不用管原来的代码。这就是著名的“开闭”原则 
对扩展开放（Open for extension）：允许子类重写方法函数 
对修改封闭（Closed for modification）：不重写，直接继承父类方法函数 """
class Person:
    def __init__(self, name='小明', age=15):
        self.name = name
        self.age = 15
    def output(self):
        print(self.name + '的年纪是', self.age)

class Student(Person):
    def __init__(self, score=80):
        super().__init__() # 继承父类的的构造函数（属性）
        self.score = score

    def output(self):
        super().output() # 继承父类的的方法
        # print(self.name + '学生的成绩是', self.score)

class Teacher(Person):
    def __init__(self, name='王五', age=30, teachAge=10):
        self.name = name #重写父类的构造函数（属性）
        self.age = age
        self.teachAge = teachAge
    def output(self):#重写父类的方法
        print(self.name + '老师的教龄是', self.teachAge, '年')

p1 = Person()
s1 = Student()
t1 = Teacher()

p1.output()
s1.output()
t1.output()
#%%
class Dog(object):
    def work(self):
        pass

class ArmyDog(Dog):
    def work(self):
        print('追击敌人')

class DrugDog(Dog):
    def work(self):
        print('追查毒品')

class Person(object):
    def work_with_dog(self, dog):  # 只要能接收父类对象，就能接收子类对象
        dog.work()  # 只要父类对象能工作，子类对象就能工作。并且不同子类会产生不同的执行效果。

p = Person()
p.work_with_dog(ArmyDog())#等价于ArmyDog().work()
p.work_with_dog(DrugDog())#等价于DrugDog().work()

#%% 6. __dict__方法获取类/实例的属性
class Student:
    def setXY(self, x, y):
        self.x = x
        self.y = y
    def output(self):
        print("这个学生的名字是", self.name)

print(Student.__dict__)
s7 = Student()
print(s7.__dict__)
s7.setXY(5,8)
print(s7.__dict__)
#%% 一些相关的内置函数(built-in functions）
# (1) issubclass(A,B): 测试A是否为B的子类，返回True或False。 参数A和B必须都是类对象，不能是实例对象。
class Student(Person):
    def __init__(self, score=80):
        super().__init__()
        self.score = score

    def output(self):
        print(self.name, '的成绩是', self.score)

print(issubclass(Student, Person))
print(issubclass(Pool, Person))

#第二个参数可以传入一个元组，判断第一个参数类对象是否是元组中任意一个类对象的子类。
print(issubclass(Student,Pool))
print(issubclass(Student,(Pool,Student)))
#%% (2）hasattr,  getattr,  setattr,  delattr方法
# hasattr(object, name), 判断某个对象是否有属性name，其中name必须为字符串格式
class Student:
    def __init__(self, name='小明', score=80):
        self.name = name
        self.score = score

s1 = Student()
print(hasattr(s1, 'name'))
print(hasattr(s1, name))

#%% getattr(object, name[, default])，获取对象object的属性name的值并返回，其中default为可选参数，如果不存在属性name，
# 则返回default的值。
class Student:
    def __init__(self, name='小明', score=80):
        self.name = name
        self.score = score
s1 = Student(name='小白')
print(getattr(s1,'name'))
print(getattr(s1,'age','您所访问的属性不存在'))
print(getattr(s1,'name','您所访问的属性不存在'))
print(getattr(s1,'age'))
#%% setattr(object, name, value), 设置object的属性name为值value
setattr(s1,'age',20)
print(getattr(s1,'age','您所访问的属性不存在'))
#%%  delattr(object, name), 删除object中的属性name。
delattr(s1,'age')
print(getattr(s1,'age','您所访问的属性不存在'))
#%% (3) property(fget=None, fset=None, fdel=None, doc=None)的使用：通过属性设置属性, property中的参数分别是获取、
# 修改和删除属性的方法/函数
class Student:
    def __init__(self, name='小明', score=80):
        self.name = name
        self.score = score

    def getScore(self):
        return self.score

    def setScore(self, value):
        self.score = value

    def delScore(self):
        del self.score

    x = property(getScore, setScore, delScore)

s2 = Student()
print(s2.getScore())
print(s2.x)
s2.x = 90
print(s2.score)
del s2.x
print(s2.score)
#%%
class Person(object):
    def __init__(self):
        self.name = "小明"
        self.__age = 20

    # 也可以通过方法来修改私有属性的值
    def set_age(self, new_age):
        self.__age = new_age

    # 获取私有属性的值
    def get_age(self):
        return self.__age

    def __get(self):
        return self.__age
    def __set(self,a):
        self.__age=a
    def __del(self):
        del self.__age

    age = property(__get,__set,__del)

p=Person()

#强行获取私有属性
print(p._Person__age)
print(p.name)

#正常获取私有属性
print(p.age)