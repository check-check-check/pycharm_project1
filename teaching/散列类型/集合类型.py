# @Time    :
# @Author  : chen
# set1 = set()
basket = {'apple', 'orange', 'apple', 'pear', 'orange', 'banana'}
print(basket)
#%% 单元内执行
test1='orange' in basket                 # fast membership testing
print(test1)
test2='crabgrass' in basket
print(test2)

# Demonstrate set operations on unique letters from two words
a = set('abracadabra')
b = set('alacazam')
print(a)   # unique letters in a
print(a-b) # letters in a but not in b
print(a|b) # letters in either a or b
print(a&b) # letters in both a and b
print(a ^ b)# letters in a or b but not both

c = {x for x in 'abracadabra' if x not in 'abc'}
print(c)
#%%