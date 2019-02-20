import datetime
import os

from flask import Flask, request, render_template

app=Flask(__name__)

@app.route('/02-file',methods=['POST','GET'])
def file_1():
    if request.method=='GET':
        return render_template('02-file.html')
    else:
        f=request.files['uimg']
        basedir=os.path.dirname(__file__)
        ftime=datetime.datetime.now().strftime('%Y%m%d%H%M%S%f')
        # print('时间字符串:'+ftime)
        ext=f.filename.split('.')[1]
        filename=ftime+'.'+ext
        upload_path=os.path.join(basedir,'static/upload',filename)
        # print('完整的上传路径：'+upload_path)
        f.save(upload_path)
        return 'Save ok'

if __name__=='__main__':
    app.run(debug=True,host='0.0.0.0')