from abc import abstractmethod
from models.admin import Admin


class AdminService:
    @abstractmethod
    def find_by_id(id: int) -> Admin:
        return Admin.query.filter_by(id=id).first()
