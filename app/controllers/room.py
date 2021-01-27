from app.services.member import get_room_id
from app.services.room import insert_room


def create_new_chatting_room(owner_user_id, friend_user_id):
    room_id = get_room_id(owner_user_id, friend_user_id)

    if not room_id:
        room_id = insert_room()

    return {
        "roomData": {
            "id": room_id
        }
    }
