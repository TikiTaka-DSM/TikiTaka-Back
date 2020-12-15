from flask_restful import Api
from flask import Blueprint


bp = Blueprint("api", __name__, url_prefix="")
api = Api(bp)
