# @Time    : 
# @Author  : chen
# datetime模块timedelta类
# timedelta类是用来计算二个datetime对象的差值的
"""
函数原型：
class datetime.timedelta([days[, seconds[, microseconds[, milliseconds[, minutes[, hours[, weeks]]]]]]])
从构造函数的定义中可以看出，所有参数都是可选的，并且默认都是0。参数的值可以是整数，浮点数，正数或负数。
"""
"""
此类中包含如下属性：
1、days:天数
2、microseconds：微秒数(>=0 并且 <1秒）
3、seconds：秒数(>=0 并且 <1天）
"""
# datetime.timedelta对象代表两个时间之间的时间差，两个date或datetime对象相减就可以返回一个timedelta对象。
#%% 1、以下是打印一天后的时间
import datetime
now=datetime.datetime.now()
delta=datetime.timedelta(days=1)
newtime=now+delta
print(newtime)
print(str(newtime))
print(newtime.strftime("%Y-%m-%d %H:%M:%S"), type(newtime.strftime("%Y-%m-%d %H:%M:%S")))
#%% 2、以下是得到1天前的时间，还有一种
now=datetime.datetime.now()
newtime1 = now-datetime.timedelta(days=1)
newtime2 = now+datetime.timedelta(days=-1)
print(newtime1, newtime2)
#%% 3、以下是得到3小时前的时间
now=datetime.datetime.now()
newtime = now-datetime.timedelta(hours=3)
print(newtime)
#%% 4、以下是得到3小时30分钟前的时间
now=datetime.datetime.now()
newtime = now-datetime.timedelta(hours=3, minutes=30)
print(newtime)
#%% 5、以下是得到3小时30秒前的时间
now=datetime.datetime.now()
newtime = now-datetime.timedelta(hours=3, seconds=30)
print(newtime)

# 以下是得到3天3小时30秒前的时间
print(now-datetime.timedelta(hours=3,seconds=30,days=3))
# 以下是得到总秒数，类型是float型
print(datetime.timedelta(hours=3,seconds=22).total_seconds())

