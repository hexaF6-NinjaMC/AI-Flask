from flask import Flask
from dotenv import load_dotenv
import os
from flask_cors import CORS

app = Flask(__name__)
CORS(app, supports_credentials=True)
load_dotenv()

# Set secret key:
app.config['SECRET_KEY'] = os.environ.get('DOPPLER_PROJECT')
# Make it easier to use:
skey = app.config['SECRET_KEY']
app.config['SESSION_COOKIE_NAME'] = "shared_cookie"
app.config['SESSION_COOKIE_DOMAIN'] = ".localhost"
app.config['REMEMBER_COOKIE_DOMAIN'] = ".localhost"
app.config['REMEMBER_COOKIE_SECURE'] = None

from app.views import app_bp
app.register_blueprint(app_bp)

# Display the environment mode for testing.
mode = os.environ.get('DOPPLER_ENVIRONMENT')
if mode:
    print(f"The environment is currently running in \"{mode}\" mode.")