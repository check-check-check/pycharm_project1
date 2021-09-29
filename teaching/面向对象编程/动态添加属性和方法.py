# @Time    : 
# @Author  : chen
#%% python动态添加属性
class Person(object):
    def __init__(self, newName, newAge):
        self.name = newName
        self.age = newAge

laowang = Person("laowang", 20)
print(laowang.name)
print(laowang.age)
laowang.addr = "北京"  # 动态添加的属性addr
print(laowang.addr)
#%% python动态添加方法：
import types
class Person(object):
    def __init__(self,newName,newAge):
        self.name = newName
        self.age = newAge
    def eat(self):
        print("...%s正在吃。。"%self.name)
def run(self):
    print("...%s正在跑。。"%self.name)
Wang = Person("laowang",20)
Wang.eat()
Wang.run = types.MethodType(run,Wang) #将run这个函数添加为方法
Wang.run()
#%% python添加静态方法和类方法，注意点，静态方法和类方法都是与类关联的
class Person(object):
    def __init__(self,newName,newAge):
        self.name = newName
        self.age = newAge
    def eat(self):
        print("...%s正在吃。。"%self.name)
@staticmethod#静态方法
def test():
    print("...static method...")
@classmethod#类方法
def test1(cls):
    print("...class method...")
laowang= Person("laowang",20)
Person.test = test#添加静态方法,静态方法跟着类走的
Person.test()
Person.test1 = test1#添加类方法，类方法跟着类走的
Person.test1()
