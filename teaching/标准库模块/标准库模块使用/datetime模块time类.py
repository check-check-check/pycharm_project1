# @Time    : 
# @Author  : chen
#%%datetime模块time类
# (一)：time类由hour小时、minute分钟、second秒、microsecond毫秒和tzinfo五部分组成
#%% 相应的，time类中就有上述五个变量来存储应该的值：
from datetime import time
a = time(12,20,59,899)
print(a.hour, a.min, a.second, a.microsecond,a.tzinfo)
# 与date类一样，time类也包含__getattribute__(...)方法可以读取相关属性：
print(a.__getattribute__('hour'))
print(a.__getattribute__('minute'))
print(a.__getattribute__('second'))
print(a.__getattribute__('microsecond'))
print(a.__getattribute__('tzinfo'))

#%%（二）、time类中的方法和属性
# 1、比较时间大小：这里的方法与date类中定义的方法大同小异
a = time(12,20,59,899)
b = time(11,20,59,889)
print(a.__gt__(b))
print(a.max, a.min)
print(time.resolution) # resolution：时间间隔单位为分钟

#%%（三）、时间的字符串输出
# 1、如果你想将时间对象转化为字符串对象的话，可以用到__format__(...)方法以指定格式进行时间输出：
a = time(12, 20, 59, 899)
print(a.__format__('%H-%M-%S'))
print(a.__format__('%H/%M/%S'))
print(a.__format__('%H:%M:%S'))
# 与此方法等价的方法为strftime(...)
print(a.strftime('%H-%M-%S'))
print(a.strftime('%H/%M/%S'))
print(a.strftime('%H:%M:%S'))
# 2、ISO标准输出：如果要使输出的时间字符符合ISO标准，请使用isoformat(...):
a = time(12, 20, 59, 899)
print(a.isoformat())
# 3、如果只是相简单的获得时间的字符串，则使用__str__(...)
a = time(12, 20, 59, 899)
print(a.__str__())
#