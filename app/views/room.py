from flask import request
from flask_restful import Resource
from flask_jwt_extended import jwt_required, get_jwt_identity

from app.controllers.room import create_new_chatting_room, get_chatting_room_detail, get_chatting_rooms


class CreateNewRoom(Resource):
    @jwt_required
    def post(self):
        friend_id = request.json['friend']
        owner_user_id = get_jwt_identity()

        return create_new_chatting_room(owner_user_id, friend_id)


class GetChattingRooms(Resource):
    @jwt_required
    def get(self):
        owner_user = get_jwt_identity()

        return get_chatting_rooms(owner_user)


class GetChattingRoomDetail(Resource):
    @jwt_required
    def get(self, room_id):
        owner_user = get_jwt_identity()

        return get_chatting_room_detail(room_id, owner_user)