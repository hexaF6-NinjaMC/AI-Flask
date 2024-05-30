"""Create Login and File Upload forms"""
# pylint: disable=line-too-long
from flask_wtf import FlaskForm
from wtforms import EmailField, PasswordField, FileField, SubmitField
from wtforms.validators import Length, InputRequired

class RegisterForm(FlaskForm):
    """Create Registration form"""
    username = EmailField(
        "Username:",
        validators=[InputRequired(), Length(1)],
        description="Enter your username.",
        render_kw={"autofocus": True, "autocomplete": True}
    )
    password = PasswordField(
        "Password:",
        validators=[InputRequired(), Length(1)],
        description="Enter your password.",
        render_kw={"autocomplete": True}
    )
    submitBtn = SubmitField("Register")

class LoginForm(FlaskForm):
    """Create Login form"""
    username = EmailField(
        "Username:",
        validators=[InputRequired(), Length(1)],
        description="Enter your username.",
        render_kw={"autofocus": True, "autocomplete": True}
    )
    password = PasswordField(
        "Password:",
        validators=[InputRequired(), Length(1)],
        description="Enter your password.",
        render_kw={"autocomplete": True}
    )
    submitBtn = SubmitField("Login")

class FileUploadForm(FlaskForm):
    """File Upload form"""
    file = FileField(
        "Training File:",
        validators=[InputRequired()],
        description="Upload a file."
    )
    submitBtn = SubmitField("Upload")
