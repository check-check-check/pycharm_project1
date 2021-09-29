# @Time    : 
# @Author  : chen
import sys
import os
os.system('clear')
mess = '''
             \033[;35m ID   :%s\033[0m
             \033[;35m Name :%s\033[0m
             \033[;35m Dep  :%s\033[0m
'''
info = '''
                     \033[;32m+++++++++++++++++++++++++++++++++++++++++++\033[0m
                     \033[;32m++  Welcome to staffs infomation system  ++\033[0m
                     \033[;32m+-----------------------------------------+\033[0m
                     \033[;32m+                                         +\033[0m
                     \033[;32m+       S: search staffs infomation       +\033[0m
                     \033[;32m+       U: update staffs infomation       +\033[0m
                                 \033[;32m+       Q: quit                           +\033[0m
                                 \033[;32m+                                         +\033[0m
                     \033[;32m+++++++++++++++++++++++++++++++++++++++++++\033[0m
'''
info2 = '''
                                 \033[;32m+++++++++++++++++++++++++++++++++++++++++++\033[0m
                                 \033[;32m+       A: Add staffs infomation          +\033[0m
                                 \033[;32m+       D: Del staffs infomation          +\033[0m
                                 \033[;32m+       Q: quit                           +\033[0m
                                 \033[;32m+++++++++++++++++++++++++++++++++++++++++++\033[0m
'''
while True:
    username = input('\033[;32mPlease input your name: \033[0m').strip()
    passwd = input('\033[;32mPlease input password: \033[0m').strip()
    if username != 'zhaohh' or passwd != '111111':
        print ('\033[;31mYour username not exist or your password wrong!\033[0m')
        continue
    else:
        print('\033[;32mHello zhaohh,Welcome!\033[0m')
        break
os.system('sleep 2')
os.system('clear')
print(info)
while True:
    user_input = input("\033[;32mPlease select (S,U,default Q): \033[0m").strip()
# search staffs infomation
    if user_input == "s" or user_input == "S":
        staff_list = open("file.txt","rw")
        c = staff_list.readlines()
        staff_list.close()
        while True:
            inputs = input('\033[;32mPlease input ID or name or dep: \033[0m').strip()
            for line in c:
                field = line.split()
                if inputs in field:
                    print(mess %(field[0],field[1],field[2]))
                    break
            else:
                juge = input('\033[;31mCan not found information! Continue? yes/no. \033[0m').strip()
                if juge == 'yes' or juge == 'y':
                    continue
                else:break
            juge = input('\033[;32mContinue search ? yes/no. \033[0m')
            if juge == 'yes' or juge == 'y':
                continue
            elif juge == 'no' or juge == 'n' or juge == '':
                sys.exit()
            break
        break
# add staffs infomation
    elif user_input == "u" or user_input == "U":
        print(info2)
        while True:
            update_input = input('\033[;32mPlease select (A,D,default Q): \033[0m').strip()
            if update_input == "a" or update_input == "A":
                info_input = input("\033[;32mPlease input user infomation: \033[0m")
                staff_list = open("file.txt","a")
                staff_list.write(info_input + '\n')
                staff_list.close()
                juge = input('\033[;32mUpdate successful! Continue search ? yes/no. \033[0m')
                if juge == 'yes' or juge == 'y':
                    continue
                elif juge == 'no' or juge == 'n' or juge == '':
                    sys.exit()
# delete staffs infomation
            elif update_input == "d" or update_input == "D":
                inputs = input('\033[;32mPlease input ID or name or dep: \033[0m')
                f = open("newfile.txt","a")
                staff_list = open("file.txt","rw")
                for line in staff_list.readlines():
                    for field in line.split():
                        if inputs == field:
                            print('\033[;32mDelete successful!\033[0m')
                            break
                    else:
                        f.write(line)
                staff_list.close()
                f.close()
                os.remove('file.txt')
                os.rename('newfile.txt','file.txt')
                juge = input('\033[;32mContinue? yes/no. \033[0m')
                if juge == 'yes' or juge == 'y':
                    continue
                elif juge == 'no' or juge == 'n' or juge == '':
                    sys.exit()
            elif update_input == "q" or update_input == "Q" or update_input == "":
                sys.exit()
            else:
                print("\033[;31m Input error,try agin!\033[0m")
                continue
    elif user_input == "q" or user_input == "Q" or user_input == "":
        sys.exit()
    else:
        print("\033[;31m Input error,try agin!\033[0m")
        continue