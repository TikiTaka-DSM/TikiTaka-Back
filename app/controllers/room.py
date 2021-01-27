from flask import abort

from app.models.room import insert_room, get_room_data_by_users_id


def create_new_chatting_room(owner_user, other_user):

    if get_room_data_by_users_id(owner_user, other_user):
        abort(409, "This room has already been created")

    room_id = insert_room(owner_user, other_user)

    return {
        "roomData": {
            "id": room_id
        }
    }


# def get_chatting_rooms(owner_user):
    # rooms = get_rooms_by_name(owner_user)





