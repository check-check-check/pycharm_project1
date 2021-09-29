# @Time    : 
# @Author  : chen
#测试1
l1 = [1, 2, 3, 4]
l2 = [2, 3, 4, 5]
l3 = zip(l1, l2)

for i in l3:
    print('for循环{}'.format(i))

l4 = [x for x in l3]
print(l4)
#测试2
l1 = [1, 2, 3, 4]
l2 = [2, 3, 4, 5]
l3 = zip(l1, l2)

l4 = [x for x in l3]
print(l4)

for i in l3:
    print('for循环{}'.format(i))