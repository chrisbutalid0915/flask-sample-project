from . import db


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True, index=True)
    username = db.Column(db.String(64), index=True, unique=True)
    email = db.Column(db.String(120), index=True, unique=True)
    password_hash = db.Column(db.String(128), nullable=False)
    disabled = db.Column(db.Boolean, default=False)

    def __init__(self, **kwargs) -> None:
        super(User, self).__init__(**kwargs)


class Address(db.Model):
    id = db.Column(db.Integer, primary_key=True, index=True)
    location = db.Column(db.String(64), index=True, unique=False)
    latitude = db.Column(db.Float)
    longitude = db.Column(db.Float)

    def __init__(self, **kwargs) -> None:
        super(Address, self).__init__(**kwargs)