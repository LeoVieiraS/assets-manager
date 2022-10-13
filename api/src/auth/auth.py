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
            return jsonify({"error": "Not Allowed"})

        return f()

    return wrapper


def user_authorization(f):
    def wrapper(*args, **kwargs):
        payload = get_payload_from_token()
        print(payload)
        user: User = UserRepository.find_by_id(payload["id"])
        if not user:
            return jsonify({"error": "Not Allowed"})

        g.user_id = user.id
        print("aaa")
        print(g.get("user_id"))

        return f()

    return wrapper
