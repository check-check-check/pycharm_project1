# @Time    : 
# @Author  : chen
# %%基本概念：类、对象、属性、方法
"""
类(Class)与对象(Object)
类(Class)是用来描述具有相同属性(Attribute)和方法(Method)对象的集合。对象(Object)是类(Class)的具体实例。
比如学生都有名字和分数，他们有着共同的属性。这时我们就可以设计一个学生类, 用于记录学生的名字和分数，并自定义
方法打印出他们的名字和方法。
属性(Attribute): 类里面用于描述所有对象共同特征的变量或数据。比如学生的名字和分数。
方法(Method): 类里面的函数，用来区别类外面的函数, 用来实现某些功能。比如打印出学生的名字和分数。
"""
# 类是抽象的, 也称之为”对象的模板”; 我们需要通过类这个模板, 创建类的实例对象, 然后才能使用类定义的功能;
# %% 例如：我们创建一个学生类
class Student:

    # 定义学生属性，初始化方法
    def __init__(self, name, score):
        # print(self,id(self),type(self)) #当我们要实例化一个类时，会自动调用__init__函数，sef 会指向实例化的对象，即'self=实例化后的对象'
        self.name = name
        self.score = score

    # 定义学生方法
    def show(self):
        print("Name: {}. Score: {}".format(self.name, self.score))


"""在这个案例中，我们只定义了一个抽象的类，电脑并没有创建什么存储空间。只有当我们完成类的实例化(Instance)时，
电脑才会创建一个具体的对象（Object），并为之分配存储空间。所以对象（Object)是类（Class)的一个实例。"""

# 创建一个具体的学生对象(Object)
student1 = Student("John", 100)  # 实例化时自动传入self参数,其他参数是位置参数，与__init__函数里面的参数一一对应对应："John"=name，score=100
# 与上面等价student1 = Student(name="John", score=100)
student2 = Student("Lucy", 99)  # 实例化

print(student1,id(student1),type(student1))
print(student2,id(student2),type(student2))
"""在这个案例中，Student是类，student1和student2是我们创建的具体的学生对象。当我们输入上述代码时，Python会自动调用
默认的__init__初始构造函数来生成具体的对象。关键字self是个非常重要的参数，代表创建的对象本身。"""
# 当你创建具体的对象后，你可以直接通过student1.name和student1.score来分别获取学生的名字和分数，也可以通过student1.show()来
# 直接打印学生的名字和分数。
print(student1.name, student1.score)
student1.show()
#%%我们再看一个案例：
class Role(object):
    def __init__(self, name, role, weapon, life_value=100, money=15000):
        self.name = name
        self.role = role
        self.weapon = weapon
        self.life_value = life_value
        self.money = money

    def shot(self):
        print("shotting...")

    def got_shot(self): #形式1
        print("ah...%s got shot..." % self.name)

    def buy_gun(self, gun_name): #形式2
        print("%s just bought %s" % (self.name, gun_name))

r2 = Role("Amy", "terrorist", "B22")# 实例化（初始化一个类，创建了一个对象）
r2.got_shot() #调用形式1

r1 = Role("Jack", "police", "AK-47")
r1.buy_gun("B51") #调用形式2
# %%类变量(class variables)与实例变量（instance variables）
"""假设我们需要在Student类里增加一个计数器number，每当一个新的学生对象(Object)被创建时，这个计数器就自动加1。由于这个计数器不属
于某个具体学生，而属于Student类的，所以被称为类变量(class variables)。而姓名和分数属于每个学生对象的，所以属于实例变量(instance 
variables)，也被称为对象变量(object variables)。"""

# 这个新Student类看上去应该是这样的:
# 创建一个学生类
class Student:
    # number属于类变量，定义在方法外，不属于具体实例
    number = 0

    # 定义学生属性，初始化方法
    # name和score属于实例变量，定义在方法里
    def __init__(self, name, score):
        self.name = name
        self.score = score
        # 此处有错误：错误的使用调用类变量的方法
        number = number + 1

    # 定义打印学生信息的方法
    def show(self):
        print("Name: {}. Score: {}".format(self.name, self.score))

