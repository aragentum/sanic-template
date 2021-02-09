from sanic.response import json
from sanic import Blueprint
from sanic_openapi import doc

from sanic_template.service.core.user_service import user_service

user_bp = Blueprint('Users', url_prefix="/users")


@user_bp.route("/users")
@doc.summary("Returns list of users")
async def users(request):
    # good place for run validator
    # ...
    data = await user_service.get_all()
    return json([d.to_response() for d in data])


__all__ = ['user_bp']
