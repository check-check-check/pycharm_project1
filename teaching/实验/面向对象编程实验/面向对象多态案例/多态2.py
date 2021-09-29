# @Time    : 
# @Author  : chen

# 利用多态实现：汽车租赁收费系统
"""
车型: 轿车:BMW/TESLA/VOLVO 日租费分别为：800/600/400
      客车:大于16座/小于16座 日租费分别为：1200/900
"""
# 利用控制台输入，进行租车计算
class Car:
    def __init__(self, name):
        self.name = name

    def price(self):
        pass


class BMW(Car):
    def __init__(self, name, days):
        super().__init__(name)
        self.days = days

    def price(self):
        print("租用%s的天数是%d，价格是%d" % (self.name, self.days, 800 * self.days))


class TESLA(Car):
    def __init__(self, name, days):
        super().__init__(name)
        self.days = days

    def price(self):
        print("租用%s的天数是%d，价格是%d" % (self.name, self.days, 600 * self.days))


class VOLVO(Car):
    def __init__(self, name, days):
        super().__init__(name)
        self.days = days

    def price(self):
        print("租用%s的天数是%d，价格是%d" % (self.name, self.days, 400 * self.days))

#  > 16人
class bus1(Car):
    def __init__(self, name, days):
        super().__init__(name)
        self.days = days

    def price(self):
        print("租用%s的天数是%d，价格是%d" % (self.name, self.days, 1200 * self.days))

# <= 16人
class bus2(Car):
    def __init__(self, name, days):
        super().__init__(name)
        self.days = days

    def price(self):
        print("租用%s的天数是%d，价格是%d" % (self.name, self.days, 900 * self.days))


def main():
    flag = True
    while flag:
        print("*" * 30)
        print("请选择车型：")
        print("1.小型车(4人座)")
        print("2.大型客车(4人以上)")
        size = int(input("请输入1/2："))
        if size == 1:
            print("*" * 30)
            print("请选择车型：")
            print("1.BMW，800/天")
            print("2.TESLA，600/天")
            print("3.VOLVO，400/天")
            sizecar = int(input("请选择车型1/2/3："))
            days = int(input("请输入使用天数："))
            if sizecar == 1:
                c = BMW("BMW宝马", days)
                c.price()
            elif sizecar == 2:
                c = TESLA("TESLA特斯拉", days)
                c.price()
            elif sizecar == 3:
                c = VOLVO("VOLVO沃尔沃", days)
                c.price()
            else:
                print("输入有误~")
                continue
        elif size == 2:
            print("*" * 30)
            print("请选择车型：")
            print("1.大型客车，16人及以下，1200/天")
            print("2.小型客车，16人以上，900/天")
            sizecar2 = int(input("请选择车型1/2："))
            days2 = int(input("请输入使用天数："))
            if sizecar2 == 1:
                c = bus1("大型客车", days2)
                c.price()
            elif sizecar2 == 2:
                c = bus2("小型客车", days2)
                c.price()
            else:
                print("输入有误~")
                continue
        else:
            print("输入有误~")
            continue


if __name__ == "__main__":
    main()
