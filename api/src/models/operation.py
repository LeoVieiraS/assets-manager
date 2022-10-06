from flask import current_app, session
from marshmallow import EXCLUDE
from marshmallow_sqlalchemy import SQLAlchemySchema
from models import db


class Operation(db.Model):

    id = db.Column(db.Integer, primary_key=True)
    operation_type = db.Column(db.String, nullable=False)
    asset = db.Column(db.String, nullable=False)
    quantity = db.Column(db.Float, nullable=False)
    peer_coin = db.Column(db.String, nullable=False)
    peer_coin_total_value = db.Column(db.Float, nullable=False)
    type_value = db.Column(db.String, nullable=False)
    usd_total_value = db.Column(db.Float, nullable=False)
    usd_unit_price = db.Column(db.Float, nullable=False)
    fee = db.Column(db.Float, nullable=False)
    usd_fee = db.Column(db.Float, nullable=False)
    coin_fee = db.Column(db.String, nullable=False)


class OperationSchema(SQLAlchemySchema):
    class Meta:
        unknown = EXCLUDE
        model = Operation
        load_instance = True
        fields = (
            "id",
            "operation_type",
            "asset",
            "quantity",
            "peer_coin",
            "peer_coin_total_value",
            "type_value",
            "usd_total_value",
            "usd_unit_price",
            "fee",
            "usd_fee",
            "coin_fee",
        )
