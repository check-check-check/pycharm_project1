# @Time    : 
# @Author  : chen
#%%
str1 = 'dddredddddewws22dff43'
# 练习：取出字符串中出现2次的字符串，使用count方法统计
def two1_string(str):
    s = set()  # 创建集合
    for i in str:
        if str.count(i) == 2:
            s.add(i)
    return s


print(two1_string(str))

# 练习2：取出字符串中出现2次的字符串，使用字典统计
def two2_string(str):
    s = {}  # 创建字典
    for i in str:
        if i in s.keys():
            s[i] += 1
        else:
            s[i] = 1
    return [i for i in s if s[i] == 2]
print(two1_string(str1))
print(two2_string(str1))
# 练习3:统计出其中英文字母，空格，数字和其他字符的个数
def tongji001(str):
    letters = 0
    space = 0
    digit = 0
    others = 0
    s={}
    for i in str:
        if i.isalpha():
            letters+=1
        elif i.isspace():
            space+=1
        elif i.isdigit():
            digit+=1
        else:
            others+=1
    s['letters'] = letters
    s['space'] = space
    s['digit'] = digit
    s['others'] = others
    return s
str2 = 'gkjtrlkhgq  43678 '
print(tongji001(str2))
#问题1：如何统计大写字母 (isupper()),小写字母(islower())
#问题2：统计元音字母的个数：a,e,i,o,u
