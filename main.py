from flask import Flask, request
from service import *

app = Flask(__name__)

@app.route('/new',methods=['POST'])
def fun_new():
    params = request.get_json()
    cutName = params.get('cutName', None)
    public = params.get('public', True)
    pwd = params.get('pwd', '')
    content = params.get('content','')
    ret = newCut(cutName, public, pwd, content)
    return ret

@app.route('/save',methods=['POST'])
def fun_save():
    params = request.get_json()
    cutName = params.get('cutName', None)
    content = params.get('content', '')
    pwd = params.get('pwd', '')
    ret = editCut(cutName, content, pwd)
    return ret

@app.route('/get',methods=['POST'])
def fun_get():
    params = request.get_json()
    cutName = params.get('cutName', None)
    pwd = params.get('pwd', '')
    ret = getContent(cutName, pwd)
    return ret


if __name__ == '__main__':
    app.run('0.0.0.0',1010,True)


