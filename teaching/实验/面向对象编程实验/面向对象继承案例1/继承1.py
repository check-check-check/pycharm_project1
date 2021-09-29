# @Time    : 
# @Author  : chen
# 第1 关：初识继承
# 定义了一个父类animal类，在此类中定义了三个方法，分别为:breathing()、runing()、foraging()
class animal:
    def foraging(self):
        print('foraging....')
    def runing(self):
        print('runing...')
    def breathing(self):
        print('breathing...')

# 请在下面填入定义fish类的代码，fish类继承自animal类
########## Begin ##########
class fish(animal):
########## End ##########
    def __init__(self,name):
        self.name = name
    def swim(self):
        print("%s会游泳" %self.name)

# 请在下面填入定义leopard类的代码，leopard类继承自animal类
########## Begin ##########
class leopard(animal):
########## End ##########
    def __init__(self,name):
        self.name = name
    def climb(self):
        print("%s会爬树" %self.name)

fName = input()
lName = input()
f = fish(fName)
f.breathing()
f.swim()
f.foraging()

l = leopard(lName)
l.breathing()
l.runing()
l.foraging()