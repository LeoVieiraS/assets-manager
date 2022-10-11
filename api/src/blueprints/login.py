import json
from flask import jsonify, request, Blueprint
from services.login_service import LoginService

login_blueprints = Blueprint("login", __name__, url_prefix="/api/v1")


@login_blueprints.route("/login", methods=["POST"])
def login():
    return LoginService.login()
