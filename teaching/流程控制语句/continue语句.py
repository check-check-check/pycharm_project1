# @Time    : 
# @Author  : chen
# %% 当执行到 continue 语句时，将不再执行本次循环中 continue 语句接下来的部分，而是继续下一次循环
lst = [7, 8, 9, 4, 5, 6]
for i in range(len(lst)):
    if lst[i] == 9:
        pass
    else:
        print('****************')
        continue

    print(i,lst[i])

# %% 当存在嵌套循环时
lst = [7, 8, 9, 4, 5, 6]
for i in range(2):
    for j in range(len(lst)):
        if lst[j] == 4:
            continue  # 跳出本次循环，进入下一层循环
        print(lst[j], end=" ")#print函数默认以"\n"结尾，end参数表示以" "(空格)结尾
    print(i)
#%%
for letter in 'Python':
    if letter == 'h':
        continue
    print('当前字母 :', letter)

#%%
var = 10
while var > 0:
    var = var - 1
    if var == 5:
        continue
    print('当前变量值 :', var)

print("Good bye!")
