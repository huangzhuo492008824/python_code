#-*- coding:utf-8 -*-
from sqlalchemy import Column, String, create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class User(Base):
    __tablename__ = 'user'

    id = Column(String(20), primary_key=True)
    name = Column(String(20))

    def __repr__(self):
        return "<User(name='%s')>" % self.name

engine = create_engine('mysql+mysqlconnector://hz:redhat@127.0.0.1:3306/hz')
res = Base.metadata.create_all(engine) # 创建表user
print type(res)
# 创建DBSession类型:
DBSession = sessionmaker(bind=engine)
# 创建session对象:
session = DBSession()
# 插入一条数据
# new_user = User(id='11', name='kevin')
# session.add(new_user)
#添加或修改数据需要提交


#查询表中的数据
user = session.query(User).filter(User.name == 'kevin33')
print '32:', user[0]
user[0].name = 'kevin34'
# print user[0].id
# session.dirty
# print 'type:{}||{}'.format(type(user), user[0])
session.commit()
session.close()

