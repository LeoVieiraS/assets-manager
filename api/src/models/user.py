from distutils.command import check
from marshmallow_sqlalchemy import SQLAlchemySchema
from werkzeug.security import generate_password_hash, check_password_hash
from marshmallow import EXCLUDE
from models import db


class User(db.Model):
    __tablename__ = "users"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255), nullable=False)
    surname = db.Column(db.String(255), nullable=False)
    email = db.Column(db.String(255), nullable=False, unique=True)
    password_hash = db.Column(db.String(255), nullable=False)

    @property
    def password(self):
        raise AttributeError("password is not readable attribute")

    @password.setter
    def password(self, password):
        self.password_hash = generate_password_hash(password)

    def verify_password(self, password):
        return check_password_hash(self.password_hash, password)


class UserSchema(SQLAlchemySchema):
    class Meta:
        unknown = EXCLUDE
        model = User
        load_instance = True
        fields = ("id", "email", "password_hash", "name", "surname", "password")
