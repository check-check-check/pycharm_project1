# @Time    : 
# @Author  : chen
# Python的time模块中时间表现的形式有三种：
"""
1.struct_time时间元组---通过time.localtime()可以生成一个struct_time
int tm_sec;		 /* 秒–取值区间为[0,59] */ 　　
int tm_min; 		 /* 分 - 取值区间为[0,59] */ 　　
int tm_hour; 	         /* 时 - 取值区间为[0,23] */ 　　
int tm_mday;		 /* 一个月中的日期 - 取值区间为[1,31] */ 　
int tm_mon;		 /* 月份（从一月开始，0代表一月） - 取值区间为[0,11] */
int tm_year; 	         /* 年份，其值从1900开始 */ 　
int tm_wday; 	         /* 星期–取值区间为[0,6]，其中0代表星期天，1代表星期一，以此类推 */ 　
int tm_yday; 	         /* 从每年的1月1日开始的天数–取值区间为[0,365]，其中0代表1月1日，1代表1月2日，以此类推 */ 　
int tm_isdst; 	         /* 夏令时标识符，实行夏令时的时候，tm_isdst为正。不实行夏令时的进候，tm_isdst为0；不了解情况时，tm_isdst()为负。*/ 　
long int tm_gmtoff;	 /*指定了日期变更线东面时区中UTC东部时区正秒数或UTC西部时区的负秒数*/ 　　
const char *tm_zone;     /*当前时区的名字(与环境变量TZ有关)*/

2.timestamp时间戳---适合进行时间的加减，time模块不能直接对时间进行加减，比如说加1个小时，1天，只能通过时间戳进行加减

3.格式化的时间字符串---适合打印输出

"""
#%% 字符串转时间strptime()函数
import time
print(
        (
            "字符串转时间: time.strptime(\"2019-10-08 20:30:00\", \"%Y-%m-%d %H:%M:%S\")\n"
            " --> {}"
        ).format(time.strptime("2019-10-08 20:30:00", "%Y-%m-%d %H:%M:%S"))
)
#%% 时间转字符串strftime()函数
t = time.localtime()
print(t)
print("时间转字符串: time.strftime(\"%Y-%m-%d %H:%M:%S\", t) --> {}".format(
        time.strftime("%Y-%m-%d %H:%M:%S", t)))
#%% 时间转时间戳time.mktime()函数
t = time.localtime()
print("时间转时间戳: time.mktime(t) --> {}".format(time.mktime(t)))
#%% 时间戳转时间time.localtime()函数
sec = time.time()
print("时间戳转时间: time.localtime(sec) --> {}".format(time.localtime(sec)))
#%%字符串与时间戳之间的转换需要先转成时间类再向目标类型转换
#字符串转时间戳,转换过程: 字符串 --> 时间 --> 时间戳
f = "2019-10-03 10:45:00"
df = "%Y-%m-%d %H:%M:%S"
t = time.strptime(f, df)
sec = time.mktime(t)
print("字符串转时间戳: sec = {}".format(sec))
#时间戳转字符串,转换过程：时间戳 --> 时间 --> 字符串
sec = 1570070700
t = time.localtime(sec)
time_str = time.strftime("%Y-%m-%d %H:%M:%S", t)
print("时间戳转字符串: time_str= {}".format(time_str))

"----------------------------------------------------------------"
#%% 获取当时间
print(time.localtime()) # 获取当时时间
print(time.time()) # 获取当时时间的时间戳
#获取当时时间特定格式的字符串
print(time.asctime())
print(time.ctime())
#%% 下面给出一个时间字符串加3个小时,并打印结果:
#时间的加减:time模块时间的加减只能通过timestamp加减对应的秒数,然后再转回去
t = time.strptime("2019-10-03 10:45:00", "%Y-%m-%d %H:%M:%S")
sec = time.mktime(t)
sec += 3 * 60 * 60
t1 = time.localtime(sec)
s1 = time.strftime("%Y-%m-%d %H:%M:%S", t1)
print("加3小时后的时间为: {}".format(s1))