# 类变量和实例变量的区别很大，访问方式也也不一样。
"""
类变量：类变量在整个实例化的对象中是公用的。类变量定义在类中且在函数体之外。访问或调用类变量的正确方式是"类名.变量名"或者
        "self.__class__.变量名"。self.__class__自动返回每个对象的类名。
实例变量：定义在方法中的变量，属于某个具体的对象。访问或调用实例变量的正确方式是"对象名.变量"名或者"self.变量名".
"""
# %%正确调用类变量和实例变量的方法
# 创建一个学生类
class Student:
    # number属于类变量，不属于某个具体的学生实例
    number = 0

    # 定义学生属性，初始化方法
    # name和score属于实例变量
    def __init__(self, name, score):
        self.name = name
        self.score = score
        Student.number = Student.number + 1  # 类变量用类来调用

    # 定义打印学生信息的方法
    def show(self):
        # print(self)
        print("Name: {}. Score: {}".format(self.name, self.score))  # 实例变量是用实例来调用(在类内调用）


# 实例化，创建对象
student1 = Student("John", 100) # 等价于student1 = Student.__init__(self=Student, name="John", score=100)
student2 = Student("Lucy", 99)

print(Student.number)  # 调用类变量
print(student1.__class__.number)

print(student1.name) # 调用实例变量

#%%类方法(Class method)
"""
正如同有些变量只属于类，有些方法也只属于类，不属于具体的对象。你有没有注意到属于对象的方法里面都有一个self参数, 比如
__init__(self),show(self)? self是指对象本身。
属于类的方法不使用self参数， 而使用参数cls，代表类本身。另外习惯上对类方法我们会加上@classmethod的修饰符做说明。"""
# 同样拿Student为例子，我们不用print函数打印出已创建学生对象的数量，而是自定义一个类方法来打印，我们可以这么做:
class Student:
    # number属于类变量，不属于某个具体的学生实例
    number = 0

    # 定义学生属性，初始化方法
    # name和score属于实例变量
    def __init__(self, name, score):
        self.name = name
        self.score = score
        Student.number = Student.number + 1

    # 定义打印学生信息的方法
    def show(self):
        print("Name: {}. Score: {}".format(self.name, self.score))
    # 定义类方法，打印学生的数量
    @classmethod
    def total(cls):
        print("Total: {0}".format(cls.number))
# 实例化，创建对象
student1 = Student("John", 100)
student2 = Student("Lucy", 99)
Student.total() # 调用类方法
#%% 类的私有属性(private attribute)和私有方法(private method)
"""类里面的私有属性和私有方法以双下划线"__"开头。私有属性或方法不能在类的外部被使用或直接访问。我们同样看看学生类这个例子，把分数score变为
私有属性，看看会发生什么。"""
# 创建一个学生类
class Student:
    # 定义学生属性，初始化方法
    # name和score属于实例变量, 其中__score属于私有变量
    def __init__(self, name, score):
        self.name = name
        self.__score = score
    # 定义打印学生信息的方法
    def show(self):
        print("Name: {}. Score: {}".format(self.name, self.__score))

# 实例化，创建对象
student1 = Student("John", 100)
student1.show() # 打印 Name: John, Score: 100
student1.__score # 打印出错，该属性不能从外部访问
"""如果你将score变成__score, 你将不能直接通过student1.__score获取该学生的分数。show()可以正常显示分数，是因为它是类里面的函数，可以
访问私有变量。"""
#%%私有方法是同样的道理
# 当我们把show()变成，__show()你将不能再通过student1.__show()打印出学生的名字和分数。值得注意的是私有方法必需
# 含有self这个参数，且把它作为第一个参数。
class Student:

    # 定义学生属性，初始化方法
    # name和score属于实例变量, 其中__score属于私有变量
    def __init__(self, name, score):
        self.name = name
        self.__score = score

    # 定义打印学生信息的方法
    def __show(self):
        print("Name: {}. Score: {}".format(self.name, self.__score))

# 实例化，创建对象
student1 = Student("John", 100)
student1.__show()

#%% 外界无法访问私有方法，但可以在类内部调用私有方法
class Test(object):
    #私有方法
    def __test2(self):
        print("私有方法__test2方法")
    #普通方法
    def test(self):
        print("普通方法test")
    #普通方法
    def _test1(self):
        print("普通方法_test1方法")
        #可以在类内部调用私有方法
        self.__test2()
t = Test()
t.test()
t._test1()





