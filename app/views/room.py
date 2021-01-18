from flask import request
from flask_restful import Resource
from flask_jwt_extended import jwt_required, get_jwt_identity

from app.controllers.room import create_new_chatting_room


class Room(Resource):
    def get(self):
        pass


class CreateNewRoom(Resource):
    @jwt_required
    def post(self):
        users = request.json['people']
        owner_user = get_jwt_identity()

        return create_new_chatting_room(owner_user, users)
