# @Time    :
# @Author  : chen
class HouseItem:
    def __init__(self, name, area):
        self.name = name
        self.area = area
    def __str__(self):
        return "%s 占地 %.2f" % (self.name, self.area)
class House:
    def __init__(self, house_type, area):
        self.house_type = house_type
        self.area = area
        # 剩余面积
        self.free_area = area
        # 家具名称列表
        self.item_list = []
    def __str__(self):
        # Python 能够自动的将一对括号内部的代码连接在一起
        return ("户型：%s\n总面积：%.2f[剩余：%.2f]\n家具：%s"
                % (self.house_type, self.area,
                   self.free_area, self.item_list))
    def add_item(self, item):  # item = bed = HouseItem("席梦思", 4)
        print("要添加 %s" % item)
        # 1. 判断家具的面积，这里的item.area要理解清楚。
        if item.area > self.free_area:
            print("%s 的面积太大了，无法添加" % item.name)
        # 2. 将家具的名称添加到列表中
        self.item_list.append(item.name)
        # 3. 计算剩余面积
        self.free_area -= item.area
# 1. 创建家具
bed = HouseItem("席梦思", 4) #实例化
print(bed,type(bed))
chest = HouseItem("衣柜", 3)
table = HouseItem("餐桌", 2)
print(chest)
print(table)
#
# 2. 创建房子对象
my_home = House("两室一厅", 60)
#
# 3.添加了三个对象
my_home.add_item(bed)
# my_home.add_item(chest)
# my_home.add_item(table)
#
print(my_home)