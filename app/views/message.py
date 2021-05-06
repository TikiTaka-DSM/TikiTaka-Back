from flask_restful import Resource
from flask import request
from app.services.jwt import jwt_identity_by_token
from app.models.message import MessageType
from app.controllers.message import store_text_message, store_image_message


class Message(Resource):
    def post(self):
        room_id = request.json['roomId']
        access_token = request.json['token']
        content = request.json['content']
        type = request.json['type']

        if type == MessageType.message:
            return store_text_message(room_id=room_id,
                                      user_id=jwt_identity_by_token(access_token),
                                      content=content)
        elif type == MessageType.photo:
            return store_image_message(room_id=room_id,
                                       user_id=jwt_identity_by_token(access_token),
                                       content=content)
