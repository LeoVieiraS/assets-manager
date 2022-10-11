from flask import Blueprint
from services.user_service import UserService
from models import db

users_blueprints = Blueprint("users", __name__, url_prefix="/api/v1")


@users_blueprints.route("/users", methods=["POST"])
def create():
    return UserService.create_user()
