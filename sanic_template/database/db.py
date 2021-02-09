import datetime
from typing import List, Dict

from gino import Gino
from sqlalchemy.dialects.postgresql import insert

from sanic_template.error.exc import SQLOperationException
from sanic_template.service.helper.date_format_service import date_format_service

db = Gino()


class BaseModel(db.Model):
    __abstract__ = True
    __table_args__ = {"extend_existing": True}

    @classmethod
    async def bulk_create(cls,
                          items: List[Dict],
                          return_columns: list = None) -> list:
        if return_columns is None:
            return_columns = cls.id
        result = await (insert(cls.__table__)
                        .values(items)
                        .on_conflict_do_nothing(index_elements=[cls.id])
                        .returning(return_columns)
                        .gino.all())
        if len(result) != len(items):
            raise SQLOperationException("Bulk update exception")
        return result

    def to_dict(self, fields: list) -> dict:
        data = dict()
        for f in fields:
            value = getattr(self, f, None)
            if isinstance(value, datetime.datetime):
                value = date_format_service.format_datetime(value)
            elif isinstance(value, datetime.date):
                value = date_format_service.format_date(value)
            elif isinstance(value, int):
                pass
            else:
                value = str(value)
            data[f] = value
        return data

    def to_response(self):
        raise NotImplemented("function to_response not implemented")
