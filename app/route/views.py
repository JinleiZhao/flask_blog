#!/home/yaya/.pyenv/plugins/python
#coding:utf-8
from flask import session, render_template
from app import app, redis_client,db
from app.model.user import User


@app.route('/', methods=('GET','POST'))
# @app.route('/index',me)
def index():
    # path = app.config['PATH'] #get config  

    redis_client.set('name','blog',60)  #key value expire
    redis_ = redis_client.get('name')  #redis
    print(redis_)
    
    session['user'] = "marry"
    user = {'nickname': session.get('user')} #session
    
    # if not User.query.filter(User.name=='mini').first():
    use = User(
        name = 'mini',
        age = 20,
        sex = 1,
        email = 'root@root.com'
    )   
    db.session.add(use)
    db.session.commit()          #flask_sqlalchemy

    # query = db.session.query(User.id,User.name).filter(User.name=='mini') #sqlalchemy
    # print(query[0])
    return render_template('index.html',user=user)


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
