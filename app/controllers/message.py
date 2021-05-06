from app.models.message import MessageModel, MessageType
from app.models.user import UserModel
from uuid import uuid4
from utils.s3 import upload_image_to_s3
from utils.base64 import decode_base64_to_file


def store_text_message(user_id, room_id, content):
    MessageModel.insert_message(user_id=user_id,
                                room_id=room_id,
                                content=content,
                                type=MessageType.message)

    user_data = UserModel.user_data_by_user_id(user_id)
    message = MessageModel.latest_message(room_id)
    message_data = {
        "user": {
            "id": user_id,
            "name": user_data.name,
            "img": user_data.img
        },
        "message": content,
        "photo": None,
        "voice": None,
        "createdAt": str(message.created_at)
    }

    return message_data


def store_image_message(user_id: str, room_id: int, content: str):
    image_name = str(uuid4()) + ".png"
    file_bytes = content.encode()
    # string 형식의 base64로 인코딩된 이미지 데이터를 bytes type 으로 변환

    file = decode_base64_to_file(file_bytes)
    # base64 decoding 을 통해 파일 데이터 가져옴

    upload_image_to_s3(file, image_name)

    MessageModel.insert_message(user_id=user_id,
                                room_id=room_id,
                                content=image_name,
                                type=MessageType.photo)

    user_data = UserModel.user_data_by_user_id(user_id)
    message = MessageModel.get_latest_message_in_room(room_id)
    message_data = {
        "user": {
            "id": user_id,
            "name": user_data.name,
            "img": user_data.img
        },
        "message": None,
        "photo": image_name,
        "voice": None,
        "createdAt": str(message.created_at)
    }

    return message_data
