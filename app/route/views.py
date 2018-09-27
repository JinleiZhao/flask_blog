#!/home/yaya/.pyenv/plugins/python
#coding:utf-8
from flask import session, render_template
from app import app, redis_client,db
from app.model.user import User


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
    return render_template('index.html',**context, user=context, books=books)
    # return render_template('upload_.html')

@app.route('/login<int:user_id>', methods=('POST','GET'))
def login(user_id):
    if user_id == 1:
        user = {
            'username': u'站长',
            'age': 22
        }
        return render_template('login.html', user=user)  # 已经注册则传进去参数
    else:
        return render_template('login.html')  # 没有注册则直接渲染
        

############获取x内的所有素数############
# In [85]: def primes(x):
#     ...:     # prepair data space
#     ...:     plist = [0, 0] + range(2,x+1)
#     ...:     print(plist)
#     ...:     for i in xrange(2, x):
#     ...:         if plist[i]: #p[0]=0 返回false
#     ...:             print('plist[%d]'%i)
#     ...:             print('plist1',plist[i+i::i],id(plist))
#     ...:             plist[i+i::i] = [0] * len(plist[i+i::i])
#                      p[4::2]       = [0 ,0 ,0 ,0]   #分别用左列表中的元素代替右边对应索引位置的值
#     ...:             print('plist2',plist[i+i::i],id(plist))
#     ...:     return filter(None, plist)  #func为None时，True和False通过iter来确定
