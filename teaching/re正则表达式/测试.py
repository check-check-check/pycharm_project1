# @Time    : 
# @Author  : chen
import re
print(re.findall(r'\w+', '宝元meet 12*() _'))
print(re.findall(r'\W+', '宝元meet 12*() _'))
#%%
pattern=re.compile(r"\w+")
print(pattern.match("qwer123",0,2).group())
print(pattern.match("qwer123",0,3).group())