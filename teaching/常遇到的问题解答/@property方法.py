# @Time    : 
# @Author  : chen
"""标准格式如下：
@property
def password(self):
    raise AttributeError('password is not a readable attribute')

@password.setter
def password(self, password):
    self.password_hash = generate_password_hash(password)
"""
# @property的用法及含义全面解析 https://www.cnblogs.com/sgfg-1314/p/10110680.html
#%% 用代码来举例子更容易理解,比如一个学生成绩表定义成这样
class Student(object):

    def get_score(self):
        return self._score

    def set_score(self, value):
        if not isinstance(value, int):
            raise ValueError('score must be an integer!')
        if value < 0 or value > 100:
            raise ValueError('score must between 0 ~ 100!')
        self._score = value
# 我们调用的时候需要这么调用:
s = Student()
s.set_score(60) # ok!
print(s.get_score())
print(s.set_score(9999))

"""但是为了方便,节省时间,我们不想写s.set_score(9999)啊,直接写s.score = 9999不是更快么,加了方法做限制不能让调用的时候
变麻烦啊,@property快来帮忙…."""

#%%
class Student(object):

    @property
    def score(self):
        return self._score

    @score.setter
    def score(self,value):
        if not isinstance(value, int):
            raise ValueError('分数必须是整数才行呐')
        if value < 0 or value > 100:
            raise ValueError('分数必须0-100之间')
        self._score = value
s = Student()
s.score = 60 # OK，实际转化为s.set_score(60)
print(s.score) # OK，实际转化为s.get_score()
s.score = 9999
print(s.score)

