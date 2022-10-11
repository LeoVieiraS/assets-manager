from flask import jsonify, request, jsonify

from models.user import User, UserSchema


class LoginService:
    def login():
        user = User.query.filter_by(email=request.json["email"]).first()
        if not user or not user.verify_password(request.json["password"]):
            return jsonify({"error": "Not allowed"}), 400
        return UserSchema(exclude=["password", "password_hash"]).dump(user), 200
