#!/home/yaya/.pyenv/plugins/python
#coding:utf-8
from flask import session, render_template, url_for, redirect, flash
from flask import request
from app import app, redis_client,db
from app.model.user import User
import json
from datetime import datetime
from app.form.loginer import NameForm
from app.model.user import User, Role
from app.utils.email import send_mail

@app.route('/index', methods=('GET','POST'))
# @app.route('/index',me)
def index():
    # path = app.config['PATH'] #get config  
    print('app content',app.wsgi_app)
    redis_client.set('name','blog',60)  #key value expire
    redis_ = redis_client.get('name').decode('utf-8')  #redis
    # print(redis_)
    
    # session['user'] = "marry"
    # user = {'nickname': session.get('user')} #session
    
    # # if not User.query.filter(User.name=='mini').first():
    # use = User(
    #     name = 'mini',
    #     age = 20,
    #     sex = 1,
    #     email = 'root@root.com'
    # )   
    # db.session.add(use)
    # db.session.commit()          #flask_sqlalchemy

    # query = db.session.query(User.id,User.name).filter(User.name=='mini') #sqlalchemy
    # print(query[0])
    context = {
        'username': u'站长',
        'age': u'18',
        'gender': u'男',
        'redis_':redis_,
        'websites': {
                    'baidu': 'www.baidu.com',
                    'google': 'www.google.com'
        }
        # 'avatar': ''
    }
    # 列表字典混合
    books = [
        {
            'name': u'西游记',
            'author': u'吴承恩',
            'price': 88
        },
        {
            'name': u'三国演义',
            'author': u'罗贯中',
            'price': 98
        }
    ]
    p = redis_client.pipeline()
    keys = redis_client.keys(pattern="top*")
    # n,top_data = redis_client.scan(0, match='top_*', count=5)
    # data = []
    m, data = 0, []
    while True:
        n, top_data = redis_client.scan(m, match='top_*', count=5)
        print(n, top_data)
        if top_data:
            data += top_data 
        if n != 0:
            m = n
        else:
            break
    # dat = p.execute()
    print(keys, data)
    page = request.args.get('page', None)
    if page:
        page = eval(page)
        print(page, type(page))
        context.update({"page":page})
    return render_template('myblog/index.html',**context, user=context, books=books)
    # return render_template('upload_.html')

@app.route('/login<int:user_id>', methods=('POST','GET'))
def login(user_id):
    if user_id == 1:
        user = {
            'username': '站长',
            'age': 22,
            'current_time': datetime.utcnow()  #用moment需用utc

        }
        print(datetime.utcnow())
        return render_template('myblog/login.html', user=user)  # 已经注册则传进去参数
    elif user_id == 2:
        user = {
            'username': '楼主',
            'age': 18
        }
        return redirect(url_for('index', page=user))
    else:
        return render_template('myblog/login.html')  # 没有注册则直接渲染
        
@app.route('/register', methods=('GET', 'POST'))
def register():
    # name = None
    form = NameForm()
    if form.validate_on_submit():
        user = User.query.filter(User.username==form.username.data).first()
        if not user:
            user = User(
                        username=form.username.data,
                        passwd=form.pwd.data
                    )
            db.session.add(user)
            db.session.commit()
            session['known'] = False
        else:
            # send_mail()  #发送email
            session['known'] = True

        session['username'] = form.username.data
        print(session)
        flash('Congratulation you have register success!')
        return redirect(url_for('register'))
    return render_template('myblog/register.html', form=form, \
                                    name=session.get('username'),\
                                    known=session.get('known', False))


@app.route('/change_passwd', methods=('POST', 'GET'))
def change_passwd():
    pass
