# @Time    : 
# @Author  : chen
user_list=[
    {'name':'alex','passwd':'123'},
    {'name':'linhaifeng','passwd':'123'},
    {'name':'wupeiqi','passwd':'123'},
    {'name':'yuanhao','passwd':'123'},
]

current_user={'username':None,'login':False}
def auth(auth_type='file'):
    def auth_deco(func):
        def wrapper(*args,**kwargs):
            if auth_type == 'file':
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
            elif auth_type == 'ldap':
                print('巴拉巴拉小魔仙')
                res=func(*args,**kwargs)
                return res
        return wrapper
    return auth_deco


#auth(auth_type='file')就是在运行一个函数,然后返回auth_deco,所以@auth(auth_type='file')
#就相当于@auth_deco,只不过现在,我们的auth_deco作为一个闭包的应用,外层的包auth给它留了一个auth_type='file'参数
@auth(auth_type='ldap')
def index():
    print('欢迎来到主页面')

@auth(auth_type='ldap')
def home():
    print('这里是你家')

def shopping_car():
    print('查看购物车啊亲')

def order():
    print('查看订单啊亲')

# print(user_list)
index()
# print(user_list)
home()