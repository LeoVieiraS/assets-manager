from flask import Flask
from flask_jwt import JWT
from flask_migrate import Migrate
from blueprints.users import users_blueprints
from blueprints.login import login_blueprints
from blueprints.operations import operations_blueprints
from models import db, ma
from models.admin import Admin


def configure(app):
    app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///project.sqlite"
    app.config["JWT_AUTH_USERNAME_KEY"] = "email"
    app.config["SECRET_KEY"] = "batata"
    db.init_app(app)
    Migrate(app, db)
    ma.init_app(app)
    register_blueprints(app)


def register_blueprints(app):
    app.register_blueprint(operations_blueprints)
    app.register_blueprint(users_blueprints)
    app.register_blueprint(login_blueprints)


def create_app():
    app = Flask(__name__)
    configure(app)
    return app
