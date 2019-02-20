from pandas import json

from flask import Flask, request

app = Flask(__name__)


@app.route('/01-server')
def server01():
    #接受前端传递过来的参数－callback
    cd=request.args.get('callback')
    return cd+"('服务器响应的内容');"

@app.route('/02-server')
def server02():
    dic={
        'flightNO':'CA977',
        'from':'Beijing',
        'to':'LA',
        'time':'00:30'
    }
    cd=request.args.get('callback')
    jsonStr=json.dumps(dic)
    print(cd+'('+jsonStr+');')
    return cd+'('+jsonStr+');'

@app.route('/03-jq-cross')
def jq_cross():
    cd = request.args.get('callback')
    return cd+"('服务器端响应回去的数据')"

@app.route('/03-server')
def server03():
    cd=request.args.get('huidiao')
    print(cd)
    return cd+"('这是使用方案2响应的数据');"


if __name__ == '__main__':
    app.run(debug=True,host='0.0.0.0')
