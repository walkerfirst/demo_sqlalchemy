from config import engine
from sqlalchemy.orm import sessionmaker
from create_table import Student, School
# 创建会话窗口,打开数据库连接  
Session = sessionmaker(bind=engine)
# 创建一个会话实例
db_session = Session()

#1.添加数据-正向relationship版
# stu_obj = Student(name="小明",stu2sch=School(name="oldBoybeijing"))
# db_session.add(stu_obj)
# db_session.commit()


#2.添加数据-反向reLationship版
# sch_obj = School(name="oldBoyshanghai")
# sch_obj.sch2stu =[Student(name="赵丽颖2"),Student(name="陈妍希2")]
# db_session.add(sch_obj)
# db_session.commit()


# 3.查询数据-正向relationship版
stu_obj = db_session.query(Student).filter().all()
for row in stu_obj:
    # 正向查询,其中row.stu2sch.name是学校名称
    print(row.id,row.name,row.school_id,row.stu2sch.name)  

# 4.查询数据-反向relationship版
sch_obj = db_session.query(School).filter().all()
for row in sch_obj:
    # 反向查询,其中row.sch2stu[0].name是学生名称
    print(row.name,row.sch2stu[0].name,row.sch2stu[-1].name)


# 5. 修改数据

sch_obj = db_session.query(School).filter(School.name=="oldBoybeijing").first()
db_session.query(Student).filter(Student.name=="陈妍希3").update({"school_id":sch_obj.id})
db_session.commit()
db_session.close()
