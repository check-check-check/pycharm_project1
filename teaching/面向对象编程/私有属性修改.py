# @Time    : 
# @Author  : chen

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
