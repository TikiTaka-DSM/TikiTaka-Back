from app.services.message import insert_message
from app.models.message import MessageType
from app.services.user import get_user_data_by_user_id


def store_text_message(user_id, room_id, content):
    message = insert_message(user_id=user_id,
                             room_id=room_id,
                             content=content,
                             type=MessageType.message)

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
        "createdAt": str(message.created_at)
    }

    return message_data
