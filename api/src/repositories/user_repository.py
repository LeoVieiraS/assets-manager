from inspect import trace
import traceback
from abc import abstractmethod
from typing import Union
from models import db
from models.user import User


class UserRepository:
    @abstractmethod
    def insert(user: User) -> User:
        try:
            db.session.add(user)
            db.session.commit()
        except Exception as e:
            traceback.format_exception(type(e), e, e.__traceback__)
        return UserRepository.find_latest()

    def find_latest() -> Union[User, None]:
        return db.session.query(User).order_by(User.id.desc()).first()

    @abstractmethod
    def find_by_email(email: str) -> Union[User, None]:
        user = User.query.filter_by(email=email).first()
        return user

    @abstractmethod
    def find_by_id(id: int) -> Union[User, None]:
        return User.query.filter_by(id=id).first()

    @abstractmethod
    def delete(email: str) -> bool:
        ...
