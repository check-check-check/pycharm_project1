# @Time    : 
# @Author  : chen
# @property作用
# %% 看如下的例子：在绑定属性时，如果我们直接把属性暴露出去，虽然写起来很简单，但是，没办法检查参数，导致可以把成绩随便改：
# 为了限制score的范围，可以通过一个set_score()方法来设置成绩，再通过一个get_score()来获取成绩，这样，在set_score()方法里，
# 就可以检查参数：
class Student(object):

    def get_score(self):
        return self.socre

    def set_socre(self, value):
        if not isinstance(value, int):
            raise ValueError('score must be an integer!')
        if value < 0 or value > 100:
            raise ValueError('score must between 0 - 100.')
        if value >= 0 and value <= 100:
            self.socre = value

s = Student()
s.set_socre(18)
print(s.get_score(), s.socre)
# 现在，对任意的Student实例进行操作，就不能随心所欲地设置score了。有没有既能检查参数，又可以用类似属性这样简单的方式来访问类的变量呢？
#%% Python的装饰器（decorator）可以给函数动态加上功能。对于类的方法，装饰器一样起作用。Python内置的@property装饰器就是负责把一个
# 方法变成属性调用的：
class Student(object):
    @property
    def score(self):
        return self._score

    @score.setter
    def score(self,value):
        if not isinstance(value, int):
            raise ValueError('score must be an integer!')
        if value < 0 or value > 100:
            raise ValueError('score must between 0 - 100!')
        self._score = value

# @property本身又创建了另一个装饰器@score.setter，负责把一个setter方法变成属性赋值，于是，我们就拥有一个可控的属性操作。
s = Student()
s.score = 60
print(s.score)
s.score = 9999 # 报错 ValueError: score must between 0 - 100!

# 注意：变量前的单下划线表示表面上私有 ，但是其实这样的实例变量外部是可以访问的，但是，按照约定俗成的规定，当你看到这样的变量时，意思就是，
# “虽然我可以被访问，但是，请把我视为私有变量，不要随意访问”。

# @property广泛应用在类的定义中，可以让调用者写出简短的代码，同时保证对参数进行必要的检查，这样，程序运行时就减少了出错的可能性。
#%%以下是个@property的练习题
# 利用@property给一个Screen对象加上width和height属性，以及一个只读属性resolution(等于width*height）
class Screen:
    @property
    def width(self):
        return self._width
    @width.setter
    def width(self,value):
        self._width = value

    @property
    def height(self):
        return self._height
    @height.setter
    def height(self,value):
        self._height = value

    @property
    def resolution(self):
        return self.height*self.width

A = Screen()
A.width = 10
A.height = 20
print(A.resolution)

# %% 再看一个例题：
class People(object):
    def __init__(self, name, age):
        self.name = name
        self.age = age
        # 私有属性
        self.__number = 0

    # 获取私有属性值  number = p1.number 会执行这个函数
    @property
    def number(self):
        # 返回私有属性值
        return self.__number

    # 设置私有属性值  p1.number = 666
    @number.setter
    def number(self, value):
        # 设置__number的值
        self.__number = value

    # 删除私有属性  del p1.number 会执行这个函数
    @number.deleter
    def number(self):
        # 删除属性
        del self.__number


p1 = People('张三', 22)
# 正常的对象属性赋值: 对象.属性名 = 属性值
p1.name = '李四'
# 删除对象的属性
del p1.name

# 私有属性升级版
# 会去执行@property装饰number函数，函数执行完成后返回一个结果
num = p1.number
print(num)

# 会去执行@number.setter装饰的number函数，在函数中设置__number属性的值
p1.number = 666
# 会去执行@property装饰number函数，函数执行完成后返回一个结果
print(p1.number)

# 会去执行@number.deleter装饰的number函数，在函数中会将__number属性删除
del p1.number
# 会去执行@property装饰number函数，函数执行完成后返回一个结果
# print(p1.number)  # 会报错，属性已经被删除
