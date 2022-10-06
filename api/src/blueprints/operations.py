from flask import Blueprint, jsonify
from models import db
from models.operation import Operation, OperationSchema
from flask import request, Response

operations_blueprints = Blueprint("users", __name__)


@operations_blueprints.route("/operations", methods=["GET"])
def find_all():
    op = Operation.query.all()
    operation_schema = OperationSchema()
    list_operations = [operation_schema.dump(o) for o in op]
    return jsonify(list_operations), 200


@operations_blueprints.route("/operations", methods=["POST"])
def create():
    op_schema = OperationSchema()
    op = op_schema.load(request.json, session=db.session)
    db.session.add(op)
    db.session.commit()

    obj = db.session.query(Operation).order_by(Operation.id.desc()).first()
    return op_schema.dump(obj)


@operations_blueprints.route("/operations/<id>", methods=["DELETE"])
def delete(id):
    op = Operation.query.filter_by(id=id).first()
    if not op:
        return "not found"
    try:
        db.session.delete(op)
        db.session.commit()
    except Exception as e:
        print(e)
        return jsonify("error"), 500
    return Response(status=200)


@operations_blueprints.route("/operations/<id>", methods=["GET"])
def find_by_id(id):
    obj = Operation.query.filter_by(id=id).first()
    op_schema = OperationSchema()
    return op_schema.dump(obj)
