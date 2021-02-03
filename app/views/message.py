from flask_restful import Resource
from flask import request
from app.services.jwt import get_jwt_identity_by_token
from app.models.message import MessageType
from app.controllers.message import store_text_message


class SaveMessage(Resource):
    def post(self):
        room_id = request.json['roomId']
        access_token = request.json['token']
        content = request.json['content']
        type = request.json['type']

        if type == MessageType.message:
            return store_text_message(room_id=room_id,
                                      user_id=get_jwt_identity_by_token(access_token),
                                      content=content)
