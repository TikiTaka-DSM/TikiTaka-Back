from app.services.message import insert_message, latest_message
from app.models.message import MessageType
from app.services.user import user_data_by_user_id
from uuid import uuid4
from utils.s3 import upload_image_to_s3
from utils.base64 import decode_base64_to_file


def store_text_message(user_id, room_id, content):
    insert_message(user_id=user_id,
                   room_id=room_id,
                   content=content,
                   type=MessageType.message)

    user_data = user_data_by_user_id(user_id)
    message = latest_message(room_id)
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


def store_image_message(user_id, room_id, content):
    image_name = str(uuid4()) + ".png"
    file_bytes = content.encode()
    file = decode_base64_to_file(file_bytes)

    upload_image_to_s3(file, image_name)

    insert_message(user_id=user_id,
                   room_id=room_id,
                   content=image_name,
                   type=MessageType.photo)

    user_data = user_data_by_user_id(user_id)
    message = latest_message(room_id, user_id)
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
