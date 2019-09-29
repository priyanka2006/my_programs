# creates forms 

from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, Length, Email,EqualTo

class RegisterForm(FlaskForm): # for registration form fields
	username = StringField('Username', validators = [DataRequired(), Length(min = 2, max = 20)])
	email = StringField('Email', validators = [DataRequired(), Email()])
	password = PasswordField('Password', validators = [DataRequired()])
	confirm_password = PasswordField('Confirm_password', validators = [DataRequired(), EqualTo('password')])
	submit = SubmitField('Sign Up')

class LoginForm(FlaskForm): # login form fields
	email = StringField('Email',validators = [DataRequired(), Email()])
	password = PasswordField('password', validators = [DataRequired()])
	submit = SubmitField('Sing In')