import traceback
from abc import abstractmethod

from flask import jsonify, g
from models import db
from models.operation import Operation, OperationSchema
from typing import List


class OperationRepository:
    @abstractmethod
    def insert(op: Operation) -> Operation:
        try:
            db.session.add(op)
            db.session.commit()
        except Exception as e:
            print(traceback.format_exception(type(e), e, e.__traceback__))
            return None, (jsonify({"error": "Operation not inserted"}), 500)
        return OperationRepository.find_latest(), None

    @abstractmethod
    def find_latest() -> OperationSchema:
        return db.session.query(Operation).order_by(Operation.id.desc()).first()

    @abstractmethod
    def delete(op: Operation):
        try:
            print(type(op))
            db.session.delete(op)
            db.session.commit()
        except Exception as e:
            print(traceback.format_exception(type(e), e, e.__traceback__))

    @abstractmethod
    def find_all() -> List[Operation]:
        return Operation.query.filter_by(user_id=g.user_id)

    @abstractmethod
    def find_by_id(id: int):
        return Operation.query.filter_by(id=id).first()
