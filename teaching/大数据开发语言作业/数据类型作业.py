# @Time    : 
# @Author  : chen
# %% 第1题：已知字符串 s = "my,name,is,zhangsan",请用两种办法取出之间的“name”字符。
s = "my,name,is,zhangsa"

str1 = s[3:7]
str2 = s.split(',')[1]
print(s.split(','))
str3 = s[-16:-12]
# 0~len(s)
# -1~-len(s)-1

# %% 第二题：修改字符串s = "my,name,is,zhangsan",把zhangsan改成你的名字。
# 方法1
s = "my,name,is,zhangsan"
s1 = s.replace('zhangsan', 'lisi')
print(s1)
print(s)  # replace方法不会改变原字符串
s = s.replace('zhangsan', 'lisi')  # 如果是需要对原字符串进行替换，可以这样写，重新赋值
print(s)
# 方法2
s = "my,name,is,zhangsan"
s = s[0:11] + 'lisi'
print('方法2:', s)

# %%第三题： bool("1" ==1) 的结果是什么？请解释原因。
print(bool("1" == 1))  # "1"是字符串类型，1是数字类型

# %% 第四题：已知如下变量：a = "字符串拼接1",b = "字符串拼接2",请用四种以上的方式将a与b拼接成字符串c。
a = "字符串拼接1"
b = "字符串拼接2"
c1 = a + b
c2 = '{}{}'.format(a, b)
c3 = ''.join([a, b])
print(c1,c2,c3)
c4 = '%s%s' % (a, b)
c5 = F"{a}{b}"  # 或者 f"{a}{b}"

# 面向对象模板拼接
from string import Template

s = Template('${s1}${s2}')
c6 = s.safe_substitute(s1=a, s2=b)
print(c6)

# %% 第五题：已知字符串a = "i,am,a,boy,in,china"。
a = "i,am,a,boy,in,china"
# （1）boy和china是随时可能变换的，变为可配置的
str1 = "i,am,a,%(sex)s,in,%(country)s" % {'sex': 'girl', 'country': 'china'}
str2 = "i,am,a,{sex},in,{country}".format(sex='girl', country='india')
# （2）请使用2种办法取出其间的字符"boy"和"china"；
print(a.split(',')[3], a.split(',')[5])
print(a[7:10], a[-5:])
#%%
# （3） 请找出第一个"i"出现的位置。
a = "i,am,a,boy,in,china"
print(a.find('i'))
print(a.index('i'))
# 找出第2个"i"出现的位置
print(a.find('i', a.find('i')+1))
# （4）请找出"china"中的"i"字符在字符串a中的位置。
print(a.find('i', 14))
print(a.find('i', a.find('china')))
print(a.rfind('i'))
# （5）请计算该字符串一共有几个逗号
print(a.count(','))

# %% 第6题：用列表推导式生成100内的大于20的偶数
a = [i for i in range(20, 100) if i % 2 == 0]
print(a)

# %%第7题：利用列表推导完成下面习题：
# 输出结果：[1 love python,2 love python,3 love python,…. 10 love python]
# 方法一：
print(['%s love python' % s for s in range(1, 11)])
# 方法二：
print(['{} love python'.format(i) for i in range(1, 11)])

# %%第8题：有一个元组 a = (1,2,3)，现在想修改1为11怎么做（元组是不可修改的）？
# 思路：将元组转化为列表，修改，然后在讲列表转化为元组即可；
a = (1, 2, 3)
a = list(a)
a[0] = 11
a = tuple(a)
print(a)

# %%第9题：已知字典：ainfo = {'ab':'liming','ac':20}。
# （1）使用2个方法，输出的结果：ainfo = {'ab':'liming','ac':20,'sex':'man','age':20}
ainfo = {'ab': 'liming', 'ac': 20}

ainfo['sex'] = 'man'
ainfo['age'] = 20

ainfo.update({'sex': 'man'})
ainfo.update({'age': 20})

#%% （2）输出结果：['ab','ac']；
ainfo = {'ab': 'liming', 'ac': 20}
print(ainfo.keys())
print(list(ainfo.keys()))

# （3）输出结果：['liming',20]；
ainfo = {'ab': 'liming', 'ac': 20}
print(ainfo.values())

# （4）通过2个方法返回键名ab对应的值。
print(ainfo.get('ab'))
print(list(ainfo.values())[0])

# %% （5）通过2个方法删除键名ab对应的值。
ainfo = {'ab': 'liming', 'ac': 20}
# 方法一:
del ainfo['ab']
print(ainfo)
# 方法二:
ainfo = {'ab': 'liming', 'ac': 20}
ainfo.pop('ab')
print(ainfo)

# %% 第10题：列表a = [11,22,24,29,30,32]
# 1.把28插入到列表的末端
a = [11, 22, 24, 29, 30, 32]
a.append(28)
print(a)
# 2.在元素29后面插入元素57
a.insert(4, 57)
print(a)
# 3.把元素11修改成6
a = [11, 22, 24, 29, 30, 32, 28]
a[0] = 6
print(a)
# 4.删除元素32
a = [11, 22, 24, 29, 30, 32, 28]
a.remove(32)  # 删除第一个元素
print(a)

# 或者删除所有符合条件的元素
for i in a:
    if i == 32:
        a.remove(i)
print(a)

# %%5.对列表从小到大排序,从大到小排列
a = [11, 22, 24, 29, 30, 32, 28]
a.sort()
print(a)
a.reverse()
print(a)

# 或者用一下方法
a = [11, 22, 24, 29, 30, 32, 28]
a.sort(reverse=True)  # 降序
print(a)
