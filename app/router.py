from flask_restful import Api
from flask import Blueprint

from app.views.ping import Ping


bp = Blueprint("api", __name__, url_prefix="")
api = Api(bp)

api.add_resource(Ping, '/ping')
