from sanic import Blueprint
from sanic.response import json

sample_bp = Blueprint('Sample')


@sample_bp.route("/")
async def index(request):
    return json({"success": True})
