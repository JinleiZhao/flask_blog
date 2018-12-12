from flask_wtf import Form
from wtforms import StringField, SubmitField, PasswordField
from wtforms.validators import Required

class NameForm(Form):
    username = StringField('Username:', validators=[Required()])
    pwd = PasswordField('Password:', validators=[Required()])
    submit = SubmitField('register')
