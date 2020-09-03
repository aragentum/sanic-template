from gino import Gino

db = Gino()


class BaseModel(db.Model):
    __abstract__ = True
    __table_args__ = {"extend_existing": True}
