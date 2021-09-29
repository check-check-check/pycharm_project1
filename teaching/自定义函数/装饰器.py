# @Time    : 
# @Author  : chen
"""python装饰器(死记装饰器的功能)"""
"""注释：python装饰器（fuctional decorators）就是用于拓展原来函数功能的一种函数，
目的是在不改变原函数名(或类名)的情况下，给函数增加新的功能。这个函数的特殊之处在于
它的返回值也是一个函数，这个函数是内嵌“原“”函数的函数。"""
#%% 一般而言，我们要想拓展原来函数代码，最直接的办法就是侵入代码里面修改，例如：
import time
def f():
    print("hello")
    time.sleep(1)
    print("world")
#%% 这是我们最原始的的一个函数，然后我们试图记录下这个函数执行的总时间，那最简单的做法就是改动原来的代码：
import time
def f():
    start_time = time.time()
    print("hello")
    time.sleep(1)
    print("world")
    end_time = time.time()

    execution_time = (end_time - start_time)*1000
    print("time is %d ms" %execution_time)
#%%
"""但是实际工作中，有些时候核心代码并不可以直接去改，所以在不改动原代码的情况下，我们可以再定义一个函数。
（但是生效需要再次执行函数）"""
import time
def deco(func):# 该函数的输入是个函数名
    start_time = time.time()
    f()#函数名+（）表示函数的执行
    end_time = time.time()
    execution_time = (end_time - start_time)*1000
    print("time is %d ms" %execution_time)

def f():
    print("hello")
    time.sleep(1)
    print("world")

if __name__ == '__main__':# __name__是Python的内置变量，这里是程序的入口。详见：https://blog.csdn.net/q2605894893/article/details/82345814

    deco(f)
    print("f.__name__ is",f.__name__)#返回f的名字
"""这里我们定义了一个函数deco，它的参数是一个函数，然后给这个函数嵌入了计时功能。但是想要拓展这一千万个函数功能，
就是要执行一千万次deco()函数，所以这样并不理想！接下来，我们可以试着用装饰器来实现，先看看装饰器最原始的面貌。 """
#%%
import time
def deco(f):
    def wrapper():
        start_time = time.time()
        f()
        end_time = time.time()
        execution_time = (end_time - start_time)*1000
        print("time is %d ms" %execution_time )
    return wrapper

@deco #给以下函数增加了一部分功能，同时不改变原函数名(或类名),该条语句相当于：f=deco(f)=wrapper
def f():
    print("hello")
    time.sleep(1)
    print("world")

if __name__ == '__main__':
    f()
"""这里的deco函数就是最原始的装饰器，它的参数是一个函数，然后返回值也是一个函数。
其中作为参数的这个函数f()就在返回函数wrapper()的内部执行。然后在函数f()前面加上@deco，
f()函数就相当于被注入了计时功能，现在只要调用f()，它就已经变身为“新的功能更多”的函数了,
（不需要重复执行原函数）。"""
#%%扩展1：带有固定参数的装饰器
import time
def deco(f):
    def wrapper(a,b):
        start_time = time.time()
        f(a,b)
        end_time = time.time()
        execution_time = (end_time - start_time)*1000
        print("time is %d ms" % execution_time)
    return wrapper

@deco
def f(a,b):
    print("be on")
    time.sleep(1)
    print("result is %d" %(a+b))

if __name__ == '__main__':
    f(3,4)
#%%扩展2：无固定参数的装饰器
import time

def deco(f):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        f(*args, **kwargs)
        end_time = time.time()
        execution_time= (end_time - start_time)*1000
        print("time is %d ms" %execution_time)
    return wrapper


@deco
def f(a,b):
    print("be on")
    time.sleep(1)
    print("result is %d" %(a+b))

@deco
def f2(a,b,c):
    print("be on")
    time.sleep(1)
    print("result is %d" %(a+b+c))


if __name__ == '__main__':
    f2(3,4,5)
    print(f2.__name__)
    f(3,4)
    print(f.__name__)
#%% 扩展3：使用多个装饰器，装饰一个函数
import time
def deco01(f):
    def wrapper(*args, **kwargs):
        print("this is deco01")
        start_time = time.time()
        f(*args, **kwargs)
        end_time = time.time()
        execution_time = (end_time - start_time)*1000
        print("time is %d ms" % execution_time)
        print("deco01 end here")
    return wrapper

def deco02(f):
    def wrapper(*args, **kwargs):
        print("this is deco02")
        f(*args, **kwargs)

        print("deco02 end here")
    return wrapper

@deco01
@deco02
def f(a,b):
    print("be on")
    time.sleep(1)
    print("result is %d" %(a+b))

if __name__ == '__main__':
    f(3,4)
    print(f.__name__)
#%%扩展4
import functools
def log(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        print('call %s():' % func.__name__)
        print('args = {}'.format(*args))
        return func(*args, **kwargs)

    return wrapper


@log
def test(p):
    print(test.__name__ + " param: " + p)
test("I'm a param")