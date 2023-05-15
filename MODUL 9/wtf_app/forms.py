from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField
<<<<<<< HEAD
from wtforms.validators import DataRequired, Email
=======
from wtforms.validators import DataRequired
>>>>>>> 87a6ff3 (poprawka apki nbp)


class LoginForm(FlaskForm):
    username = StringField('username', validators=[DataRequired()])
    password = PasswordField('password', validators=[DataRequired()])
<<<<<<< HEAD


class EmailPasswordForm(FlaskForm):
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
=======
>>>>>>> 87a6ff3 (poprawka apki nbp)
