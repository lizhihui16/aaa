from flask import Flask, request, render_template, redirect
from flask_sqlalchemy import SQLAlchemy
import pymysql
from sqlalchemy import or_, func
pymysql.install_as_MySQLdb()
app=Flask(__name__)
#指定数据库的配置
app.config['SQLALCHEMY_DATABASE_URI']='mysql://root:123456@localhost:3306/flask'
#指定当视图执行完毕后，自动提交数据库操作
app.config['SQLALCHEMY_COMMIT_ON_TEARDOWN']=True
#指定每次执行操作时打印原始的SQL语句
# app.config['SQLALCHEMY_ECHO']=True
#创建数据库的实例
db=SQLAlchemy(app)

#创建实体类
class Users(db.Model):
    __tablename__='users'
    id=db.Column(db.Integer,primary_key=True)
    username=db.Column(db.String(80),nullable=False,unique=True)
    age=db.Column(db.Integer)
    email=db.Column(db.String(120),unique=True)
    isActive=db.Column(db.Boolean,default=True)
    #增加关联属性和反向引用关系
    wife=db.relationship('Wife',backref='user',uselist=False)

    def __init__(self,username,age,email):
        self.username=username
        self.age=age
        self.email=email

    def __repr__(self):
        return '<Users:%r>'%self.username

class Wife(db.Model):
    __tablename__='wife'
    id=db.Column(db.Integer,primary_key=True)
    wname=db.Column(db.String(30))
    #增加对Users的一对一的引用关系
    users_id=db.Column(db.Integer,db.ForeignKey('users.id'))

    def __init__(self,wname):
        self.wname=wname

class Student(db.Model):
    __tablename__='student'
    id=db.Column(db.Integer,primary_key=True)
    sname=db.Column(db.String(30),nullable=False)
    sage=db.Column(db.Integer)
    #增加对Classes的一（Classes）对多（Student）的引用关系
    classes_id=db.Column(db.Integer,db.ForeignKey('classes.id'))

    def __init__(self,sname,sage):
        self.sname=sname
        self.sage=sage

    def __repr__(self):
        return '<Student:%r>'%self.sname

class Classes(db.Model):
    __tablename__='classes'
    id=db.Column(db.Integer,primary_key=True)
    name=db.Column(db.String(30),nullable=False)
    #增加关联属性和反向引用关系
    students=db.relationship('Student',backref='classes',lazy='dynamic')

    def __init__(self,name):
        self.name=name

    def __repr__(self):
        return '<Classes:%r>'%self.name

class Teacher(db.Model):
    __tablename__='teacher'
    id=db.Column(db.Integer,primary_key=True)
    tname=db.Column(db.String(30),nullable=False)
    tage=db.Column(db.Integer)
    tbirth=db.Column(db.Date)
    #增加一个列（外键）：引用自course表的主键
    course_id=db.Column(db.Integer,db.ForeignKey('course.id'))

    def __init__(self,tname,tage,tbirth):
        self.tname=tname
        self.tage=tage
        self.tage=tage
        self.tbirth=tbirth

    def __repr__(self):
        return '<Teacher:%r>'%self.tname

class Course(db.Model):
    __tablename__='course'
    id=db.Column(db.Integer,primary_key=True)
    cname=db.Column(db.String(30),nullable=False)
    #增加关联属性和反向引用关系
    #关联属性：在course对象中通过那个属性能够得到对应的所有的teacher对象
    #反向引用：在teacher对象中通过那个属性能够得到他对应的course
    teachers=db.relationship('Teacher',backref='course',lazy='dynamic')

    def __init__(self,cname):
        self.cname=cname

    def __repr__(self):
        return '<Course:%r>'%self.cname

db.create_all()

@app.route('/01-add')
def add_views():
    #创建Users对象，并插入到数据库中
    users=Users('王老师',35,'mrwang@163.com')
    db.session.add(users)
    db.session.commit()
    return 'Add ok'

@app.route('/02-register',methods=['POST','GET'])
def register():
    if request.method=='GET':
        return render_template('02-register.html')
    else:
        #接受前端传递过来的数据
        # unam =request.form.get('uname')
        # print(unam)
        #将数据构建成实体对象
        #将数据保存回数据库
        uname =request.form['uname']
        # print(uname)
        uage=request.form['uage']
        uemail=request.form['uemail']
        users=Users(uname,uage,uemail)
        db.session.add(users)
        # db.session.commit()
        return 'OK'

