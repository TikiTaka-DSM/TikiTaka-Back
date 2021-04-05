from app.models import session, catch_exception
from app.models.room import Room


@catch_exception
def room_data_by_room_id(room_id):
    return session.query(Room).filter(Room.id == room_id).first()


@catch_exception
def insert_room():
    room = Room(name="")

    session.add(room)
    session.commit()


@catch_exception
def last_room_id():
    room = session.query(Room).order_by(Room.id.desc()).first()
    return room.id
