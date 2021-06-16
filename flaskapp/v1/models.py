from enum import unique
from flaskapp import db


class HouseOwner(db.Model):
    __tablename__ = 'house_owner'
    id = db.Column(db.interge, primary_key=True)
    username = db.Column(db.String(64), unique=False)
    phone = db.Coulumn(db.String(32), unique=True)
    wechat = db.Coulumn(db.String(128), unique=True)
    id_card = db.Coulumn(db.String(64), unique=True)

    