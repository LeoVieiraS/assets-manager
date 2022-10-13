import jwt
from models.user import User
from repositories.admin_repository import AdminRepository
from repositories.user_repository import UserRepository
from flask import jsonify, request, g, current_app


def get_payload_from_token():
    token = request.headers.get("Authorization").replace("Bearer ", "")

    if not token:
        return jsonify({"error": "Not Allowed"})

    return jwt.decode(token, current_app.secret_key)


def admin_authorization(f):
    def wrapper(*args, **kwargs):
        payload = get_payload_from_token()
        admin = AdminRepository.find_by_id(payload["id"])
        if not admin:
            return jsonify({"error": "Not Allowed"}), 401

        return f()

    wrapper.__name__ = f.__name__
    return wrapper


def user_authorization(f):
    def wrapper(*args, **kwargs):
        payload = get_payload_from_token()
        user: User = UserRepository.find_by_id(payload["id"])
        if not user:
            return jsonify({"error": "Not Allowed"}), 401
        g.user_id = user.id
        return f()

    wrapper.__name__ = f.__name__
    return wrapper
