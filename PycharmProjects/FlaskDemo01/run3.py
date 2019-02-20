from flask import Flask, render_template

app=Flask(__name__)


@app.route('/01-temp')
def temp():
    #渲染01-temp.html模板并响应给客户端
    str=render_template('01-temp.html',name='李',age=18)
    print(str)
    return str


@app.route('/03-createElement-exer')
def temp1():
    #渲染01-temp.html模板并响应给客户端
    str1=render_template('03-createElement-exer.html')
    print(str1)
    return str1


if __name__=='__main__':
    app.run(debug=True)