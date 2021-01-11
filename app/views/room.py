from flask import request
from flask_restful import Resource


class Room(Resource):
    def get(self):
        pass

    def post(self):
        users = request.json['people']

        pass
