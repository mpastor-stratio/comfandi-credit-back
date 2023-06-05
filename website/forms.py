from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, IntegerField
from wtforms.validators import DataRequired, Email, Length, EqualTo

class SignUpForm(FlaskForm):
    email = StringField('email', validators=[DataRequired(), Email()])
    firstName = StringField('firstName', validators=[DataRequired(), Length(min=2, max=50)])
    password1 = PasswordField('password1', validators=[DataRequired(), Length(min=7, max=120)])
    password2 = PasswordField('password2', validators=[DataRequired(), EqualTo('password1', message='Passwords must match')])
    rol_id = IntegerField('rol_id', validators=[DataRequired()])