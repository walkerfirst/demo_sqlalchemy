# 通过sqlaclchemy 对数据库的增删改查

from create_table import User, Base
from config import engine
from sqlalchemy.orm import sessionmaker
from datetime import datetime

# 创建会话窗口,打开数据库连接
Session = sessionmaker(bind=engine)

# 创建一个会话实例
session = Session()

1. # 添加数据
def add_user(username, password):
    """添加用户"""
    new_user = User(username=username, password=password, created_at=datetime.now())
    session.add(new_user)
    session.commit()
    print(f"User {username} added.")

# 2. 查询数据
def get_user_by_username(username):
    """根据用户名查询用户"""
    user = session.query(User).filter_by(username=username).first()
    return user

# 3. 更新数据  
def update_user_password(username, new_password):
    """更新用户密码"""
    user = get_user_by_username(username)
    if user:
        user.password = new_password
        session.commit()
        print(f"Password for {username} updated.")
    else:
        print(f"User {username} not found.")
# 4. 删除数据
def delete_user(username):
    """删除用户"""
    user = get_user_by_username(username)
    if user:
        session.delete(user)
        session.commit()
        print(f"User {username} deleted.")
    else:
        print(f"User {username} not found.")
# 5. 关闭会话
def close_session():
    """关闭会话"""
    session.close()
    print("Session closed.")
# 6. 测试函数
if __name__ == "__main__":
    # 添加用户
    add_user("testuser", "password123")
    
    # 查询用户
    user = get_user_by_username("testuser")
    if user:
        print(f"User found: {user.username}, Password: {user.password}")
    
    # 更新用户密码
    update_user_password("testuser", "newpassword456")
    
    # 删除用户
    # delete_user("testuser")
    
    # 关闭会话
    close_session()