from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import pymysql
pymysql.install_as_MySQLdb()

app=Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI']='mysql://root:123456@localhost:3306/flask'
app.config['SQLALCHEMY_COMMIT_ON_TEARDOWN']=True

db=SQLAlchemy(app)

class Users(db.Model):
    __tablename__='users'
    id=db.Column(db.Integer,primary_key=True)
    username=db.Column(db.String(80),nullable=False,unique=True)
    age=db.Column(db.Integer)
    email=db.Column(db.String(120),unique=True)
    isActive=db.Column(db.Boolean,default=True)
    #添加多（Users）对多(Goods)的关联属性和反向应用关系
    #涉及到第三张关联表－users_goods
    goods=db.relationship('Goods',secondary='users_goods',lazy='dynamic',backref=db.backref('users',lazy='dynamic'))
    #增加对UsersGoods的关联属性和反向引用关系：目的是为了创建Users类与UsersGoods类之间的关系
    userGoods=db.relationship('UsersGoods',backref='user',lazy='dynamic')

class Goods(db.Model):
    __tablename__='goods'
    id=db.Column(db.Integer,primary_key=True)
    gname=db.Column(db.String(80))
    gprice=db.Column(db.Float)
    #增加对UsersGoods的关联属性和反向引用关系：目的是为了创建Goods类与UsersGoods类之间的关系
    goodUsers = db.relationship('UsersGoods', backref='good', lazy='dynamic')

#创建users_goods的第三张关联表，从而来表示多对多的关系
class UsersGoods(db.Model):
    __tablename__='users_goods'
    id=db.Column(db.Integer,primary_key=True)
    users_id=db.Column(db.Integer,db.ForeignKey('users.id'))
    goods_id=db.Column(db.Integer,db.ForeignKey('goods.id'))
    count=db.Column(db.Integer,default=1)

db.create_all()

@app.route('/01-users-goods')
def users_goods_views():
    # #为１号用户购买１号商品
    user=Users.query.filter_by(id=1).first()
    good=Goods.query.filter_by(id=1).first()
    #将good商品增加到user所购买的商品列表中
    user.goods.append(good)
    #将user更新回数据库
    db.session.add(user)

    #为１号用户购买２号商品
    ug=UsersGoods()
    ug.users_id=1
    ug.goods_id=2
    ug.count=5
    db.session.add(ug)
    return 'ok'


@app.route('/02-remove-goods')
def remove_goods():
    #获取id＝１的Users信息
    user=Users.query.filter_by(id=1).first()
    #获取id＝１的Goods信息
    good = Goods.query.filter_by(id=1).first()
    #将good从user中移除出去
    user.goods.remove(good)
    db.session.add(user)
    return 'Remove ok'


@app.route('/03-query-goods')
def query_goods():
    #查询１号用户购买的商品
    user=Users.query.filter_by(id=1).first()
    goods=user.goods.all()
    print('用户姓名:%s'%user.username)
    for g in goods:
        print('商品名称:%s'%g.gname)
        #查询每个商品的购买数量
        count=user.userGoods.filter_by(goods_id=g.id).first().count
        print('购买数量：%d'%count)
    #购买２号商品的用户
    good=Goods.query.filter_by(id=2).first()
    users=good.users.all()
    print('商品名称:%s'% good.gname)
    for u in users:
        print('用户姓名:%s'% u.username)
        coun=good.goodUsers.filter_by(users_id=u.id).first().count
        print('购买数量%d'%coun)
    return 'ok'

if __name__=='__main__':
    app.run(debug=True,host='0.0.0.0')