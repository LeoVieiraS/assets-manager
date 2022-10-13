from flask import Blueprint
from services.user_service import UserService
from auth.auth import admin_authorization

users_blueprints = Blueprint("users", __name__, url_prefix="/api/v1")


@users_blueprints.route("/users", methods=["POST"])
@admin_authorization
def create():
    return UserService.create_user()
