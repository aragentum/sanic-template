from sanic.response import json
from sanic import Blueprint

from sanic_template.database.model.user import User

user_bp = Blueprint('user_view_bp')


@user_bp.route("/users")
async def users(request):
    user_data = []
    for user in await User.query.gino.all():
        user_data.append({"first_name": user.first_name,
                          "last_name": user.last_name,
                          "username": user.username})
    return json(user_data)
