# @Time    : 
# @Author  : chen
#创建一个对象
class user:
    userName = "未命名"
    passwd = "123456"
    #定义构造函数 初始化内容
    def __init__(self,newUserName,newPasswd):
        self.userName = newUserName
        self.passwd = newPasswd
    def toString(self):
        print("名字:",self.userName,"密码：",self.passwd)

#主函数
#创建一个列表对象
objectUser = []
#创建一个序号列表菜单
memu = ["1.显示全部已注册用户","2.查找/修改/删除用户信息","3.添加新用户","4.退出系统"]
#用列表来保存语句
flag = 1
while(flag):
    print("\n用户注册信息管理系统")
    # 遍历序号菜单
    for m in memu:
        print(m)
    #获取字符串
    num = input("请输入序号选择对应菜单：")
    num = num.split(".")
    #用来接收int类型的要求命令
    askForNum = int(num[0])
    #1.显示全部已注册用户@@@@
    if(askForNum == 1):
        for num1 in objectUser:
            num1.toString()
    #2.查找/修改/删除用户信息
    elif (askForNum == 2):
        findUser = input("请输入要查找的用户")
        #去遍历objectUser 里面是否存在该用户名
        flag2 = 0
        for num2 in objectUser:
            #如果名字存在
            if(num2.userName == findUser):
                flag2 = 1
                print("用户已经注册了！！！")
                print("请选择操作\n")
                ww = print("1.修改用户\n2.删除用户\n")
                aa = input("请输入你的选择:")
                #如果是条件1.修改用户
                if(aa == "1"):
                    temp2Name = input("请输入新的用户名:")
                    temp2Passwd = input("请输入新的密码:")
                    num2.userName = temp2Name
                    num2.passwd = temp2Passwd
                    break
                # 如果是条件2.删除用户
                if(aa == "2"):
                    objectUser.remove(num2)
                    break
            #如果用户不存在
        if(flag2 == 0):
            print("该用户不存在!!!")
    #3.添加新用户 @@@@
    elif (askForNum == 3):
        newUser = input("请输入新的用户名:")
        newPass = input("请输入新的密码:")
        tempUser = user(newUser,newPass)
        objectUser.append(tempUser)
        print("已成功添加用户！")
    #4.退出系统
    elif (askForNum == 4):
        flag = 0
        print("已经退出系统!!!")
        break
    else:
        print("输入格式不对请重新输入!!!!")