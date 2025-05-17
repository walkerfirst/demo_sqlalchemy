from sqlalchemy import Column, Integer, String,DateTime,Float
from sqlalchemy.ext.declarative import declarative_base
from config import engine

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

# 将所有的表映射到数据库
# 创建所有表
Base.metadata.create_all(engine)
# 创建一个会话
