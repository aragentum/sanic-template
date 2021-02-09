from sanic_template.database.model.user import User
from sanic_template.database.repo.abs.base_repo import BaseRepo


class UserRepo(BaseRepo):

    def get_model(self):
        return User

    async def create_or_update(self, username: str, first_name: str, last_name: str):
        # update
        exists_user = await (User.query
                             .where(User.username == username)
                             .gino.first())
        if exists_user:
            await (exists_user
                   .update(first_name=first_name, last_name=last_name)
                   .apply())
            return exists_user

        # create
        user = await User.create(first_name="Roman",
                                 last_name="Averchenkov",
                                 username="aragentum")
        return user


user_repo = UserRepo()

__all__ = ['user_repo']