@app.route('/03-query')
def query_views():
    users=db.session.query(Users).all()
    for u in users:
        print(u)
        print('姓名：%s,年龄：%s,邮箱：%s'%(u.username,u.age,u.email))
    # user=db.session.query(Users).first()
    # print(user)

    #测试查询返回部分列
    # query=db.session.query(Users.age)
    # print(query)


    #测试filter()函数
    #查询Users中年龄大于３０的人的信息
    # users=db.session.query(Users).filter(Users.age>30).all()
    # users=db.session.query(Users).filter(Users.age>30,Users.id>1).all()
    # users=db.session.query(Users).filter(or_(Users.age>30,Users.id==1)).all()
    # users=db.session.query(Users).filter(Users.email.like('%w%')).all()
    # users =db.session.query(Users).filter(Users.id.in_([2,7])).all()
    # users =db.session.query(Users).filter(Users.age.between(30,50)).all()
    # print(type(users))
    # for u in users:
    #     print('姓名：%s,年龄：%s,邮箱：%s'%(u.username,u.age,u.email))



    #filter_by
    #查询id=1的users的信息
    # users=db.session.query(Users).filter_by(id=1).first()
    # print(users)
    #

    #查询users表中的前2条数据
    # users=db.session.query(Users).limit(2).all()
    # users=db.session.query(Users).limit(2).offset(3).all()


    #先按年龄降序排序，在按id升序排序
    # users=db.session.query(Users).order_by('age desc,id asc').all()
    # users=db.session.query(Users.age).group_by('age').all()
    # print(users)



    #聚合函数
    # users=db.session.query(func.avg(Users.age).label('avgAge')).all()
    # users=db.session.query(Users.age,func.avg(Users.age),func.sum(Users.age)).group_by('age').all()
    # print(users)


    #基于Models进行的查询
    # users=Users.query.all()
    # users=Users.query.filter(Users.id>6).all()
    # users=Users.query.filter_by(id=6).all()
    #
    # for u in users:
    #     print('ID:%d,姓名：%s,年龄：%s,邮箱：%s'%(u.id,u.username,u.age,u.email))

    return "<script>alert('Query OK');</script>"

@app.route('/04-queryall')
def queryall():
    users=Users.query.filter_by(isActive=True).all()
    return render_template('04-queryall.html',users=users)

@app.route('/05-update',methods=['POST','GET'])
def update():
    if request.method=='GET':
        #接受前端传递过来的参数id
        id=request.args.get('id')
        #根据id查询出对应的对象
        user=Users.query.filter_by(id=id).first()
        #将查询出来的对象发送到05-updata.html中进行显示
        return render_template('05-update.html',user=user)
    else:
        #查
        id=request.form.get('id')
        user=Users.query.filter_by(id=id).first()
        #改
        username = request.form.get('uname')
        age = request.form['uage']
        email = request.form['uemail']
        user.username = username
        user.age=age
        user.email=email
        #保存
        db.session.add(user)
        return redirect('04-queryall')

@app.route('/07-delete')
def delete():
    id=request.args.get('id')
    user=Users.query.filter_by(id=id).first()
    # db.session.delete(user)
    #以修改来表示删除：将users的isActive的值更改为False来表示删除
    user.isActive=False
    db.session.add(user)
    return redirect('04-queryall')

@app.route('/06-update')
def update_users():
    user=Users.query.filter_by(id=7).first()
    user.username='Brother Chao'
    user.age=60
    db.session.add(user)
    return 'Update ok'

@app.route('/08-insert')
def insert_views():
    c1=Course('钢管舞')
    c2=Course('爵士舞')
    db.session.add(c1)
    db.session.add(c2)
    return 'Imsert ok'

@app.route('/09-register-teacher')
def register_teacher():
    #方案１：通过关联属性关联数据
    # tea1=Teacher('魏老师',40,'1985-10-01')
    # tea1.course_id=1
    # db.session.add(tea1)

    #方案２：通过反向引用属性关联数据
    tea2=Teacher('王老师',45,'1975-10-01')
    #查询id为1的Course的信息
    course=Course.query.filter_by(id=1).first()
    tea2.course=course
    db.session.add(tea2)
    return 'Register Teacher ok'

@app.route('/10-query')
def query10_views():
    #通过coruse对象查询对应所有的teacher们
    # course=Course.query.filter_by(id=1).first()
    #teacher提供了对应的teacher的查询
    # teachers=course.teachers.all()
    # print('课程名称：'+course.cname)
    # print('对应的老师们：')
    # for tea in teachers:
    #     print('姓名：%s,生日：%s'%(tea.tname,tea.tbirth))
    # return 'Query ok'

    #通过teacher得到对应的course
    tea=Teacher.query.filter_by(id=1).first()
    course=tea.course
    print('教师姓名：%s'% tea.tname)
    print('所教课程：%s'% course.cname)
    return 'Query ok'

@app.route('/11-register-stu',methods=['GET','POST'])
def register_stu():
    if request.method=='GET':
        #查询classes表中所有的数据
        list=Classes.query.all()
        return render_template('11-register-stu.html',list=list)
    else:
        #获取前端提交的数据
        sname=request.form.get('sname')
        sage=request.form.get('sage')
        classes_id=request.form.get('classes')
        #构建Student对象
        stu=Student(sname,sage)
        stu.classes_id=classes_id
        #将对象保存进数据库
        db.session.add(stu)
        return redirect('/12-students')

@app.route('/12-students')
def student():
    list=Student.query.all()
    return render_template('/12-students.html',list=list)


@app.route('/13-wife')
def wife_users():
    #通过wife找users
    # Wife.query.filter_by(id=1).first()
    # user=wife.user
    # print('Wife:%s'%wife.wname)
    # print('User:%s'%user.username)
    #通过users找wife
    user=Users.query.filter_by(id=2).first()
    wife=user.wife
    print('Wife:%s'%wife.wname)
    print('User:%s'%user.username)
    return 'OK'



if __name__=='__main__':
    app.run(debug=True,host='0.0.0.0')



