from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

# 建立连接
engine = create_engine('mysql+mysqlconnector://username:password@localhost/database')

# 创建Session
Session = sessionmaker(bind=engine)
session = Session()

# 创建Base类
Base = declarative_base()

# 定义模型类
class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    name = Column(String(50))

# 查询数据
users = session.query(User).all()
for user in users:
    print(f"User ID: {user.id}, Name: {user.name}")

# 添加数据
new_user = User(name="John Doe")
session.add(new_user)
session.commit()

# 关闭Session
session.close()