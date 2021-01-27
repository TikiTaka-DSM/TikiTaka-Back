from sqlalchemy import Column, String, Integer, ForeignKey, or_, and_

from app.models import Base, session, catch_exception


class Room(Base):
    __tablename__ = 'rooms'

    id = Column(Integer, primary_key=True, autoincrement=True)
    user_id = Column(String(45), ForeignKey('users.id'))
    friend_user_id = Column(String(45), ForeignKey('users.id'))


@catch_exception
def get_room_data_by_room_id(room_id):
    return session.query(Room).filter(Room.id == room_id).first()


@catch_exception
def get_room_data_by_users_id(user_id, other_user_id):
    room = session.query(Room).\
            filter((Room.id == user_id & Room.friend_user_id == other_user_id) |
                   (Room.id == other_user_id & Room.friend_user_id == user_id)).first()

    return room


@catch_exception
def insert_room(user_id, friend_user_id):
    room = Room(user_id=user_id, friend_user_id=friend_user_id)

    session.add(room)
    session.commit()
    session.close()

    return room.id
