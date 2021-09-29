# @Time    : 
# @Author  : chen
#%% 面向对象编程--封装(对外不可见)
"""在面向对象的编程中,通常情况下很少让外部类直接访问类内部的属性和方法，而是向外部类提供一些按钮,对其内部的成员进行访问,以保证
程序的安全性，这就是封装。"""
"""在以下案例中用户不能用student1.__score方式访问学生分数，然而用户也就知道了__score是个私有变量。我们有没有一种方法让用户通过
student1.score来访问学生分数而继续保持__score私有变量的属性呢？这时我们就可以借助python的@property装饰器了。我们可以先定义
一个方法score(), 然后利用@property把这个函数伪装成属性。见下面例子:"""
#%% @property的用法与神奇之处
# 创建一个学生类
class Student:
# 定义学生属性，初始化方法
# name和score属于实例变量, 其中score属于私有变量
    def __init__(self, name, score):
        self.name = name
        self.__score = score

    # 利用property装饰器把函数伪装成属性
    @property
    def score(self):
        print("Name: {}. Score: {}".format(self.name, self.__score))

# 实例化，创建对象
student1 = Student("John", 100)
student1.score
# 注意：一旦给函数加上一个装饰器@property,调用函数的时候不用加括号就可以直接调用函数了
#%% 面向对象编程--继承(Inheritance)
"""面向对象的编程带来的最大好处之一就是代码的重用，实现这种重用的方法之一是通过继承(Inheritance)。你可以先定义一个基类(Base class)或
父类(Parent class)，再按通过class 子类名（父类名)来创建子类(Child class)。这样子类就可以从父类那里获得其已有的属性与方法，这种现
象叫做类的继承。"""
"""我们再看另一个例子，老师和学生同属学校成员，都有姓名和年龄的属性，然而老师有工资这个专有属性，学生有分数这个专有属性。这时我们就可以
定义1一个学校成员父类，2个子类。"""
# 创建父类学校成员SchoolMember
class SchoolMember:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def tell(self):
        # 打印个人信息
        print('Name:"{}" Age:"{}"'.format(self.name, self.age), end=" ")

# 创建子类老师 Teacher
class Teacher(SchoolMember):
    def __init__(self, name, age, salary):
        SchoolMember.__init__(self, name, age) # 利用父类进行初始化
        self.salary = salary
    # 方法重写
    def tell(self):
        SchoolMember.tell(self)
        print('Salary: {}'.format(self.salary))

# 创建子类学生Student
class Student(SchoolMember):
    def __init__(self, name, age, score):
        SchoolMember.__init__(self, name, age)
        self.score = score
    def tell(self):
        SchoolMember.tell(self)
        print('score: {}'.format(self.score))

teacher1 = Teacher("John", 44, "$60000")
student1 = Student("Mary", 12, 99)

teacher1.tell() # 打印 Name:"John" Age:"44" Salary: $60000
student1.tell() # Name:"Mary" Age:"12" score: 99
"""注意：
1.在创建子类的过程中，你需要手动调用父类的构造函数__init__来完成子类的构造。
2.在子类中调用父类的方法时，需要加上父类的类名前缀，且需要带上self参数变量。比如SchoolMember.tell(self), 这个可以通过使用super
  关键词简化代码。
3.如果子类调用了某个方法(如tell())或属性，Python会先在子类中找，如果找到了会直接调用。如果找不到才会去父类找。这为方法重写带来
  了便利。"""
# 实际Python编程过程中，一个子类可以继承多个父类，原理是一样的。第一步总是要手动调用__init__构造函数
#%% super()关键字调用父类方法
"""在子类当中可以通过使用super关键字来直接调用父类的中相应的方法，简化代码。在下面例子中，学生子类调用了父类的tell()方法。
super().tell()等同于SchoolMember.tell(self)。当你使用Python super()关键字调用父类方法时，注意去掉括号里self这个参数。"""
# 创建子类学生Student
class Student(SchoolMember):
    def __init__(self, name, age, score):
        SchoolMember.__init__(self, name, age)
        self.score = score
    def tell(self):
        super().tell() # 等同于 SchoolMember.tell(self)
        print('score: {}'.format(self.score))
