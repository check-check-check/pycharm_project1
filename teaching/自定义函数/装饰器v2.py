# @Time    : 
# @Author  : chen
import time
def timer(func):
    def deco(*args, **kwargs):
        start_time = time.time()
        func(*args, **kwargs)
        end_time = time.time()
        print('函数{}的执行时间是:{}'.format(func, end_time - start_time))
    return deco
@timer
def test1():
    time.sleep(2)
    print('in the test1')
@timer
def test2(a, b):
    print('求和：', a+b)


test1()
test2(3,4)
