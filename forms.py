from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, PasswordField
from wtforms.validators import DataRequired, URL, Email, Length, Regexp
from flask_ckeditor import CKEditorField
import re

##WTForm
class CreatePostForm(FlaskForm):
    title = StringField("Blog Post Title", validators=[DataRequired()])
    subtitle = StringField("Subtitle", validators=[DataRequired()])
    img_url = StringField("Blog Image URL", validators=[DataRequired(), URL()])
    body = CKEditorField("Blog Content", validators=[DataRequired()])
    submit = SubmitField("Submit Post")

class RegisterForm(FlaskForm):
    email = StringField("Email", validators=[DataRequired(), Email()])
    # password = PasswordField("Password", validators=[DataRequired(), Length(min=8, max=16), Regexp(re.compile(r'^(?=.*[A-Z])(?=.*[a-z])(?=.*[0-9]).{6,16}$'))])
    password = PasswordField("Password", validators=[DataRequired(), Length(min=8, max=16)])
    name = StringField("Name", validators=[DataRequired()])
    submit = SubmitField("Sign me up")

class LoginForm(FlaskForm):
    email = StringField("Email", validators=[DataRequired(), Email()])
    password = PasswordField("Password", validators=[DataRequired()])
    submit = SubmitField("Login")

class CommentForm(FlaskForm):
    comment = CKEditorField("Comment", validators=[DataRequired()])
    submit = SubmitField("Submit Comment")



# VALIDAR PASSWORD
# import re
# password=input("Input password := ")
# pattern = re.compile(r'^(?=.*[A-Z])(?=.*[a-z])(?=.*[0-9]).{6,16}$')
# a=re.search(pattern,password)
# if a==None:
# print("This password is not valid")
# else:
# print("This password is valid")