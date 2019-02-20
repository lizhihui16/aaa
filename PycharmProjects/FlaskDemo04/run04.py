from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import pymysql
pymysql.install_as_MySQLdb()

app=Flask(__name__)
#为app指定数据库的配置信息
app.config['SQLALCHEMY_DATABASE_URI']='mysql://root:123456@localhost:3306/flask'
#创建SQLALchemy的数据库实例
db=SQLAlchemy(app)


#创建一个模型类－Users,映射到数据库叫ｕｓｅｒｓ表
#创建字段id,主键，自增
#创建字段usename,长度为80的字符串并且不允许为空，值唯一
#创建字段age,整数
#创建字段email,长度为１２０的字符串，必须唯一
class Student(db.Model):
    __tablename__='student'
    id=db.Column(db.Integer,primary_key=True)
    sname=db.Column(db.String(30),nullable=False)
    sage=db.Column(db.Integer)


class Teacher(db.Model):
    __tablename__='teacher'
    id=db.Column(db.Integer,primary_key=True)
    tname=db.Column(db.String(30),nullable=False)
    tage=db.Column(db.Integer)
    tbirth=db.Column(db.Date,nullable=True)


class Course(db.Model):
    __tablename__='course'
    id=db.Column(db.Integer,primary_key=True)
    cname=db.Column(db.String(30),nullable=False)

#将创建好的实体类映射回数据库
db.create_all()



@app.route('/')
def index():
    print(db)
    return '创建db成功'




if __name__=='__main__':
    app.run(debug=True,host='0.0.0.0')