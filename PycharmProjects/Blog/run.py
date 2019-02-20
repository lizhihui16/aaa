from flask import Flask, render_template, request, redirect, make_response

app = Flask(__name__)

# 访问路径 http://localhsot:5000/
@app.route('/')
def index():
    return render_template('index.html')

#访问路径　http://localhost:5000/list
@app.route('/list')
def list():
    return render_template('list.html')


@app.route('/login',methods=['GET','POST'])
def login():
    if request.method=='GET':
        #去看login.html模板
        return render_template('login.html')
    else:
        #接受前端请求提交的数据
        username=request.form['username']
        password=request.form['password']
        #如果用户名是admin并且密码也是admin，去/路径
        if username=='admin' and password=='admin':
            #登录成功，重定向到'/'
            return redirect('/')
        else:
            #使用响应对象输出‘用户名或密码不正确’
            resp=make_response('用户名或密码不正确')
            return resp

if __name__ == "__main__":
    app.run(debug=True,host='0.0.0.0')