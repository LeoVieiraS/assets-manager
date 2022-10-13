from models import db


class Admin(db.Model):
    __tablename__ = "admins"

    id = db.Column(db.Integer, primary_key=True)
    device = db.Column(db.String(255), nullable=True)
    app_name = db.Column(db.String(255), nullable=True)
    start_date = db.Column(db.String(255), nullable=True)
