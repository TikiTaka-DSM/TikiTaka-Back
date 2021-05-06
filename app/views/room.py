from flask import request
from flask_restful import Resource
from flask_jwt_extended import jwt_required, get_jwt_identity

from schematics.models import Model
from schematics.types import StringType, IntType
from app.views import validate_json
from app.controllers.room import create_new_chatting_room, get_chatting_room_detail, get_chatting_rooms


class Rooms(Resource):
    class Schema(Model):
        friend_id = StringType(
            serialized_name='friend',
            required=True,
            max_length=45
        )

    @jwt_required
    def get(self):
        owner_user = get_jwt_identity()

        return get_chatting_rooms(owner_user)

    @validate_json(Schema)
    @jwt_required
    def post(self):
        friend_id = request.json['friend']
        owner_user_id = get_jwt_identity()

        return create_new_chatting_room(owner_user_id, friend_id)



class Room(Resource):
    class Schema(Model):
        room_id = IntType(
            serialized_name='room_id',
            required=True
        )
    @jwt_required
    def get(self, room_id):
        owner_user = get_jwt_identity()

        return get_chatting_room_detail(room_id, owner_user)