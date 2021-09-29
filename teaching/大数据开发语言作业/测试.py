# @Time    : 
# @Author  : chen
sum = 0
for x in range(100):
    sum = sum + x
    x = x + 1
print (sum)

#%%
a=[1,5,6,4,2,3]
for i in range(5):
    if a[i]>a[i+1]:
        a[i],a[i+1]=a[i+1],a[i]
print(a)
#%%
sum = 0
for i in range(101):
    sum = sum+i
print(sum)
#%%
x = [1,2,3]
z = []
for y in x:
    z.append(str(y))
print(",".join(z))

#%%
sum([0,1,2])
#%%
import pandas,numpy