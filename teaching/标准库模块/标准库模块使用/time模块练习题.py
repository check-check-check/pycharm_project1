# @Time    : 
# @Author  : chen
# %% 1.将字符串的时间"2017-10-10 23:40:00"转换为时间戳和时间元组
import time
times = "2017-10-10 23:40:00"
formatTime = time.strptime(times,"%Y-%m-%d %H:%M:%S")
print(formatTime)
print(time.mktime(formatTime))#将时间元组转换成时间戳，从1970年到times时间

#%% 2.字符串格式更改。如提time = “2017-10-10 23:40:00”,想改为 time= “2017/10/10 23:40:00”
times = "2000-10-10 23:40:00"
formatTime=time.strptime(times,'%Y-%m-%d %H:%M:%S')#先变为时间元组
print(formatTime)
print(time.strftime('%Y/%m/%d %H:%M:%S',formatTime))# strftime表示时间的格式。
#%% 3.获取当前时间戳转换为指定格式日期
now = time.time()
print(now)
threeAgo=now-60*60*24*3
formaTime=time.localtime(now)#把时间戳转换为元组。
print(formaTime)
#再用strf函数转换为时间格式。
print(time.strftime('%Y/%m/%d %H:%M:%S',formaTime))
#%% 4.获得三天前的时间
threeAgo = time.time() - 60*60*24*3
threeAgo=time.localtime(threeAgo)  #把时间戳转换为元组
print(time.strftime('%Y-%m-%d %H:%M:%S',threeAgo))