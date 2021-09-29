# @Time    : 
# @Author  : chen
"python装饰器中functools.wraps的作用详解"

# 举例：定义一个最简单的装饰器
def user_login_data(f):
    def wrapper(*args, **kwargs):
        return f(*args, **kwargs)
    return wrapper
# 用装饰器装饰以下两个函数
@user_login_data
def num1():
    print("aaa")
@user_login_data
def num2():
    print("bbbb")
if __name__ == '__main__':
    print(num1.__name__)
    print(num2.__name__)
"""由此函数使用装饰器时,函数的函数名即 __name__已经被装饰器改变.一般定义装饰器的话可以
   不用考虑这点,但是如果多个函数被两个装饰器装饰时就报错,因为两个函数名一样,第二个函数再
   去装饰的话就报错.解决方案就是引入functools.wraps  ,以上代码的解决如下:"""
#%%增加@functools.wraps(f), 可以保持当前装饰器去装饰的函数的 __name__ 的值不变
import functools
def user_login_data(f):
    @functools.wraps(f)
    def wrapper(*args, **kwargs):
        return f(*args, **kwargs)
    return wrapper
@user_login_data
def num1():
    print("aaa")
@user_login_data
def num2():
    print("bbbb")
if __name__ == '__main__':
    print(num1.__name__)
    print(num2.__name__)
