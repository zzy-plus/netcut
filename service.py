import os
from utils import *
import json
import random
import time


# 新增cut
def newCut(cutName=None, public=True, pwd:str='', content=''):
    if not public and pwd == '':
        return {'status':False, 'data': '', 'msg': '密码不能为空'}
    if cutName is None: #随机生成cutName
        randCutName = ''.join(random.sample('zyxwvutsrqponmlkjihgfedcba1234567890', 8)) + str(round(time.time() * 1000))
        cutData = {
            'cutName': randCutName,
            'public': public,
            'pwd': '' if public else pwd,
            'content': content
        }
        with open('./cuts/' + randCutName + '.json', 'w', encoding='utf-8') as f:
            json.dump(cutData, f)
        return {'status':True, 'data': cutData, 'msg': '新建cut成功'}
    else:   #如果传入了cutName
        if isCutExist(cutName):    #如果存在
            return {'status':False, 'data':'', 'msg': '该剪切板已存在'}
        cutData = {
            'cutName': cutName,
            'public': public,
            'pwd': '' if public else pwd,
            'content': content
        }
        with open('./cuts/' + cutName + '.json', 'w', encoding='utf-8') as f:
            json.dump(cutData, f)
        return {'status':True, 'data':cutData, 'msg': '新建cut成功'}

# 删除cut
def delCut(cutName:str):
    if isCutExist(cutName):
        os.remove('./cuts/' + cutName + '.json')
        return {'status':True, 'data':cutName, 'msg': '删除成功'}
    return {'status': False, 'data': cutName, 'msg': '删除失败:cut不存在'}


# 修改cut
def editCut(cutName, content, pwd=''):
    if not isCutExist(cutName):
        res = newCut(cutName=cutName, content=content)
        if res['status']:
            return {'status': True, 'data': {'cutName':res['data']['cutName'], 'content':content}, 'msg': 'cut不存在，已新建'}
        else:
            return {'status': True, 'data': '', 'msg': res['msg']}
    # 读取cut内容:
    with open('./cuts/' + cutName +'.json', 'r', encoding='utf-8') as f:
        cutData = json.load(f)

    if cutData['public'] or cutData['pwd'] == pwd :   #如果鉴权成功
        cutData['content'] = content
        with open('./cuts/' + cutName +'.json', 'w', encoding='utf-8') as f:
            json.dump(cutData,f)
        return {'status': True, 'data': {'cutName':cutName, 'content':content}, 'msg': '修改成功'}
    else:
        return {'status': False, 'data': '', 'msg': '鉴权失败'}


# 获取cut保存的内容
def getContent(cutName, pwd=''):
    if not isCutExist(cutName):
        return {'status': False, 'data': '', 'msg': 'cut不存在'}
        # 读取cut内容:
    with open('./cuts/' + cutName + '.json', 'r', encoding='utf-8') as f:
        cutData = json.load(f)
    if cutData['public'] or cutData['pwd'] == pwd:  # 如果鉴权成功
        return {'status': True, 'data': cutData['content'], 'msg': '查询成功'}
    else:
        return {'status': False, 'data': '', 'msg': '鉴权失败'}

