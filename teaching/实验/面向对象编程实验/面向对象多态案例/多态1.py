# @Time    : 
# @Author  : chen
# 多态（polymorphism）的解释：是指基类（父类）的同一个方法在不同派生类（子类）对象中具有不同的表现和行为。派生类继承了基类行为和属性
# 之后，还会增加某些特定的行为和属性，同时还可能会对继承来的某些行为进行一定的改变，这都是多态的表现形式。也就是“一个接口多种实现”
# 作用：增加了程序的灵活性；增加了程序的可扩展性
#%% 对象所属的类之间有继承关系
# 先看一个例子
class Animal:
    def __init__(self,name):
        self.name=name
    def talk(self):
        print("Animal类的talk方法")
    @staticmethod #静态方法
    def animal_talk(obj): #动物叫的接口
        obj.talk()

class Cat(Animal):
    def talk(self):
        print("%s 喵喵叫"%self.name)
class Dog(Animal):
    def talk(self):
        print("%s 汪汪叫"%self.name)

c=Cat('小黑')
d=Dog('大黄')
print(c,d)
# 同一个方法在不同派生类（子类）对象中具有不同的表现和行为
Animal.animal_talk(c)#多态：一个接口多种实现
Animal.animal_talk(d)

# 派生类还会增加某些特定的行为，同时还可能会对继承来的某些行为进行一定的改变
c.talk()
d.talk()
#%% 在看一个例子
class gradapa:
    def __init__(self, money):
        self.money = money

    def p(self):
        print("this is gradapa")
    #这是一个类方法
    def fc(obj):
        obj.p()


class father(gradapa):
    def __init__(self, money, job):
        super().__init__(money)
        self.job = job

    def p(self):
        print("this is father,我重写了父类的方法")


class mother(gradapa):
    def __init__(self, money, job):
        super().__init__(money)
        self.job = job

    def p(self):
        print("this is mother,我重写了父类的方法")
        return 100

gradapa1 = gradapa(3000)
father1 = father(2000, "工人")
mother1 = mother(1000, "老师")

#这里的多态性体现是向同一个函数，传递不同参数后，可以实现不同功能.
gradapa.fc(gradapa1)
gradapa.fc(father1)
gradapa.fc(mother1)

#%% 对象所属的类之间没有继承关系
class Duck:                                  # 鸭子类
    def fly(self):
        print("鸭子沿着地面飞起来了")

    def test(obj):  # 实现飞的功能函数
        obj.fly()

class Swan:                                  # 天鹅类
    def fly(self):
        print("天鹅在空中翱翔")

class Plane:                                 # 飞机类
    def fly(self):
        print("飞机隆隆地起飞了")

duck = Duck()
Duck.test(duck)
swan = Swan()
Duck.test(swan)
plane = Plane()
Duck.test(plane)