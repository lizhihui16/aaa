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
class Usert(db.Model):
    __tablename__='users'
    id=db.Column(db.Integer,primary_key=True)
    usename=db.Column(db.String(80),nullable=False,unique=True)
    age=db.Column(db.Integer)
    email=db.Column(db.String(120),unique=True)

#将创建好的实体类映射回数据库
db.create_all()



@app.route('/')
def index():
    print(db)
    return '创建db成功'




if __name__=='__main__':
    app.run(debug=True,host='0.0.0.0')