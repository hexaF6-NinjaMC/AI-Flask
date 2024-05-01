"""Sets up the app's functionality"""
import os
from flask import Flask
from dotenv import load_dotenv
from flask_cors import CORS
from app.routes import app_bp
from app.error_handling import error_bp

app = Flask(__name__)
CORS(app)
load_dotenv()

# Set secret key:
app.config["CORS_HEADERS"] = "Content-Type: application/json"
app.config['SECRET_KEY'] = os.environ.get('DOPPLER_PROJECT')
app.config['SESSION_COOKIE_NAME'] = "shared_cookie"
app.config['SESSION_COOKIE_DOMAIN'] = ".localhost"
app.config['REMEMBER_COOKIE_DOMAIN'] = ".localhost"
app.config['REMEMBER_COOKIE_SECURE'] = None
app.register_blueprint(error_bp)
app.register_blueprint(app_bp)

# Display the environment mode for testing.
mode = os.getenv('DOPPLER_ENVIRONMENT')
if mode:
    print(f"The environment is currently running in \"{mode}\" mode.")
