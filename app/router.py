from flask_restful import Api
from flask import Blueprint

from app.views.ping import Ping
from app.views.user import Auth, User


bp = Blueprint("api", __name__, url_prefix="")
api = Api(bp)

api.add_resource(Ping, '/ping')

api.add_resource(User, '/user')
api.add_resource(Auth, '/user/auth')
