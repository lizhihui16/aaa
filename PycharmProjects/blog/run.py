from flask import Flask, render_template, request, make_response, redirect

app=Flask(__name__)

@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html')



@app.route('/about')
def about_2():
    return render_template('about.html')

@app.route('/info')
def info_6():
    return render_template('info.html')

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


@app.route('/footer')
def footer_3():
    return render_template('footer.html')

@app.route('/gbook')
def gbook_4():
    return render_template('gbook.html')

@app.route('/header')
def header_5():
    return render_template('header.html')




@app.route('/photo')
def photo_9():
    return render_template('photo.html')

@app.route('/register')
def register_10():
    return render_template('register.html')

@app.route('/release')
def release_11():
    return render_template('release.html')

@app.route('/time')
def time_12():
    return render_template('time.html')



if __name__=='__main__':
    app.run(debug=True,host='0.0.0.0')