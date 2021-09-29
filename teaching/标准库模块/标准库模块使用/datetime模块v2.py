# @Time    : 
# @Author  : chen
"""datetime模块提供强大易用的日期处理功能，用于记录程序操作或修改时间、时间计算、日志时间显示等功能。
datatime模块重新封装了time模块，提供的类包括date、time、datetime、timedelta、tzinfo。"""
# %% 1、获取当前日期时间
import datetime

print(datetime.datetime.now())
print(datetime.datetime.now().date())
print(datetime.datetime.now().time())
print(datetime.date.today())

# %% 2、获取当前日期、当前年份、当前月份、当天
print(datetime.date.today())
print(str(datetime.date.today())[0:4])
print(str(datetime.date.today())[5:7])
print(str(datetime.date.today())[8:10])

# 等价于
print(datetime.date.today().year)
print(datetime.date.today().month)
print(datetime.date.today().day)

# %% 3、计算距离当前10天前、10天后的日期
# 计算10天后的日期
compute_day = datetime.date.today() + datetime.timedelta(days=10)
print(compute_day)
# 计算10天前的日期
compute_day = datetime.date.today() - datetime.timedelta(days=10)
print(compute_day)

# 4、计算距离当前时间10小时后、10小时前的时间
cur_time = datetime.datetime.now()
print(cur_time)
# 计算10小时后的时间
compute_time = cur_time + datetime.timedelta(hours=10)
print(compute_day)
# 计算10小时前的时间
compute_time = cur_time - datetime.timedelta(hours=10)
print(compute_day)

# 5、计算两个日期间隔多少天
day1 = datetime.datetime(2020, 2, 1)
day2 = datetime.datetime(2020, 1, 5)
interval_day = (day1 - day2).days
print(interval_day)

# %% 6、计算时间间隔, 时间差单位为秒
start_time = datetime.datetime.now()
end_time = datetime.datetime.now()
seconds = end_time - start_time
seconds1 = (end_time - start_time).seconds
print(seconds, seconds1)

# %% 7.获取上个月第一天和最后一天的日期
today = datetime.date.today()
mlast_day = datetime.date(today.year, today.month, 1) - datetime.timedelta(1)
mfirst_day = datetime.date(mlast_day.year, mlast_day.month, 1)
print(mfirst_day, mlast_day)

# %% 8.计算上周一和周日的日期
today = datetime.date.today()
today_weekday = today.isoweekday()
last_sunday = today - datetime.timedelta(days=today_weekday)
last_monday = last_sunday - datetime.timedelta(days=6)
print(last_sunday, last_monday)

# %% 9.计算指定日期当月最后一天的日期和本月天数
date = datetime.date(2017, 12, 20)


def eomonth(date_object):
    if date_object.month == 12:
        next_month_first_date = datetime.date(date_object.year + 1, 1, 1)
    else:
        next_month_first_date = datetime.date(date_object.year, date_object.month + 1, 1)
    return next_month_first_date - datetime.timedelta(1)


print(eomonth(date))
print(eomonth(date).day)
# %% 10.计算指定日期下个月当天的日期
import datetime
date = datetime.date(2017, 1, 20)
def eomonth(date_object):
    if date_object.month == 12:
        next_month_first_date = datetime.date(date_object.year + 1, 1, 1)
    else:
        next_month_first_date = datetime.date(date_object.year, date_object.month + 1, 1)
    return next_month_first_date - datetime.timedelta(1)


def edate(date_object):
    if date_object.month == 12:
        next_month_date = datetime.date(date_object.year + 1, 1, date_object.day)
    else:
        next_month_first_day = datetime.date(date_object.year, date_object.month + 1, 1)
        if date_object.day > eomonth(next_month_first_day).day:
            next_month_date = datetime.date(date_object.year, date_object.month + 1, eomonth(last_month_first_day).day)
        else:
            next_month_date = datetime.date(date_object.year, date_object.month + 1, date_object.day)
    return next_month_date
print(edate(date))
#%% 11. 获得本周一至今天的时间段并获得上周对应同一时间段
