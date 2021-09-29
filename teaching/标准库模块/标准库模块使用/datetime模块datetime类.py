# @Time    : 
# @Author  : chen
# %% datetime模块datetime类
# (一)、datetime类的数据构成
# datetime类其实是可以看做是date类和time类的合体，其大部分的方法和属性都继承于这二个类，
# datetime(year, month, day[, hour[, minute[, second[, microsecond[,tzinfo]]]]])
# （二）、专属于datetime的方法和属性
# %% 1、 date(…)：返回datetime对象的日期部分：
from datetime import datetime

a = datetime.now()
print(a, type(a))
print(a.date())
# %% 2、time(…)：返回datetime对象的时间部分：
print(a.time())
# %% 3、utctimetuple(…)：返回UTC时间元组：
print(a.utctimetuple())
# %% 4、combine(…)：将一个date对象和一个time对象合并生成一个datetime对象：
print(datetime.combine(a.date(), a.time()))
# %% 5、now(…)：返回当前日期时间的datetime对象：
print(a.now())
# %% 6、utcnow(…):返回当前日期时间的UTC datetime对象：
print(a.utcnow())
#%% 7、strptime(…)：根据string, format 2个参数，返回一个对应的datetime对象：
print(datetime.strptime('2017-3-22 15:25','%Y-%m-%d %H:%M'))
#%% 8、utcfromtimestamp(…):UTC时间戳的datetime对象，时间戳值为time.time()：
import time
print(datetime.utcfromtimestamp(time.time()))