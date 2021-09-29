# @Time    : 
# @Author  : chen
# 函数有返回值的情况1--返回各种数据类型：数字，字符串，元组，集合，列表，字典
def test1():

    pass #占位符，不加pass会报错

def test2():
    return 0

def test3():
    return 0,'hello',['a','b','c'],{'name':'alex'}

print(test1(),type(test1())) #无返回值，默认返回None
print(test2(),type(test2())) #返回一个值
print(test3(),type(test3())) #返回多个值时，存储在一个元组里面