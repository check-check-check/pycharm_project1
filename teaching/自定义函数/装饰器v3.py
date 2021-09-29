# @Time    : 
# @Author  : chen
user_list=[
    {'name':'alex','passwd':'123'},
    {'name':'linhaifeng','passwd':'123'},
    {'name':'wupeiqi','passwd':'123'},
    {'name':'yuanhao','passwd':'123'},
]

current_user={'username':None,'login':False}

def auth_deco(func):
    def wrapper(*args,**kwargs):
        if current_user['username'] and current_user['login']:
            res=func(*args,**kwargs)
            return res
        username=input('用户名: ').strip()
        passwd=input('密码: ').strip()

        for index,user_dic in enumerate(user_list):
            if username == user_dic['name'] and passwd == user_dic['passwd']:
                current_user['username']=username

                current_user['login']=True
                res=func(*args,**kwargs)
                return res
                break
        else:
            print('用户名或者密码错误,重新登录')

    return wrapper

@auth_deco
def index():
    print('欢迎来到主页面')

@auth_deco
def home():
    print('这里是你家')

def shopping_car():
    print('查看购物车啊亲')

def order():
    print('查看订单啊亲')

print(user_list)
# index()
print(user_list)
home()