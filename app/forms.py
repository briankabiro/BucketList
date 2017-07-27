from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField
from wtforms.validators import InputRequired, Length

class LoginForm(FlaskForm):
    # the class for the login form
    username = StringField(
        'Username', validators=[InputRequired(),
                                Length(min=1)])
    password = PasswordField(
        'Password', validators=[InputRequired(),
                                Length(min=1)])


class RegisterForm(FlaskForm):
    # the class for the sign up form
    username = StringField(
        'Username', validators=[InputRequired(),
                                Length(min=1)])
    password = PasswordField(
        'Password', validators=[InputRequired(),
                                Length(min=1)])
