from abc import abstractmethod
from models.admin import Admin


class AdminRepository:
    @abstractmethod
    def find_by_id(id):
        return Admin.query.filter_by(id=id).first()
