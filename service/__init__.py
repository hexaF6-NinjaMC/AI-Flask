"""Sets up the app's functionality"""
import os
from dotenv import load_dotenv
from flask import Flask
from flask_cors import CORS
# from flask_jwt_extended import create_access_token, get_jwt, get_jwt_identity, set_access_cookies
from service.models import User
from service.routes import app_bp
from service.error_handling import error_bp
from service.extensions import database, login_manager

app = Flask(__name__)
CORS(app)
load_dotenv()

path = os.getcwd()
UPLOAD_FOLDER = os.path.join(path, os.getenv('UPLOAD_FOLDER'))

if not os.path.isdir(UPLOAD_FOLDER):
    os.mkdir(UPLOAD_FOLDER)

# Set secret key:
app.config["CORS_HEADERS"] = "Content-Type: application/json"
app.config['SECRET_KEY'] = os.getenv('DOPPLER_PROJECT')
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.config['ADMIN_USER_ID'] = os.getenv('ADMIN_USER_ID')
app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('DATABASE_URI')

database.init_app(app)
login_manager.init_app(app)

login_manager.login_view = '/login'

@login_manager.user_loader
def load_user(user_id):
    """Loads the user by their ID from the database"""
    user = database.session.get(User, int(user_id))
    return user

with app.app_context():
    database.create_all()

app.register_blueprint(error_bp)
app.register_blueprint(app_bp)

# Display the environment mode for testing.
mode = os.getenv('DOPPLER_ENVIRONMENT')
if mode:
    print(f"The environment is currently running in \"{mode}\" mode.")
