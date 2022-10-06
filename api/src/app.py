from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from blueprints.operations import operations_blueprints
from flask_marshmallow import Marshmallow
from models import ma
from models import db


def create_app():
    app = Flask(__name__)

    app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///project.sqlite"
    db.init_app(app)
    Migrate(app, db)
    ma.init_app(app)
    app.register_blueprint(operations_blueprints)

    return app
