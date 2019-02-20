from flask import Flask

#将当前运行的主程序构建Flask应用，以便接收用户的请求（request）和响应（response）
app=Flask(__name__)

#@app.route('/'):定义Flask中的路由，主要定义用户的访问路径，'/'表示的是整个网站的根路径
#def index():表示的是匹配上@app.route()的路径的处理程序－视图处理函数（views）,、
# 所有的视图处理函数必须要有一个return,必须要return一个字符串


@app.route('/')
def index():
    return "My First Flask Demo"


@app.route('/login')
def index1():
    return '欢迎访问登录页面'


#定义带参数的路由以及视图处理函数


@app.route('/show/<name>')
def show1(name):
    return '<h1>传递进来的参数为：%s</h1>'%name


@app.route('/register')
def index2():
    return "欢迎访问注册页面"

#路径：localhost:500/show/wangwc/25
@app.route('/show/<name>/<age>')
def show2(name,age):
    return '姓名：%s,年龄：%s'%(name,age)





if __name__=='__main__':
    #运行Ｆlask应用（启动False服务）默认会在本机开启5000端口，允许使用http://localhost:5000/访问Flask的web应用
    #debug=True,将运行模式更改为调试模式（开发环境中推荐使用True,生产环境中必须改为False）
    app.run(debug=True)