# @Time    : 
# @Author  : chen
dic1 = {'a': 10, 'b': 12, 'c': 15, 'd': 15}
print(list(filter(lambda key: dic1[key] > 12, dic1)))
#%%
dic1 = {'a': 10, 'b': 12, 'c': 15, 'd': 15}
def fun(dic):
    dic_choose={}
    for key in dic:
        if dic[key]>12:
            dic_choose[key]=dic[key]
    return dic_choose
print(fun(dic1))
#%%
class Student:
    def __init__(self,student_name,student_sex,student_school,student_classes):

        self.student_name = student_name
        self.student_sex = student_sex
        self.student_school = student_school
        self.student_classes = student_classes
    def student_registered(self):
        student_dict = {}
        print("欢迎进入学生注册系统")
        student_name = input("注册姓名：")
        student_sex = input("性别：")
        student_school = input("学校：")
        student_class = input("班级：")
        st1 = Student(student_name,student_sex,student_school,student_class)
        student_dict["姓名"] = st1.student_name
        student_dict["性别"] = st1.student_sex
        student_dict["学校"] = st1.student_school
        student_dict["班级"] = st1.student_classes
        return student_dict
A = Student(11,11,11,11,)
print(A.student_registered())
#%%
student_dict = {}
print("欢迎进入学生注册系统")
student_name = input("注册姓名：")
student_sex = input("性别：")
student_school = input("学校：")
student_class = input("班级：")

student_dict["姓名"] = student_name
student_dict["性别"] = student_sex
student_dict["学校"] = student_school
student_dict["班级"] = student_class
print(student_dict)
#%%
x = 1
def change(a):
    global x
    x += 1
    print(x)
change(x)
#%%
print(int(5/2))
