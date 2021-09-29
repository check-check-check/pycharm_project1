# @Time    :
# @Author  : chen
# （一）、datetime模块中包含如下类
# 1、date	日期对象,常用的属性有year, month, day
# 2、time	时间对象
# 3、datetime	日期时间对象,常用的属性有hour, minute, second, microsecond
# 4、datetime_CAPI	日期时间对象C语言接口
# 5、timedelta	时间间隔，即两个时间点之间的长度
# 6、tzinfo	时区信息对象
# （二）、datetime模块中包含的常量
"""
常量	    功能说明	            用法	        返回值
MAXYEAR	返回能表示的最大年份	datetime.MAXYEAR	9999
MINYEAR	返回能表示的最小年份	datetime.MINYEAR	1
"""
# %% datetime模块date类
#  (1) date对象由year年份、month月份及day日期三部分构成： 通过year, month, day三个数据描述符可以进行访问：
import datetime

a = datetime.date.today()
print(a, type(a))
print(a.year, a.month, a.day)
print(a.__getattribute__("year"), a.__getattribute__("month"), a.__getattribute__("day"))
# %% (2) date对象中包含的方法与属性
"""
方法名	方法说明	用法
__eq__(…)	等于(x==y)	x.__eq__(y)
__ge__(…)	大于等于(x>=y)	x.__ge__(y)
__gt__(…)	大于(x>y)	x.__gt__(y)
__le__(…)	小于等于(x<=y)	x.__le__(y)
__lt__(…)	小于(x	x.__lt__(y)
__ne__(…)	不等于(x!=y)	x.__ne__(y)
"""
a = datetime.date(2017, 3, 1)
b = datetime.date(2017, 3, 15)
print(a.__str__(), type(a.__str__()), type(a))
print(a.__eq__(b))
print(a.__ge__(b))
print(a.__gt__(b))
# %% (3) 获得二个日期相差多少天
a = datetime.date(2017, 3, 1)
b = datetime.date(2017, 3, 15)
print(a.__sub__(b), type(a.__sub__(b)))
print(a.__sub__(b).days)
#%% (4) 如果想要让所使用的日期符合ISO标准，那么使用如下三个方法:
# *isocalendar(...)*:返回一个包含三个值的元组，三个值依次为：year年份，week number周数，weekday星期数（周一为1…周日为7)：
print(datetime.date(2017,3,22).isocalendar())
# *isoformat()返回符合ISO 8601标准 (YYYY-MM-DD) 的日期字符串
print(datetime.date(2017,3,22).isoformat())
#返回符合ISO标准的指定日期所在的星期数（周一为1…周日为7)
print(datetime.date(2017,3,22).isoweekday())
print(datetime.date(2017,3,22).weekday())

#%% timetuple(...):该方法为了兼容time.localtime(...)返回一个类型为time.struct_time的数组，但有关时间的部分元素值为0
import datetime
a = datetime.date(2017,3,22)
a = a.timetuple()
print(a)
print(a.tm_year, a.tm_mon, a.tm_yday)
#%% toordinal(...)： 返回公元公历开始到现在的天数。公元1年1月1日为1
import datetime
a = datetime.date(2017,3,22)
print(a.toordinal())
#%% replace(...)：返回一个替换指定日期字段的新date对象。参数3个可选参数，分别为year,month,day。注意替换是产生新对象，不影响原date对象。
a = datetime.date(2017,3,22)
b = a.replace(year=2018)
print(a)
print(b)
#%% resolution：date对象表示日期的最小单位。这里是天。
print(datetime.date.resolution)
#%% fromordinal(...)：将Gregorian日历时间转换为date对象；Gregorian Calendar ：一种日历表示方法，类似于我国的农历，
# 西方国家使用比较多。
a = datetime.date(2017,3,22)
b = a.toordinal()
print(datetime.date.fromordinal(b))
#%% fromtimestamp(...)：根据给定的时间戮，返回一个date对象
import time
print(datetime.date.fromtimestamp(time.time()))
#%% today(...)：返回当前日期
print(datetime.date.today())
#%% max/min： date类能表示的最大/最小的年、月、日的数值
print(datetime.date.max)
print(datetime.date.min)

#%%（6）如果你想将日期对象转化为字符串对象的话，可以用到__format__(...)方法以指定格式进行日期输出：
a = datetime.date(2017,3,22)
print(a.__format__('%Y-%m-%d'))
print(a.__format__('%Y/%m/%d'))
print(a.__format__('%Y:%m:%d'))
# 与此方法等价的方法为strftime(...)
print(a.strftime('%Y-%m-%d'))
# 如果只是相简单的获得日期的字符串，则使用__str__(...)
print('a.__str__():', a.__str__())
# 如果想要获得ctime样式的格式请使用ctime(...):
print(a.ctime())
