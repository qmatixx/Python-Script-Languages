from flask_wtf import FlaskForm
from wtforms import (StringField, PasswordField,
                     SubmitField, BooleanField, SelectMultipleField)
from wtforms.validators import (DataRequired, Length, Email,
                                EqualTo, ValidationError)
from model.models import User, SpotiClient
from flask_login import current_user


class RegistrationForm(FlaskForm):
    username = StringField('Username',
                           validators=[DataRequired(), Length(min=3, max=20)])
    password = PasswordField('Password',
                             validators=[DataRequired()])
    confirm_password = PasswordField('Confirm Password',
                                     validators=[DataRequired(),
                                                 EqualTo('password')])
    submit = SubmitField('Sign Up')

    def validate_username(self, username):
        user = User.query.filter_by(username=username.data).first()
        if user:
            raise ValidationError('User with this username already exists'
                                  'Please enter another one.')


class LoginForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    remember = BooleanField('Remember Me')
    submit = SubmitField('Login')


class UpdateAccountForm(FlaskForm):
    client_id = StringField('Client Id', validators=[DataRequired()])
    client_secret = StringField('Client Secret', validators=[DataRequired()])
    client_name = StringField('Client Name', validators=[DataRequired()])
    submit = SubmitField('Update')

    # def __init__(self, *args, **kwargs):
    #     super(UpdateAccountForm, self).__init__(*args, **kwargs)
    #     self
        # self.favorite_cameras.choices = [
        #     (camera.id, camera.title) for camera in Camera.query.all()
        # ]

    # def validate_username(self, username):
    #     if username.data != current_user.username:
    #         user = User.query.filter_by(username=username.data).first()
    #         if user:
    #             raise ValidationError('This username is already taken. '
    #                                   'Please choose another one.')