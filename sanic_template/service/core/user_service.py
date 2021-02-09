from typing import List

from sanic_template.database.model.user import User
from sanic_template.database.repo.user_repo import user_repo
from sanic_template.utils.core import Singleton


class UserService(Singleton):
    async def get_all(self) -> List[User]:
        return await user_repo.all()


user_service = UserService()


__all__ = ['user_service']
