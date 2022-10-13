from flask import jsonify, request, jsonify, current_app
from models.user import User
import jwt


class LoginService:
    def login():
        user: User = User.query.filter_by(email=request.json["email"]).first()
        if not user or not user.verify_password(request.json["password"]):
            return jsonify({"error": "Not allowed"}), 401
        return jsonify(
            {
                "token": jwt.encode({"id": user.id}, current_app.secret_key).decode(
                    "utf-8"
                )
            }
        )
