from flask import abort
from sqlalchemy.exc import SQLAlchemyError

from app.models import session
from app.models.room import Room


def get_room_data_by_room_name(room_name):
    return session.query(Room).filter(Room.name == room_name).first()


def _create_room(room_name):
    room = Room(name=room_name)

    session.add(room)
    session.commit()
    session.close()

    return room.id


def create_new_chatting_room(owner_user, users):
    room_name = f"{owner_user}".join(users)

    if get_room_data_by_room_name(room_name) == room_name:
        abort(409, "This room has already been created")

    room_id = _create_room(room_name)

    return {
        "roomData": {
            "id": room_id
        }
    }
