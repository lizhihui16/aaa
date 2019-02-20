# create database db5;
# #show create database db5;

# use db5;

# create table t1(
# id int primary key auto_increment,
# name varchar(20),
# score float(5,2)
# )charset=utf8;

# insert into t1 values
# (1,'李白',60),
# (2,'杜甫',70),
# (3,'白居易',80)

# #在db5库中t1表插入１条记录，‘王伟’，８０
# import pymysql
# # 创建数据库连接对象

# db=pymysql.connect(host='localhost',
#                     user='root',
#                     password='123456',
#                     database='db5',
#                     charset='utf8')
# #创建游标对象（利用数据库对象）
# cursor=db.cursor()
# #执行SQL命令(利用游标对象)
# cursor.execute('insert into t1 values(5,"王维",80);')
# #提交到数据库执行（commit())
# db.commit()
# print('ok')
# #关闭游标对象
# cursor.close()
# #关闭数据库对象
# db.close()

#在t1表中增加１条记录
#在t1表中把李白的成绩改为１００分
#在t1表中删除１条记录

# import pymysql
# db=pymysql.connect(host='localhost',
#                     user='root',
#                     password='123456',
#                     database='db5',
#                     charset='utf8')
# cursor=db.cursor()
# try:
#     s='insert into t1(name,score) values("李智慧",100)'
#     cursor.execute(s)
    
#     m='update t1 set score=100 where name="李白"'
#     cursor.execute(m)
    
#     n='delete from t1 where name="李智慧"'
#     cursor.execute(n)
#     print('ok')
# except Exception as e:
#     db.rollback()
#     print("Failed",e)
# db.commit()

# cursor.close()
# db.close()



# import pymysql
# db=pymysql.connect(host='localhost',
#                     user='root',
#                     password='123456',
#                     database='db5',
#                     charset='utf8')
# cursor=db.cursor()
# try:
#     sel='select * from t1'
#     cursor.execute(sel)
#     #取走游标对象中第一条的表记录
#     data1=cursor.fetchone()
#     print(data1)
#     print('*'*40)

#     data2=cursor.fetchmany(2)
#     print(data2)
#     print('*'*40)
#     #取走游标对象中剩下的表记录
#     data3=cursor.fetchall()
#     print(data3)
# except Exception as e:

#     print("Failed",e)
# cursor.close()
# db.close()



#sql语句参数化
import pymysql
db=pymysql.connect(host='localhost',
                    user='root',
                    password='123456',
                    database='db5',
                    charset='utf8')
cursor=db.cursor()
while True:
    c=input('按q退出，按回车输入学生信息')
    if c.strip().lower()=='q':
        break
    name=input('请输入姓名')
    score=input('请输入成绩')
    try:
        cursor.execute('insert into t1(name,score) values(%s,%s)',[name,score])
        db.commit()
        print('ok')
    except Exception as e:
        db.rollback()
        print("Failed",e)
cursor.close()
db.close()






























