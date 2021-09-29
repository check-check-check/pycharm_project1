# @Time    : 
# @Author  : chen

import random

def roll_selec():
    select_num = random.randint(1,6)
    return select_num

def main():

    try_times = eval(input('请输入您要模拟投掷骰子的总次数：'))
    list_1 = [0] * 6
    for i in range(try_times):
        result = roll_selec()
        for j in range(1,7):
            if result == j:
                list_1[j - 1] += 1
    for k,x in enumerate(list_1):
        print('点数{}模拟的次数为{}，概率为{}'.format(k+1,x,float(x/try_times)))

if __name__ == '__main__':
    main()
