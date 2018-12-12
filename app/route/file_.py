import os
import io # py2 StringIO
import time
import uuid
import six
import oss2
from PIL import Image
from datetime import datetime
from flask import Flask, request, redirect, render_template, jsonify
from werkzeug.utils import secure_filename
from app import app
from flask import g

def oss_filename(file):
    time_ = str(time.time())[:6]
    uuid_ = str(uuid.uuid4()).split('-')[0]
    return '%s%s' % (time_+"_"+uuid_,
                     os.path.splitext(file.filename)[-1])


def time_dir():
    now = datetime.now()
    year = str(now.year)
    month = str(now.month) if now.month >= 10 else '0'+str(now.month)
    return year+month+'/'

def loc_file_name(file):
    time_ = str(time.time())[:6]
    uuid_ = str(uuid.uuid4()).split('-')[0]
    return '%s/%s%s' % (time.strftime('%Y%m/%d'),time_+"_"+uuid_,
                    os.path.splitext(file.filename)[-1])

def save_img(file):  #保存图片，本地/oss
    dirname = os.path.join(app.config['PATH'],'app/static/img/'+loc_file_name(file)) #xxx/xxx/xx.png 图片位置和名称
    path = os.path.dirname(dirname) # xxx/xxx/  图片的所在目录
    try:
        file_ = io.BytesIO(file.read()) #写入io  py3{StringIO,BytesIO} py2{StringgIO}  
        f = file_.getvalue()  #读取数据
    except:
        raise
    finally:
        file_.close()
    '!!!!!!!!!!!!!!!!!!!!!上传本地!!!!!!!!!!!!!!!!!!!!!!!!'
    if not os.path.exists(path):   #创建目录
        os.makedirs(path)
    open(dirname,'wb').write(f)  #写入
    return dirname
    '!!!!!!!!!!!!!!!!!!!!!上传oss!!!!!!!!!!!!!!!!!!!!!!!!!'
    remote_file = oss_filename(file)  #oss存储名称
    #oss 配置
    # auth = oss2.Auth(app.config['ACCESS_KEY_ID'], app.config['ACCESS_KEY_SECRET'])
    # bucket = oss2.Bucket(auth, app.config['ENDPOINT'], app.config['ALI_BUCKET'])
    # bucket.put_object(time_dir()+remote_file, f)  #上传到oss，直接在内存中读取

@app.route('/file', methods=('GET',))
def file():
    g.user = 'zhangsan'
    print(g.user)
    return render_template('myblog/upload_.html', user=g.user)

@app.route('/upload_file', methods=('POST',))
def upload_file():   
    # file = request.files['file']  #获取指定的file
    # print(file.filename) 
    # print(g.user)
    file = request.files.values()   #获取所有的file 
    for f in file:
        file = f
        img = save_img(file)
        url = img.split('app')[-1]
    return jsonify({'succ':True,'file':url})

