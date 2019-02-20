from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import pymysql
pymysql.install_as_MySQLdb()

app=Flask(__name__)

app.config['SQLALCHEMY_DATANASE_URI']='mysql://root:123456@localhost:3306/flask'
db=SQLAlchemy(app)

class Student(db.Model):
    __tablename__='Student'
    id=db.Column(db.Integer,primary_key=True)
    sname=db.Column(db.String(30),nullable=False)
    sage=db.Column(db.SmallInteger)


# @app.route('/')
# def index():
#     return '创建成功'


if __name__=='__main__':
    app.run(debug=True,host='0.0.0.0')