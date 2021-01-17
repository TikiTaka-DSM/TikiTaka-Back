from flask import abort
from flask_jwt_extended import jwt_required, get_jwt_identity
from sqlalchemy.exc import SQLAlchemyError

from app.models import session
from app.models.room import Room


def get_room_data_by_room_name(room_name):
    return session.query(Room).filter(Room.name == room_name).first()


def create_room(room_name):
    room = Room(name=room_name)

    session.add(room)
    session.commit()

    return room.id


@jwt_required
def create_new_room(users):
    user_id = get_jwt_identity()
    room_name = f"{user_id}".join(users)

    if get_room_data_by_room_name(room_name) == room_name:
        abort(409, "This room has already been created")

    room_id = create_room(room_name)

    return {
        "roomData": {
            "id": room_id
        }
    }
