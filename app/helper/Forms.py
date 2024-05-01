from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, EmailField, PasswordField, BooleanField
from wtforms.validators import DataRequired, Email, EqualTo, Length

class CreateUserForm(FlaskForm):
    name = StringField(label='Display name: ', validators=[DataRequired()], render_kw={'placeholder': 'Insert your display name here', 'autofocus': True, 'autocomplete': 'username'})
    email = EmailField(label='Email address: ', validators=[DataRequired(), Email(message='Text in email field is not a valid format.', check_deliverability=True)], render_kw={'placeholder': 'Insert email', 'autocomplete': 'email'})
    password = PasswordField(label='Create password: ', validators=[DataRequired(), EqualTo(fieldname='password_confirmation', message='Passwords must match.'), Length(min=8, max=40, message='Password must be at least 8 characters, and up to 40 characters, long.')], render_kw={'placeholder': 'Create password', 'autocomplete': 'new-passsword'})
    showPassword = BooleanField(label='Show password? ', render_kw={'id': 'showPassword'})
    password_confirmation = PasswordField(label='Confirm password: ', validators=[DataRequired(), EqualTo(fieldname='password', message='Passwords must match.')], render_kw={'placeholder': 'Confirm password', 'autocomplete': 'new-passsword'})
    submitBtn = SubmitField(label='Register')

class LoginForm(FlaskForm):
    email = EmailField(label='Email: ', validators=[DataRequired(), Email(message='Text in email field is not a valid format.', check_deliverability=True)], render_kw={'placeholder': 'Insert email here', 'autofocus': True, 'autocomplete': 'email'})
    password = PasswordField(label='Password: ', validators=[DataRequired()], render_kw={'placeholder': 'Insert password', 'autocomplete': 'current-passsword'})
    showPassword = BooleanField(label='Show password? ', render_kw={'id': 'showPassword'})
    submitBtn = SubmitField(label='Submit')

class UpdateUserForm(FlaskForm):
    new_name = StringField(label='Display name: ')
    new_email = EmailField(label='Email: ', validators=[Email(message='Text in email field is not a valid format.', check_deliverability=True)])
    updateBtn = SubmitField(label='Submit')

class ChangePasswordForm(FlaskForm):
    password = PasswordField(label='Enter new password: ', validators=[DataRequired(), EqualTo(fieldname='password_confirmation', message='Passwords must match.'), Length(min=8, max=40, message='Password must be at least 8 characters, and up to 40 characters, long.')], render_kw={'placeholder': 'Enter new password'})
    showPassword = BooleanField(label='Show password? ', render_kw={'id': 'showPassword'})
    password_confirmation = PasswordField(label='Confirm password: ', validators=[DataRequired(), EqualTo(fieldname='password', message='Passwords must match.')], render_kw={'placeholder': 'Confirm new password'})
    changeBtn = SubmitField(label='Submit')

class NewTokenForm(FlaskForm):
    email = EmailField(label='Email: ', validators=[DataRequired(), Email(message='Text in email field is not a valid format.', check_deliverability=True)], render_kw={'placeholder': 'Insert email here', 'autofocus': True})
    submitBtn = SubmitField(label='Send New Link')

class HTMLEmailForm(FlaskForm):
    email = EmailField(label='Email: ', validators=[DataRequired(), Email(message='Text in email field is not a valid format.', check_deliverability=True)], render_kw={'placeholder': 'Insert email here', 'autofocus': True})
    submitBtn = SubmitField(label='Send HTML Email')