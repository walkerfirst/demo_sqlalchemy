from sqlalchemy import Column, Integer, String,DateTime,Float,ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from config import engine
from sqlalchemy.orm import relationship

# 创建一个基类，用于声明模型类
Base = declarative_base()

class User(Base):
    """用户表"""
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True, autoincrement=True)
    username = Column(String, unique=True,index=True)
    password = Column(String)
    created_at = Column(DateTime)
    def as_dict(self):
        """将对象转换为字典"""
        return {
            'id': self.id,
            'username': self.username,
            'password': self.password,
            'created_at': self.created_at
        }

class Student(Base):
    __tablename__="students"
    id = Column(Integer, primary_key=True) 
    name = Column(String(32),unique=True)
    school_id =Column(Integer,ForeignKey("schools.id")) 
    stu2sch = relationship("School", back_populates="sch2stu")  # 注意类名大小写

class School(Base):
    __tablename__="schools"
    id = Column(Integer, primary_key=True) 
    name = Column(String(32),unique=True)
    sch2stu = relationship("Student", back_populates="stu2sch")  # 双向配置

# 将所有的表映射到数据库
# 创建所有表
Base.metadata.create_all(engine)
# 创建一个会话
