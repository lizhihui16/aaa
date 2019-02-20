from flask import Flask, render_template


app=Flask(__name__)


@app.route('/02-temp')
def temp():
    #渲染01-temp.html模板并响应给客户端
    str=render_template('02-temp.html',song='绿光',name='宝强',nam='羽凡',na='乃亮')
    print(str)
    return str

if __name__=='__main__':
    app.run(debug=True)