# @Time    : 
# @Author  : chen
import pymysql
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import sessionmaker

# 1.首先，创建连接数据库
engine = create_engine("mysql+pymysql://root:chenxiao5566@localhost/test", encoding='utf-8')

# 2.使用Declarative系统映射的类是根据基类定义的，换句话说每个映射类需要继承这个基类
Base = declarative_base()  # 生成orm基类


# 使用 Declarative 的类至少需要一个__tablename__属性，并且至少有一个 Column属于主键
# 3.继承基类
class User(Base):
    __tablename__ = 'user02'  # 表名
    id = Column(Integer, primary_key=True)
    name = Column(String(32))
    password = Column(String(64))
    beizhu = Column(String(64), )


class teacher(Base):
    __tablename__ = 'user01'  # 表名
    id = Column(Integer, primary_key=True)
    name = Column(String(32))
    password = Column(String(64))


# 初始化表
def init_db():
    Base.metadata.create_all(engine)


# 删除表
def drop_db():
    Base.metadata.drop_all(engine)


# 我们可以使用MetaData 为所有数据库中尚不存在的表向数据库发出CREATE TABLE语句。
# 下面，我们调用该MetaData.create_all()方法，将我们Engine 作为数据库连接源传递。
# 我们将看到首先发出特殊命令以检查user表的存在，然后是实际的语句：CREATE TABLE

# 4.创建表结构
init_db()

# 数据库中的空字符串不是 NUll, python 中的 None 存到数据库中是 NULL

user1 = User(name='root', password='CHEN123456', beizhu='')  # 此时，实例对象只是在此刻环境的内存中有效，并没有在表中真正生成数据

# 5.要想生成数据到表中，需要创建一个和数据库沟通的会话对象，利用这个会话对象对数据库中的表进行操作（增加、更新，删除、查询）
#   创建与数据库的会话session_class 。注意,这里返回给session的是个class,不是实例
Session_class = sessionmaker(bind=engine)
Session = Session_class()  # 生成session实例

user2 = User(name="test", password="123456", beizhu='')  # 生成你要创建的数据对象
print(user2.name, user2.id)  # 此时还没创建对象呢，不信你打印一下id发现还是None

Session.add(user1)
Session.add(user2)  # 把要创建的数据对象添加到这个session里， 一会统一创建
# Session.add_all([user1,user2])#等价于以上2条
print(user2.name, user2.id)  # 此时也依然还没创建

# 6.现在进行回滚操作,之后再次进行查询操作会发现已恢复到修改之前。撤销以上操作
# Session.rollback()
# 7.现此才统一提交，创建数据
Session.commit()
print(user2.name, user2.id)
# %%查询操作
# query(类名) 返回的就是对象
# query(类名.字段名) 返回的就是含有数据的元组对象
# 控制返回的查询结果集
# all() 返回的是所有的结果集，是列表
# first() 返回的是所有结果集中的第一个数据

print(Session.query(User.name, User.beizhu).all())
# 迭代查询结果集
for name, id, in Session.query(User.name, User.beizhu):
    print(name, id)

# %%给列起别名,可以使用 label() 给每个列名起别名
for row in Session.query(User.name.label('t_name')).all():
    print(row.t_name)

# %% 条件查询:filter_by() 接收的是关键字参数;
# filter()允许使用python的比较或关系运算符，实现更灵活的查询
# filter_by()的参数是**kwargs，直接支持组合查询
ret = Session.query(User.name, User.id).filter_by(name='root').all()
print(ret)

# %% filter()不支持组合查询，只能连续调用filter来变相实现
ret = Session.query(User.name, User.id).filter(User.id > 10).all()
print(ret)

# %% 关系运算符的查询
query = Session.query(User.name, User.id)
# 相等==
ret = query.filter(User.name == 'root').all()
print(ret)
# 不相等!=
ret = query.filter(User.name != 'root').all()
print(ret)
# LIKE:在某些数据库中，这个可能会不区分大小写，也有可能区分大小写
ret = query.filter(User.name.like('%ROOt%')).all()
print(ret)
# %%确保忽略大小写， 大部分数据库不支持 ilike
query.filter(User.name.ilike('ROOT')).all()

# %% in
query.filter(User.id.in_([2, 3, 5, 10])).all()
# %% not in 使用波浪号~ 表示非
query.filter(~User.id.in_([2, 3, 5, 10])).all()

# %%BETWEEN:使用 between 表示范围
query.filter(User.id.between(1, 10)).all()

# %% 数据库中的空字符串不是NUll，python 中的 None 存到数据库中是 NULL
ret = query.filter(User.beizhu == None).all()
print(ret)
# 或者
ret = query.filter(User.beizhu.is_(None)).all()
print(ret)
# %% IS NOT NULL
ret = query.filter(User.name != None).all()
print(ret)
# 或者
ret = query.filter(User.name.isnot(None)).all()
print(ret)
# %% and使用逗号或者and_
from sqlalchemy import and_, or_

ret = query.filter(User.name == 'root', User.id > 10, User.id < 18).all()
print(ret)
ret = query.filter(or_(User.name == 'root', User.name == 'root1')).all()
print(ret)
ret = query.filter(or_(User.name == 'root', and_(User.id > 10, User.id < 18))).all()
print(ret)

# %% order by 排序
# 正序
ret = Session.query(User.name, User.id).order_by(User.name).all()
print(ret)
# 倒序
ret = Session.query(User.name, User.id).order_by(User.name.desc()).all()
print(ret)
# 先按名字排序，假如有相同的再安id 排序
ret = Session.query(User.name, User.id).order_by(User.name, User.id.desc()).all()
print(ret)
ret = Session.query(User).filter(User.name == 'root').count()
print(ret)
# %% 嵌套，从最内层的查询结果中再查询想要的数据
ret = Session.query(User.id, User.name, User.beizhu).filter(
    User.id.in_(Session.query(User.id).filter_by(name='root'))).all()
print(ret)

# %%分组统计查询
from sqlalchemy.sql import func
# 统计表中所有的数据
ret = Session.query(func.count('*')).select_from(User).first()
print(ret)

# %% 以id分组，并统计每组的数据数量
ret = Session.query(func.count(User.id), User.id).group_by(User.id).all()
print(ret)
# %% 以id为分组，并统计每组的最大/最小 id 号，年龄总和/平均值，
ret = Session.query(
    func.max(User.id),
    func.min(User.id),
    func.sum(User.id),
    func.avg(User.id),
    User.id
).group_by(User.id).all()
print(ret)

# %% 从分组的数据中再查找需要的数据
Session.query(
    func.max(User.id),
    func.min(User.id),
    func.sum(User.id),
    func.avg(User.id),
    User.id).group_by(User.id).having(func.min(User.id) > 2).all()
