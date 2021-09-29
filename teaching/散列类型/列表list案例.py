# @Time    : 
# @Author  : chen
'''对以上内容进行一个练习：
题目：输入一年中的某一天，判断这一天是这一年的第几天：【输入格式：YYYY-MM-DD】'''
User_input = input('输入：年-月-日')
Year = int(User_input.split('-')[0])   ##得到年份
Month = int(User_input.split('-')[1])  ##得到月份
Day = int(User_input.split('-')[2])    ##得到天

li = [31,28,31,30,31,30,31,31,30,31,30,31]   ##所有平年各个月份的天数
num = 0    ##记录天数
if ((Year % 4 == 0) and (Year % 100 != 0) or (Year % 400 == 0)):    ##当润年时：
    li[1] = 29   ##将二月的天数改为29
for i in range(12):  ##遍历月份
	if Month > i + 1:   ##i从0开始，假如是5月的某一天，i循环到3停止，经过0-1-2-3四次循环，取4个月份即取1-2-3-4月的所有天
		num += li[i]   ##将1-4月总天数求和
	else:            ##退出if判断后，当下一次循环时，i=4，i+1不满足if的条件，进入else，将最后5月的第几天加入总天数中
		num += Day
		break
print('这一天是%d年的第%d天' %(Year,num))