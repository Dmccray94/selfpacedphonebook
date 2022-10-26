from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validarots import Datarequirea, Email

class UserLogInForm(Flaskform):
    email = StringField('Email',validators = [Datarequired(), Email()])
    email = PasswordField('Password', validators = [Datarequired(), Email()])
    email = SubmitField()