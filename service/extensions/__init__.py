"""Set up extensions for use in the application factory pattern."""
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager

database = SQLAlchemy()
login_manager = LoginManager()
