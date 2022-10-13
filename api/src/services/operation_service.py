from abc import abstractmethod
from flask import request, jsonify, g

from repositories.operation_repository import OperationRepository
from models.operation import OperationSchema, Operation
from models import db


class OperationService:
    @abstractmethod
    def create_operation():
        op_schema = OperationSchema()
        op: Operation = op_schema.load(request.json, session=db.session)
        op.user_id = g.user_id
        res, errors = OperationRepository.insert(op)
        if errors:
            return errors
        return op_schema.dump(res)

    @abstractmethod
    def delete_operation(id: int):
        op = OperationRepository.find_by_id(id)
        if not op:
            return jsonify({"error": "Not found"}), 422
        print(op)
        OperationRepository.delete(op)
        return jsonify({"status": "ok"}), 200

    @abstractmethod
    def search_operations():
        op = OperationRepository.find_all()
        operation_schema = OperationSchema()
        list_operations = [operation_schema.dump(o) for o in op]
        return jsonify(list_operations), 200

    @abstractmethod
    def find_opertion_by_id(id):
        op = OperationRepository.find_by_id(id)
        op_schema = OperationSchema()
        return op_schema.dump(op)
