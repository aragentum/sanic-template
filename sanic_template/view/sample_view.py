from sanic import Blueprint
from sanic.response import json

sample_bp = Blueprint('sample_view_bp')


@sample_bp.route("/")
async def index(request):
    return json({"success": True})
