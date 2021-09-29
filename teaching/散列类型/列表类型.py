# @Time    : 
# @Author  : chen
#%%创建列表

service = ['http','ssh','ftp']
# 1.1：索引
print(service[1])    ##输出第二个元素，ssh
print(service[-1])   ##输出最后一个元素，ftp


#%%1.2：切片

print(service[1:])   ##打印第一个元素之后的内容
print(service[:-1])  ##打印最后一个元素之前的内容
print(service[::-1])  ##倒序输出

#%%1.3：重复

print(service * 3)   ##输出三遍

#%%1.4：连接

service1 = ['nfs','samba']
print(service + service1)

#%%1.5：成员操作赋

print('htt' in service)

#%%1.6：迭代:[for循环遍历]

for i in service:
    print(i)
#%%
for x, y in [(5, 2), (5, -2), (-5, 2),]:
    print('{:4d}  {:4d}'.format(x, y,))
#%%1.7列表里嵌套列表

service2 = [['abc','def','www'],[1,2,3],['mike','tony','sun']]
print(service2[2][1])   ##第三个元素中的第二个元素
print(service2[:][1])   ##第二个元素

#%%
for x, y in [(5, 2), (5, -2), (-5, 2),]:
    print('{:4.1f}  {:4.1f}  {:5.2f}  {:5.2f}'.format(x, y, x % y, math.fmod(x, y),))

