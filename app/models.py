from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash
from datetime import datetime
from app.extensions import db

class Users(db.Model, UserMixin):
    __bind_key__ = 'external'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255), nullable=False, unique=True)
    email = db.Column(db.String(255), nullable=False, unique=True)
    date_added = db.Column(db.DateTime, default=datetime.utcnow)
    email_confirmed = db.Column(db.Boolean, default=False, nullable=False)

    # Do some password hashing!
    password_hash = db.Column(db.String(255), nullable=False)
    permitted = db.Column(db.Boolean, default=False, nullable=False)
    
    @property
    def password(self):
        raise AttributeError('Password is not a readable attribute!')
    
    @password.setter
    def password(self, password):
        self.password_hash = generate_password_hash(password)

    def verify_password(self, password):
        return check_password_hash(self.password_hash, password)