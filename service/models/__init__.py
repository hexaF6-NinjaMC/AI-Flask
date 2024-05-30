"""Sets up the database models"""
from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash
from service.extensions import database

# pylint: disable-next=too-few-public-methods
class User(database.Model, UserMixin):
    """The User model"""
    id = database.Column(database.Integer, primary_key=True)
    username = database.Column(database.String, unique=True)
    password = database.Column(database.String, nullable=False)
    is_admin = database.Column(database.Boolean, default=False)

    def create(self, user_name, password_text):
        """Creates a new User"""
        self.username = user_name
        self.password = generate_password_hash(password_text, "scrypt", 32)
        database.session.add(self)
        database.session.commit()
        database.session.close()

    def get_id(self):
        """Retrieves a User public_id"""
        return self.id

    def verify_password(self, password_text):
        """Checks if the password is correct"""
        return check_password_hash(self.password, password_text)

    @classmethod
    def get_user_by_name(cls, name):
        """Retrieves a User by name"""
        return database.one_or_404(database.select(cls).filter_by(username=name))

    @classmethod
    def get_user_by_email(cls, email):
        """Retrieves a User by email"""
        return database.one_or_404(database.select(cls).filter_by(username=email))
