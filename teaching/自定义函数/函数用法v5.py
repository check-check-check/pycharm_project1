# @Time    : 
# @Author  : chen
# 函数有返回值的情况2
# positional argument位置参数，即通过在参数列表中的相对位置确定传递给哪个形参
# keyword argument关键参数，通过name=value这样的形式，根据name确定传递给哪个形参。


"""正常情况下，给函数传参数要按顺序，不想按顺序就可以用关键参数，只需指定参数名即可，
但记住一个要求就是，关键参数必须放在位置参数之后。"""


def test(x, y, z):  # x,y,z形参
    print(x, y, z)


# x=3,y=6,z=2
test(x=3, y=6, z=2)
test(3, 6, 2)
test(x=3, z=2, y=6)  # x,y,z实参
test(3, z=2, y=6)


# 默认参数特点：调用函数的时候，默认参数非必须传递
def conn(host, port=3306):
    print('ip是：%s，port是：%d' % (host, port))


conn('128.168,0,0', port=3305)
