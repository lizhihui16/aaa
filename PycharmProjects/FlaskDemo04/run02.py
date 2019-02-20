import os

import datetime
from flask import Flask, request, render_template

app=Flask(__name__)

@app.route('/01-file',methods=['GET','POST'])
def file_views():
    if request.method=="GET":
        return render_template('01-file.html')
    else:
        #处理的上传的文件
        #1.得到上传文件
        f=request.files['uimg']
        #2.将文件保存进指定的目录处
        # print(f.filename)
        # f.save('static/'+f.filename)

        #3.将文件保存进指定的目录处[绝对路径]
        #获取当前文件的所在目录名
        # basedir=os.path.dirname(__file__)
        # # print('当前文件所在目录的绝对路径'+basedir)
        # upload_path=os.path.join(basedir,'static',f.filename)
        # # print('完整的上传路径：'+upload_path)
        # f.save(upload_path)

        basedir=os.path.dirname(__file__)
        # print('当前文件所在目录的绝对路径'+basedir)
        #获取当前的时间拼成字符串，在拼上扩展名
        ftime=datetime.datetime.now().strftime('%Y%m%d%H%M%S%f')
        # print('时间字符串:'+ftime)
        ext=f.filename.split('.')[1]
        filename=ftime+'.'+ext
        upload_path=os.path.join(basedir,'static',filename)
        # print('完整的上传路径：'+upload_path)
        f.save(upload_path)

        return 'Save ok'



if __name__=='__main__':
    app.run(debug=True,host='0.0.0.0')