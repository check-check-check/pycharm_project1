# @Time    : 
# @Author  : chen
# 创建对象, 我们需要定义构造函数__init__()方法; 构造函数用于执行”实例对象的初始化工作”,
# 即对象创建后, 初始化当前对象的相关属性, 无返回值;
"""__init__()要点如下：
1.名称固定，必须为__init__()
2.第一个参数固定，必须为self。self指的就是刚刚创建好的示例对象;
3.构造函数通常用来初始化示例属性
4.__init__()方法：初始化创建好的对象，初始化指的是："给实例属性赋值";
"""
#%% 形式1: def __init__(self)
"""这种形式在__init__方法中，只有一个self，指的是实例的本身，但是在方法的类部，包含两个属性，name， grade。它允许定义一个空
的结构，当新数据来时，可以直接添加。实例化时，需要实例化之后，再进行赋值。"""
class Student:
    def __init__(self):
        self.name = None
        self.grade = None

    def print_grade(self):
        print("%s grade is %s" % (self.name, self.grade))


s1 = Student()  # 创建对象s1
s1.name = "Tom"
s1.grade = 8

s2 = Student()  # 创建对象s2
s2.name = "Jerry"
s2.grade = 7

s1.print_grade()
s2.print_grade()
#%%形式2：def __init__(self, 参数1，参数2，···，参数n)
# 这种形式在定义方法时，就直接给定了两个参数name和grade，且属性值不允许为空。实例化时，直接传入参数。
class Student:
    def __init__(self, name, grade):
        self.name = name
        self.grade = grade

    def print_grade(self):
        print("%s grade is %s" % (self.name,self.grade))

s1 = Student("Tom", 8)  # 创建对象s1
s2 = Student("Jerry", 7)  # 创建对象s2

s1.print_grade()
s2.print_grade()

"""总结：
1、self是形式参数，当执行s1 = Student(“Tom”, 8)时，self等于s1；当执行s2 = Student(“sunny”, 7)时，self=s2。
2、两种方法的区别在于定义函数时属性赋值是否允许为空和实例化时是否直接传入参数，个人觉得第二种更为简洁。"""

#%% 类中为什么要定义__init__()方法?
# 1、不用init()方法定义类
class Rectangle:
    def getPeri(self,a,b):
        return (a + b)*2
    def getArea(self,a,b):
        return a*b

rect = Rectangle()
print(rect.getPeri(3,4))
print(rect.getArea(3,4))
print(rect.__dict__) #查看实例属性__init__里面

"""
1.从上例中可以看到，我们在类中并没有定义init()方法，但是也能够得到类似的要求，结果返回了矩形实例rect的周长及面积。
2.但是，我们通过print(rect.__dict__)来看这个实例的属性，竟然是空的，我定义了一个矩形，按理来说它的属性应该是它的长、宽。
但是它竟然没有。这就是没有定义init()的原因了。
3.在实例化对象的时候，rect = Rectangle()参数为空，没有指定a、b的值，只有在调用函数的时候才指定了。且类中定义的每个方法的
参数都有a、b，这显然浪费感情，在类中直接指定方法就可以了。
"""

#%% 2、用init()方法定义类
# 上述同样的例子，采用init()方法定义类，如下：
class Rectangle:
    def __init__(self,a,b):
        self.a = a
        self.b = b
    def getPeri(self):
        return (self.a + self.b)*2
    def getArea(self):
        return self.a*self.b

rect = Rectangle(3,4 )
print(rect.getPeri())
print(rect.getArea())
print(rect.__dict__) #查看实例属性__init__里面

# 定义完init()后，创建的每个实例都有自己的属性，也方便直接调用类中的函数。