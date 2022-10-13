import json
from flask import Blueprint
from services.login_service import LoginService

from auth.auth import admin_authorization

login_blueprints = Blueprint("login", __name__, url_prefix="/api/v1")


@login_blueprints.route("/login", methods=["POST"])
@admin_authorization
def login():
    return LoginService.login()
