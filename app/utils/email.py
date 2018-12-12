import os
from flask_mail import Message
from app import mail, app
from threading import Thread

def send_async_email(app, msg):
    with app.app_context():
        mail.send(msg)

def send_mail():
    print(app.config['MAIL_USERNAME'])
    msg = Message('My Test', sender=app.config['MAIL_USERNAME'], recipients=['298518760@qq.com'])
    msg.body = 'test mail'
    msg.html = '<b> HTML %s </b>'%msg.body
    # mail.send(msg)
    # print(mail)
    th = Thread(target=send_async_email, args=[app, msg])
    th.start()
    return th