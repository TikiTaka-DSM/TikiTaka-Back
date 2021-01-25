from flask import Flask, jsonify
from flask_cors import CORS
from flask_socketio import SocketIO, join_room, emit, leave_room
from app.router import bp
from flask_jwt_extended import JWTManager

import base64, uuid
from json import dumps
from io import BytesIO
from utils.s3 import upload_image_to_s3
from utils.jwt import get_jwt_identity_by_token
from app.models.message import MessageType, Message
from app.models.user import get_user_data_by_user_id
from config.app import LocalAppConfig
from app.models import session


def create_app(*config_cls):

    _app = Flask(__name__)
    _app.register_blueprint(bp)

    for config in config_cls:
        _app.config.from_object(config)

    JWTManager(_app)
    CORS(_app)

    return _app


def create_socketio(_app):
    socketio = SocketIO(_app)

    @socketio.on('sendMessage')
    def receive_text_message(json):
        room_id = json['roomId']
        user_id = get_jwt_identity_by_token(json['token'], LocalAppConfig.JWT_SECRET_KEY)
        content = json['message']

        join_room(room_id)
        message = Message(user_id=user_id,
                          room_id=room_id,
                          content=content,
                          type=MessageType.message)

        session.add(message)
        session.commit()

        _message = session.query(Message).filter(Message.user_id == user_id).filter(Message.room_id == room_id).first()

        user_data = get_user_data_by_user_id(user_id)
        message_data = {
            "user": {
                "id": user_id,
                "name": user_data.name,
                "img": user_data.img
            },
            "message": content,
            "photo": None,
            "voice": None,
            "createdAt": str(_message.created_at)
        }

        emit('realTimeChatting', dumps(message_data), room=room_id)
        leave_room(room_id)

    @socketio.on('test')
    def test():
        emit('test', "test")

    @socketio.on('sendImage')
    def recevie_file(json):
        file_bytes = json['file'].encode()
        file = BytesIO(base64.b64decode(file_bytes))

        upload_image_to_s3(file, str(uuid.uuid4()) + '.png')

    return socketio

