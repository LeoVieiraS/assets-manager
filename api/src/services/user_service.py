from abc import abstractmethod


from flask import request
from models import db
from models.user import User, UserSchema
from repositories.user_repository import UserRepository


class UserService:
    @abstractmethod
    def create_user():
        user_schema = UserSchema()
        user = user_schema.load(request.json, session=db.session)
        user.password = request.json["password"]
        new_user = UserRepository.insert(user)

        return UserSchema(exclude=["password", "password_hash"]).dump(new_user)
