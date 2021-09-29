# @Time    : 
# @Author  : chen
Zhan = []  ##定义栈列表

t = []   ##定义出栈临时栈列表

while True:
    print("""
        菜单
        1.入栈
        2.出栈
        3.查看栈顶元素
        4.查看栈长度
        5.查看栈中元素
        6.退出""")
    choice = input('请输入选择: ')
    if choice == '1':
        Aim_Name = input('请输入要入栈的元素名： ')
        Zhan = Zhan+[Aim_Name]
        print('入栈成功!')
    elif choice == '2':
        Del_Name = input('请输入要出栈的元素名： ')
        if Del_Name in Zhan:
            Length = len(Zhan)
            if Zhan.index(Del_Name) == Length-1:   #如果为栈顶元素
                Zhan.pop()
            else:   #不为栈顶元素
                SuoYin = Zhan.index(Del_Name)
                for i in range(Length-1-SuoYin):   #将要出栈元素后面的元素先保留
                    t.append(Zhan.pop())    #原栈中最后一个元素变为了第一个，顺序颠倒
                Zhan.pop()   #目标出栈
                Zhan = Zhan+t[::-1]  #将目标元素后的其他元素移回栈中
        else:
            print('栈中没有%s' %Del_Name)
    elif choice == '3':
        Zhan_Top = Zhan[-1]
        print('栈顶元素为：%s' %Zhan_Top)
    elif choice == '4':
        Length = len(Zhan)
        print('栈的长度为%s' %Length)
    elif choice == '5':
        print(Zhan)
    elif choice == '6':
        exit()
    else:
        print('请输入正确的选项！')
    print('\n')