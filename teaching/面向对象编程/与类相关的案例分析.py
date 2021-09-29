# @Time    : 
# @Author  : chen
#%%案例1
# 对象可以调用实例属性和类属性，但是类无法调用实例属性
class Student:

    # 类属性name，sex
    __key1 = 'value1'
    name = 'Student'
    sex = 'boy'
    def __init__(self, name, age):
        # 实例属性name，age
        self.name = name
        self.age = age
obj1 = Student('Tearcher', 20)

print(obj1.name, obj1.sex) #因为实例并A没有sex属性，所以会继续查找class的sex属性
print(Student.name)
# print(Student.age) #报错：type object 'Student' has no attribute 'age'

obj1.sex = 'girl' # 动态给实例绑定sex属性
# 由于实例属性优先级比类属性高，因此，它会屏蔽掉类的sex属性
# 但是类属性并未消失，用Student.sex仍然可以访问
print(obj1.sex,Student.sex)

del obj1.sex # 删除实例的sex属性
print(obj1.sex, Student.sex) #再次调用obj1.sex，由于实例的sex属性没有找到，类的name属性就显示出来了

print(Student.__key1) #类的私有属性
"""从上面的例子可以看出，在编写程序的时候，千万不要把实例属性和类属性使用相同的名字，因为相同名称的实例属性将屏蔽掉类属性，
但是当你删除实例属性后，再使用相同的名称，访问到的将是类属性"""
