from sqlalchemy import create_engine
# 创建数据库引擎,连接到SQLite数据库
engine = create_engine('sqlite:///test.db')
# echo=True表示输出SQL语句到控制台