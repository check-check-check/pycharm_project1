# @Time    : 
# @Author  : chen
inuser = input('UserName: ')
inpasswd = input('Password: ')
users = ['root', 'westos']
passwds = ['123', '456']

if inuser == 'admin' and inpasswd == 'admin':
    while True:
        print("""
            菜单
        1.添加会员信息
        2.删除会员信息
        3.查看会员信息
        4.退出
        """)
        choice = input('请输入选择： ')
        if choice == '1':
            Add_Name = input('要添加的会员名: ')
            Add_Passwd = input('设置会员的密码为： ')
            users = users + [Add_Name]
            passwds = passwds + [Add_Passwd]
            print('添加成功！')

        elif choice == '2':
            Remove_Name = input('请输入要删除的会员名： ')
            if Remove_Name in users:
                Remove_Passwd = input('请输入该会员的密码： ')
                SuoYinZhi = int(users.index(Remove_Name))
                if Remove_Passwd == passwds[SuoYinZhi]:
                    users.remove(Remove_Name)
                    passwds.pop(SuoYinZhi)
                    print('成功删除！')
                else:
                    print('用户密码错误,无法验证身份,删除失败')
            else:
                print('用户错误！请输入正确的用户名')
        elif choice == '3':
            print('查看会员信息'.center(50,'*'))
            print('\t用户名\t密码')
            usercount = len(users)
            for i in range(usercount):
                print('\t%s\t%s' %(users[i],passwds[i]))
        elif choice == '4':
            exit()
        else:
            print('请输入正确选择！')