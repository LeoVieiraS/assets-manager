from flask import Blueprint
from auth.auth import user_authorization
from services.operation_service import OperationService

operations_blueprints = Blueprint("operations", __name__, url_prefix="/api/v1")


@operations_blueprints.route("/operations", methods=["GET"])
@user_authorization
def find_all():
    return OperationService.search_operations()


@operations_blueprints.route("/operations", methods=["POST"])
def create():
    return OperationService.create_operation()


@operations_blueprints.route("/operations/<id>", methods=["DELETE"])
def delete(id):
    return OperationService.delete_operation(id)


@operations_blueprints.route("/operations/<id>", methods=["GET"])
def find_by_id(id):
    return OperationService.find_opertion_by_id(id)
