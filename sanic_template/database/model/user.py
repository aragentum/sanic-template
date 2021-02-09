from sanic_template.database.db import BaseModel, db


class User(BaseModel):
    __tablename__ = "users"

    id = db.Column(db.BigInteger(), primary_key=True, index=True, unique=True)
    first_name = db.Column(db.Unicode(200))
    last_name = db.Column(db.Unicode(200))
    username = db.Column(db.Unicode(200), index=True, unique=True)
    created_at = db.Column(db.DateTime(), server_default=db.func.now())

    def to_response(self):
        return self.to_dict([
            "id",
            "first_name",
            "last_name",
            "username",
            "created_at"
        ])
