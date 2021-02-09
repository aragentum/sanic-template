from abc import abstractmethod

from sanic_template.database.db import db
from sanic_template.utils.core import Singleton


class BaseRepo(Singleton):
    @abstractmethod
    def get_model(self):
        pass

    async def first(self, pk):
        Model = self.get_model()
        return (await Model.query
                .where(Model.id == pk)
                .gino.first())

    async def exists(self, query) -> bool:
        return await db.scalar(db.exists(query).select())

    async def all(self):
        Model = self.get_model()
        return await Model.query.gino.all()


__all__ = ['BaseRepo']
