from flask import Flask, make_response, request, render_template, session, redirect
from flask_sqlalchemy import SQLAlchemy
import pymysql
pymysql.install_as_MySQLdb()

app=Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI']='mysql://root:123456@localhost:3306/flask'
app.config['SQLALCHEMY_COMMIT_ON_TEARDOWN']=True
app.config['SECRET_KEY']='xienasdindfisaoifdnsxxxx'

db=SQLAlchemy(app)

class Login(db.Model):
    __tablename__='login'
    id=db.Column(db.Integer,primary_key=True)
    lname=db.Column(db.String(30))
    lpwd=db.Column(db.String(30))
    uname=db.Column(db.String(30))

db.create_all()


@app.route('/01-setCookie')
def setCookie():
    resp=make_response('保存cookie成功')
    #保存uname进cookie，值为wangwc
    resp.set_cookie('unane','wangwc',3600)
    return resp

@app.route('/02-getCookie')
def getCookie():
    print(request.cookies)
    uname=request.cookies.get('unane')
    return 'uname的值为:%s'% uname


@app.route('/03-login',methods=['GET','POST'])
def login():
    if request.method=='GET':
        #判断cookies中是否有uname的值
        if 'uname' in request.cookies:
            # 有uname的话，则视为保存过密码（曾经成功登录过）
            uname=request.cookies.get('uname')
            return '欢迎:'+uname
        # 没有uname的话，去往03-login.html
        else:
            return render_template('03-login.html')
    else:
        #获取用户名称和密码，并判断是否登录成功
        uname=request.form.get('uname')
        upwd=request.form.get('upwd')
        if uname=='admin' and upwd=='admin':
            resp = make_response('欢迎：' + uname)
            #判断是否记住密码
            if 'isSaved' in request.form:
                resp.set_cookie('uname', uname, 60 * 60 * 24 * 356)
            return resp
        else:
            return '登录失败'

@app.route('/04-setSession')
def setsession():
    session['uname']='Tarena'
    return '保存session成功'

@app.route('/05-getSession')
def getsession():
    if 'uname' in session:
        uname=session['uname']
        return 'uname:'+uname
    else:
        return 'session中没有相应数据'


@app.route('/06-login',methods=['POST','GET'])
def login_views():

    if request.method=='GET':
        #判断session中是否有登录信息
        if 'lname' in session and 'id' in session:
            #已经成功登录过
            return redirect('/')
        else:
            #没有在登录状态上
            #判断cookies中是否有登录信息
            if 'lname' in request.cookies and 'id' in request.cookies:
                #cookies中有登录信息，从cookies中取出数据保存进session,并重回首页
                lname=request.cookies.get('uname')
                id=request.cookies.get('id')
                session['id']=id
                session['lname']=lname
                return redirect('/')
            else:
                #cookie中也没有登录信息
                return render_template('07-login.html')
    else:

        #处理post请求
        #接受前端传递过来的数据并验证登录是否成功
        uname=request.form.get('uname')
        upwd=request.form.get('upwd')
        login=Login.query.filter(Login.lname==uname,Login.lpwd==upwd).first()
        if login:
            #登录成功
            #将信息保存进session
            session['lname'] = uname
            session['id']=login.id
            #创建响应对象
            resp=redirect('/')
            #判断是否将数据保存进cookie
            if 'isSaved' in request.form:
                mAge=60 * 60 * 24 * 356
                resp.set_cookie('id',str(login.id),mAge)
                resp.set_cookie('lname', uname,mAge )
            return resp
        else:
            #登录失败
            errMsg='用户名或密码不正确'
            return render_template('07-login.html',errMsg=errMsg)


@app.route('/')
def index():
    #登录信息的处理
    #判断session是否有登录信息
    if 'id' in session and 'lname' in session:
        lname=session.get('lname')
        return render_template('index.html',lname=lname)
    else:
        if 'id' in request.cookies and 'lname' in request.cookies:
            #cookies中有登录信息
            id=request.cookies.get('id')
            lname=request.cookies.get('lname')
            session['id']=id
            session['lname']=lname
            return render_template('index.html',lname=lname)
        else:
            #cookies中没有登录信息
            return render_template('/index.html')


@app.route('/logout')
def logout():
    resp = redirect('/')
    if 'id' in session and 'lname' in session:
        del session['id']
        del session['lname']
    if 'id' in request.cookies and 'lname' in request.cookies:
        resp.delete_cookie('id')
        resp.delete_cookie('lname')
    return resp




if __name__=='__main__':
    app.run(debug=True,host='0.0.0.0')