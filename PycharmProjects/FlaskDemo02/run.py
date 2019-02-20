from flask import Flask, render_template


app=Flask(__name__)


@app.route('/00-temp')
def temp():

    # dic={
    #     'title' :'绿光',
    #     'author' : '宝强',
    #     'music' : '羽凡',
    #     'singer' : '乃亮',
    # }
    # #渲染01-temp.html模板并响应给客户端
    # return render_template('00-temp.html',params=dic)

    title ='绿光'
    author = '宝强'
    music = '羽凡'
    singer = '乃亮'
    print(locals())
    return render_template('00-temp.html',params=locals())


if __name__=='__main__':
    app.run(debug=True)