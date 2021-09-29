# @Time    : 
# @Author  : chen
# 第2关：覆盖方法
class Point:
    def __init__(self, x, y, z, h):
        self.x = x
        self.y = y
        self.z = z
        self.h = h
    def getPoint(self):
        return self.x, self.y, self.z, self.h
class Line(Point):
    # 请在下面填入覆盖父类getPoint()方法的代码，并在这个方法中分别得出x - y与z - h结果的绝对值
    ########## Begin ##########
    def getPoint(self):
        length_one = abs(self.x - self.y)
        length_two = abs(self.z - self.h)
        ########## End ##########
        print(length_one, length_two)
obj1 = Line(1,2,3,4)
obj1.getPoint()