from sqlalchemy import Column, String, Integer
from app.models import Base, session


class RoomModel(Base):
    __tablename__ = 'rooms'

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(45))

    @staticmethod
    def get_room_data_by_room_id(room_id):
        return session.query(RoomModel).filter(RoomModel.id == room_id).first()

    @staticmethod
    def insert_room():
        room = RoomModel(name="")

        session.add(room)
        session.commit()

    @staticmethod
    def get_last_room_id():
        room = session.query(RoomModel).order_by(RoomModel.id.desc()).first()
        return room.id

