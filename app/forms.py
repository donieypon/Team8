from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField, TextAreaField
from wtforms.validators import ValidationError, DataRequired, Email, EqualTo
from app.models import User


class LoginForm(FlaskForm):
    username = StringField('Username', render_kw={"placeholder": "Enter Username"}, validators=[DataRequired()])
    password = PasswordField('Password', render_kw={"placeholder": "Password"}, validators=[DataRequired()])
    remember_me = BooleanField('Remember Me')
    submit = SubmitField('Sign In')

class createAccount(FlaskForm):
    username = StringField('Username', render_kw={"placeholder": "Enter Username"}, validators=[DataRequired()])
    email = StringField('Email', render_kw={"placeholder": "Enter email"}, validators=[DataRequired(), Email()])
    password = PasswordField('Password', render_kw={"placeholder": "Enter password"}, validators=[DataRequired()])
    password2 = PasswordField(
        'Repeat Password', render_kw={"placeholder": "Re-enter password"}, validators=[DataRequired(), EqualTo('password')])
    submit = SubmitField('Register')

    def validate_username(self, username):
        user = User.query.filter_by(username=username.data).first()
        if user is not None:
            raise ValidationError('Please use a different username.')

    def validate_email(self, email):
        user = User.query.filter_by(email=email.data).first()
        if user is not None:
            raise ValidationError('Please use a valid email address.')

class PostForm(FlaskForm):
    nameTitle = StringField('nameTitle', validators=[DataRequired()])
    content = TextAreaField('content')
    complete = BooleanField('complete')
    submit = SubmitField('Create')

class addFriend(FlaskForm):
    username = StringField('Username', validators=[DataRequired()], description="Enter friend's username")
    message = StringField('Message', description="Send a message")
    add = SubmitField('Add')

class mailForm(FlaskForm):
    email = StringField('Email', validators=[DataRequired()])
    subject = StringField('Subject')
    content = TextAreaField('content', validators=[DataRequired()])
    submit = SubmitField('Send')

