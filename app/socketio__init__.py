import base64, uuid
from json import dumps
from io import BytesIO

from utils.s3 import upload_image_to_s3
from app.services.jwt import get_jwt_identity_by_token
from flask_socketio import SocketIO, join_room, emit, leave_room
from app.controllers.message import store_text_message


def create_socketio(_app):
    socketio = SocketIO(_app)

    @socketio.on('test')
    def test():
        emit('test', "test")

    @socketio.on('joinRoom')
    def join_room(data):
        room_id = data['roomId']

        join_room(room_id)


    @socketio.on('sendMessage')
    def receive_text_message(data):
        room_id = data['roomId']
        user_id = get_jwt_identity_by_token(data['token'])
        content = data['message']

        message_data = store_text_message(user_id, room_id, content)

        emit('realTimeChatting', dumps(message_data), room=room_id)

    return socketio