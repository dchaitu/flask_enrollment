from flask_wtf import FlaskForm
from wtforms import StringField, BooleanField, IntegerField, SubmitField,PasswordField
from wtforms.validators import DataRequired, Email, Length, EqualTo, ValidationError
from apps.models import User


class LoginForm(FlaskForm):
    email = StringField("Email", validators=[DataRequired(), Email()])
    password = PasswordField("Password", validators=[DataRequired(), Length(min=6, max=12)])
    remember_me = BooleanField("Remember Me")
    submit = SubmitField("Login")


class RegistrationForm(FlaskForm):
    email = StringField("Email", validators=[DataRequired(), Email()])
    password = PasswordField("Password", validators=[DataRequired(), Length(min=6, max=12)])
    password_confirm = PasswordField("Confirm Password",
                                   validators=[DataRequired(), Length(min=6, max=12), EqualTo('password')])
    first_name = StringField("First Name", validators=[DataRequired(), Length(min=2, max=32)])
    last_name = StringField("Last Name", validators=[DataRequired(), Length(min=2, max=32)])
    submit = SubmitField("Register Now")

    def validate_email(self, email):
        user = User.objects(email=email.data).first()
        if user:
            raise ValidationError("Email already in use.Try another.")
